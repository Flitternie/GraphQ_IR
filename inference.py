import os
import torch
import argparse
import sys

from utils.misc import MetricLogger, seed_everything, ProgressBar
from utils.load_kb import DataForSPARQL
from utils.data import DataLoader

from transformers import BartConfig, BartForConditionalGeneration, BartTokenizer

import torch.optim as optim
import logging
import time
from utils.lr_scheduler import get_linear_schedule_with_warmup
import re

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query

def inference(args):
    if args.mode == 'program':
        from bart2query.program.predict import validate, predict
    elif args.mode == 'sparql':
        from bart2query.sparql.predict import validate, predict
    elif args.mode == 'lambda':
        from bart2query.overnight.predict import validate, predict
    elif args.mode == 'ir':
        from bart2ir.predict import validate, predict

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    logging.info("Create train_loader and val_loader.........")
    vocab_json = os.path.join(args.input_dir, 'vocab.json')
    val_pt = os.path.join(args.input_dir, 'test.pt')
    val_loader = DataLoader(vocab_json, val_pt, args.batch_size)
    kb = DataForSPARQL(os.path.join("./data/kqapro/dataset_new/", 'kb.json'))
    
    logging.info("Create model.........")
    config_class, model_class, tokenizer_class = (BartConfig, BartForConditionalGeneration, BartTokenizer)
    tokenizer = tokenizer_class.from_pretrained(args.model_name_or_path)
    model = model_class.from_pretrained(args.ckpt)
    model.resize_token_embeddings(len(tokenizer))
    model = model.to(device)
    
    if args.validate:
        _, outputs = validate(args, kb, model, val_loader, device, tokenizer)
        # with open("./%s_results.txt"%args.mode, "w+") as f:
        #     for output in outputs:
        #         f.write(output.strip() + "\n")
    else:
        predict(args, kb, model, val_loader, device, tokenizer)
    
def main():
    parser = argparse.ArgumentParser()
    # input and output
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--save_dir', required=True, help='path to save files')
    parser.add_argument('--model_name_or_path', required = True)
    parser.add_argument('--ckpt', required=True)

    # training parameters
    parser.add_argument('--batch_size', default=256, type=int)
    parser.add_argument('--seed', type=int, default=666, help='random seed')

    parser.add_argument('--mode', required=True, choices= ['program', 'sparql', 'lambda', 'ir'])
    parser.add_argument('--validate', default = True, type = bool)

    # validating parameters
    # parser.add_argument('--num_return_sequences', default=1, type=int)
    # parser.add_argument('--top_p', default=)

    # model hyperparameters
    parser.add_argument('--dim_hidden', default=1024, type=int)
    parser.add_argument('--alpha', default = 1e-4, type = float)

    args = parser.parse_args()

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir, exist_ok=True)
    time_ = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    fileHandler = logging.FileHandler(os.path.join(args.save_dir, '{}.predict.log'.format(time_)))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    
    for k, v in vars(args).items():
        logging.info(k+':'+str(v))

    seed_everything(args.seed)

    inference(args)


if __name__ == '__main__':
    main()

