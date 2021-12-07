import os
import torch
import torch.optim as optim
import torch.nn as nn
import argparse
import shutil
import json
from tqdm import tqdm
from datetime import date
from utils.misc import MetricLogger, seed_everything, ProgressBar
from utils.data import DataLoader, DistributedDataLoader, prepare_dataset
from transformers import BartConfig, BartForConditionalGeneration, BartTokenizer

import torch.optim as optim
import logging
import time
from utils.lr_scheduler import get_linear_schedule_with_warmup
from .predict import validate

import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data.distributed import DistributedSampler

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query

def train(args):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    if args.local_rank in [-1, 0]:
        logging.info("Create train_loader and val_loader.........")
    vocab_json = os.path.join(args.input_dir, 'vocab.json')
    train_pt = os.path.join(args.input_dir, 'train.pt')
    val_pt = os.path.join(args.input_dir, 'val.pt')
    
    if args.n_gpus > 1:
        train_dataset, train_vocab = prepare_dataset(vocab_json, train_pt, training=True, pretrain=args.pretrain)
        train_sampler = DistributedSampler(train_dataset)
        train_loader = DistributedDataLoader(train_dataset, train_vocab, args.batch_size//args.n_gpus, train_sampler, pretrain=args.pretrain)
    else:
        train_loader = DataLoader(vocab_json, train_pt, args.batch_size, training=True, pretrain=args.pretrain)
    val_loader = DataLoader(vocab_json, val_pt, args.batch_size, training=False, pretrain=False)
    

    if args.local_rank in [-1, 0]:
        logging.info("Create model.........")
    config_class, model_class, tokenizer_class = (BartConfig, BartForConditionalGeneration, BartTokenizer)
    tokenizer = tokenizer_class.from_pretrained(args.model_name_or_path)
    model = model_class.from_pretrained(args.model_name_or_path)  
    model.resize_token_embeddings(len(tokenizer))
    
    if args.n_gpus > 1:
        # model = nn.DataParallel(model)
        model = nn.SyncBatchNorm.convert_sync_batchnorm(model).cuda()
        model = DDP(model, device_ids=[args.local_rank], output_device=args.local_rank, find_unused_parameters=True)
    else:
        model = model.to(device)

    t_total = len(train_loader) // args.gradient_accumulation_steps * args.num_train_epochs    # Prepare optimizer and schedule (linear warmup and decay)
    no_decay = ["bias", "LayerNorm.weight"]
    bart_param_optimizer = list(model.named_parameters())
    optimizer_grouped_parameters = [
        {'params': [p for n, p in bart_param_optimizer if not any(nd in n for nd in no_decay)],
         'weight_decay': args.weight_decay, 'lr': args.learning_rate},
        {'params': [p for n, p in bart_param_optimizer if any(nd in n for nd in no_decay)], 'weight_decay': 0.0,
         'lr': args.learning_rate}
    ]
    args.warmup_steps = int(t_total * args.warmup_proportion)
    optimizer = optim.AdamW(optimizer_grouped_parameters, lr=args.learning_rate, eps=args.adam_epsilon)
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=args.warmup_steps,
                                                num_training_steps=t_total)
    # Check if saved optimizer or scheduler states exist
    if os.path.isfile(os.path.join(args.model_name_or_path, "optimizer.pt")) and os.path.isfile(
            os.path.join(args.model_name_or_path, "scheduler.pt")):
        # Load in optimizer and scheduler states
        optimizer.load_state_dict(torch.load(os.path.join(args.model_name_or_path, "optimizer.pt")))
        scheduler.load_state_dict(torch.load(os.path.join(args.model_name_or_path, "scheduler.pt")))

    # Train!
    if args.local_rank in [-1, 0]:
        logging.info("***** Running training *****")
        logging.info("  Num examples = %d", len(train_loader.dataset))
        logging.info("  Num Epochs = %d", args.num_train_epochs)
        logging.info("  Gradient Accumulation steps = %d", args.gradient_accumulation_steps)
        logging.info("  Total optimization steps = %d", t_total)

    global_step = 0
    steps_trained_in_current_epoch = 0
    # Check if continuing training from a checkpoint
    if os.path.exists(args.model_name_or_path) and "checkpoint" in args.model_name_or_path:
    #     # set global_step to gobal_step of last saved checkpoint from model path
    #     global_step = int(args.model_name_or_path.split("-")[-1].split("/")[0])
    #     epochs_trained = global_step // (len(train_loader) // args.gradient_accumulation_steps)
    #     steps_trained_in_current_epoch = global_step % (len(train_loader) // args.gradient_accumulation_steps)
        logging.info("  Continuing training from checkpoint, will skip to saved global_step")
    #     logging.info("  Continuing training from epoch %d", epochs_trained)
    #     logging.info("  Continuing training from global step %d", global_step)
    #     logging.info("  Will skip the first %d steps in the first epoch", steps_trained_in_current_epoch)
    
    if args.local_rank in [-1, 0]:
        logging.info('Checking...')
        logging.info("===================Dev==================")
    
    tr_loss, logging_loss = 0.0, 0.0
    best_acc, current_acc = 0.0, 0.0
    model.zero_grad()
    # prefix = 0
    if args.local_rank in [-1, 0]:
        print("Current performance on validation set: %f" % (current_acc))
    
    args.logging_steps = round(len(train_dataset)/args.batch_size) // 2
    args.save_steps = args.logging_steps
    epochs_not_improving = 0
    
    for epoch_i in range(int(args.num_train_epochs)):
        if args.n_gpus > 1:
            train_loader.sampler.set_epoch(epoch_i)
        pbar = ProgressBar(n_total=len(train_loader), desc='Training')
        epochs_not_improving += 1
        for step, batch in enumerate(train_loader):
            # Skip past any already trained steps if resuming training
            if steps_trained_in_current_epoch > 0:
                steps_trained_in_current_epoch -= 1
                continue
            model.train()
            batch = tuple(t.to(device) for t in batch)
            pad_token_id = tokenizer.pad_token_id
            if not args.pretrain:
                source_ids, source_mask, y = batch[0], batch[1], batch[-2]  
            else:
                source_ids, source_mask, y = batch[0], batch[1], batch[2]
            y_ids = y[:, :-1].contiguous()
            labels = y[:, 1:].clone()
            labels[y[:, 1:] == pad_token_id] = -100

            inputs = {
                "input_ids": source_ids.to(device),
                "attention_mask": source_mask.to(device),
                "decoder_input_ids": y_ids.to(device),
                "labels": labels.to(device),
            }
            outputs = model(**inputs)
            loss = outputs[0]
            if torch.cuda.device_count() > 1:
                loss = loss.sum()
            loss.backward()
            pbar(step, {'loss': loss.item()})
            tr_loss += loss.item()
            if (step + 1) % args.gradient_accumulation_steps == 0:
                torch.nn.utils.clip_grad_norm_(model.parameters(), args.max_grad_norm)
                optimizer.step()
                scheduler.step()  # Update learning rate schedule
                model.zero_grad()
                global_step += 1

            if args.logging_steps > 0 and global_step % args.logging_steps == 0 and args.local_rank in [-1, 0]:
                logging.info("===================Dev==================")
                current_acc = validate(args, model, val_loader, device, tokenizer)
                print("Current best performance on validation set: %f" % (best_acc))

            if args.save_steps > 0 and global_step % args.save_steps == 0 and current_acc > best_acc and args.local_rank in [-1, 0]:
                epochs_not_improving = 0
                best_acc = current_acc
                print("Best performance on validation set updated: %f" % (best_acc))
                # Save model checkpoint
                # output_dir = os.path.join(args.output_dir, "checkpoint-{}".format(global_step + prefix))
                output_dir = os.path.join(args.output_dir, "checkpoint-best")
                if not os.path.exists(output_dir) and args.local_rank in [-1, 0]:
                    os.makedirs(output_dir)
                model_to_save = (
                    model.module if hasattr(model, "module") else model
                )  # Take care of distributed/parallel training
                model_to_save.save_pretrained(output_dir)
                torch.save(args, os.path.join(output_dir, "training_args.bin"))
                logging.info("Saving model checkpoint to %s", output_dir)
                tokenizer.save_vocabulary(output_dir)
                torch.save(optimizer.state_dict(), os.path.join(output_dir, "optimizer.pt"))
                torch.save(scheduler.state_dict(), os.path.join(output_dir, "scheduler.pt"))
                logging.info("Saving optimizer and scheduler states to %s", output_dir)
            
            if args.n_gpus > 1:
                dist.barrier()
        
        if 'cuda' in str(device):
            torch.cuda.empty_cache()
        if epochs_not_improving > args.early_stopping:
            logging.info("%d epochs not improving, training early stopped" % epochs_not_improving)
            return global_step, tr_loss / global_step
    
    return global_step, tr_loss / global_step


def main():
    parser = argparse.ArgumentParser()
    # input and output
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)

    parser.add_argument('--save_dir', required=True, help='path to save checkpoints and logs')
    parser.add_argument('--model_name_or_path', required=True, help='pretrained language models')
    parser.add_argument('--ckpt')

    # training parameters
    parser.add_argument('--weight_decay', default=1e-5, type=float)
    parser.add_argument('--batch_size', default=16, type=int)
    parser.add_argument('--seed', type=int, default=666, help='random seed')
    parser.add_argument('--learning_rate', default=3e-5, type=float)
    parser.add_argument('--num_train_epochs', default=25, type=int)
    parser.add_argument('--save_steps', default=448, type=int)
    parser.add_argument('--logging_steps', default=448, type=int)
    parser.add_argument('--early_stopping', default=5, type=int)
    parser.add_argument('--warmup_proportion', default=0.1, type=float,
                        help="Proportion of training to perform linear learning rate warmup for,E.g., 0.1=10% of training.")
    parser.add_argument("--adam_epsilon", default=1e-8, type=float,
                        help="Epsilon for Adam optimizer.")
    parser.add_argument("--gradient_accumulation_steps", type=int, default=1,
                        help="Number of updates steps to accumulate before performing a backward/update pass.", )
    parser.add_argument("--max_grad_norm", default=1.0, type=float,
                        help="Max gradient norm.")
    
    parser.add_argument('--pretrain', action='store_true')
    parser.add_argument('--local_rank', default=-1, type=int,
                    help='node rank for distributed training')
    parser.add_argument('--port', default=12355, type=int)
    
    # validating parameters
    # parser.add_argument('--num_return_sequences', default=1, type=int)
    # parser.add_argument('--top_p', default=)
    
    # model hyperparameters
    parser.add_argument('--dim_hidden', default=1024, type=int)
    parser.add_argument('--alpha', default = 1e-4, type = float)
    args = parser.parse_args()

    if not os.path.exists(args.save_dir) and args.local_rank in [-1, 0]:
        os.makedirs(args.save_dir)
    time_ = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    fileHandler = logging.FileHandler(os.path.join(args.save_dir, '{}.log'.format(time_)))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    # args display
    if args.local_rank in [-1, 0]:
        for k, v in vars(args).items():
            logging.info(k+':'+str(v))

    seed_everything(args.seed)

    # distributed data parallel   
    args.n_gpus = torch.cuda.device_count()
    if args.n_gpus > 1:
        os.environ['MASTER_ADDR'] = 'localhost'
        os.environ['MASTER_PORT'] = str(args.port)
        dist.init_process_group(backend='nccl', world_size=args.n_gpus)
        torch.cuda.set_device(args.local_rank)

    train(args)
    
    if args.n_gpus > 1:
        dist.destroy_process_group()

if __name__ == '__main__':
    main()
