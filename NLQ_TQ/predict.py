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

from Bart_Program.data import DataLoader
from transformers import BartConfig, BartForConditionalGeneration, BartTokenizer
import torch.optim as optim
import logging
import time
from utils.lr_scheduler import get_linear_schedule_with_warmup

import torch.nn.functional as F
from NLQ_TQ.train import cal_performance
from nltk.translate.bleu_score import sentence_bleu

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query


def predict(args, model, data, device, tokenizer):
    model.eval()
    
    with torch.no_grad():
        all_outputs = []
        all_targets = []
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, choices, target_ids, answer = [x.to(device) for x in batch]
            outputs = model.generate(
                input_ids=source_ids,
                max_length = 500,
            )
            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            
        assert len(all_outputs) == len(all_targets) 
        all_bleu, all_correct = cal_performance(all_outputs, all_targets, tokenizer)
        acc = all_correct/len(all_outputs)
        avg_bleu = all_bleu/len(all_outputs)
        print("Avg Accuracy: %f\nAvg BLEU: %f\n" % (acc, avg_bleu))
            
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for output_id in all_outputs]
        targets = [tokenizer.decode(target_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for target_id in all_targets]
        
        with open(os.path.join(args.save_dir, 'predict.txt'), 'w') as f:
            for output in tqdm(outputs):
                f.write(output + '\n')
        with open(os.path.join(args.save_dir, 'gold.txt'), 'w') as f:
            for target in tqdm(targets):
                    f.write(target + '\n')

def train(args):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    logging.info("Create train_loader and val_loader.........")
    vocab_json = os.path.join(args.input_dir, 'vocab.json')
    train_pt = os.path.join(args.input_dir, 'train.pt')
    val_pt = os.path.join(args.input_dir, 'test_ans.pt')
    train_loader = DataLoader(vocab_json, train_pt, args.batch_size, training=True)
    val_loader = DataLoader(vocab_json, val_pt, args.batch_size)
    vocab = train_loader.vocab

    logging.info("Create model.........")
    config_class, model_class, tokenizer_class = (BartConfig, BartForConditionalGeneration, BartTokenizer)
    tokenizer = tokenizer_class.from_pretrained(args.ckpt)
    model = model_class.from_pretrained(args.ckpt)
    model = model.to(device)
    # logging.info(model)

    # validate(args, model, val_loader, device, tokenizer)
    predict(args, model, val_loader, device, tokenizer)

    # vis(args, model, val_loader, device, tokenizer)
def main():
    parser = argparse.ArgumentParser()
    # input and output
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--save_dir', required=True, help='path to save checkpoints and logs')
    parser.add_argument('--model_name_or_path', required = True)
    parser.add_argument('--ckpt', required=True)

    # training parameters
    parser.add_argument('--batch_size', default=256, type=int)
    parser.add_argument('--seed', type=int, default=666, help='random seed')
    
    # validating parameters
    # parser.add_argument('--num_return_sequences', default=1, type=int)
    # parser.add_argument('--top_p', default=)
    # model hyperparameters
    parser.add_argument('--dim_hidden', default=1024, type=int)
    parser.add_argument('--alpha', default = 1e-4, type = float)
    args = parser.parse_args()

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)
    time_ = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    fileHandler = logging.FileHandler(os.path.join(args.save_dir, '{}.predict.log'.format(time_)))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    # args display
    for k, v in vars(args).items():
        logging.info(k+':'+str(v))

    seed_everything(666)

    train(args)


if __name__ == '__main__':
    main()

