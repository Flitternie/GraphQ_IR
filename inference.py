import os
import sys
import time
import logging
import argparse
import importlib

import torch
import numpy as np
from tqdm import tqdm
from transformers import AutoConfig, BartForConditionalGeneration, AutoTokenizer, set_seed

from utils.data import DataLoader

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query

def validate(args, model, data, device, tokenizer):
    try:
        spec = importlib.util.spec_from_file_location("config", args.config)
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
    except:
        raise Exception('Error loading config file')
        
    model.eval()
    model = model.module if hasattr(model, "module") else model
    
    with torch.no_grad():
        all_outputs = []
        all_targets = []
        all_answers = []
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, _, target_ids, answers = [x.to(device) for x in batch]
            outputs = model.generate(
                input_ids=source_ids,
                max_length = 512,
            )
            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            all_answers.extend(answers.cpu().numpy())
            
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces=False) for output_id in all_outputs]
        targets = [tokenizer.decode(target_id, skip_special_tokens = True, clean_up_tokenization_spaces=False) for target_id in all_targets]

    with open("./test.txt", "w") as f:
        for output, target in zip(outputs, targets):
            f.write("{}\t{}\n".format(output, target))

    str_matching = np.mean([1 if p.strip() == g.strip() else 0 for p, g in zip(outputs, targets)])
    lf_matching = config.evaluate(args, outputs, targets, all_answers, data)
    logging.info('Execution accuracy: {}, String matching accuracy: {}'.format(lf_matching, str_matching))
    
    return lf_matching, outputs

def inference(args):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    logging.info("Create train_loader and test_loader.........")
    vocab_json = os.path.join(args.input_dir, 'vocab.json')
    test_pt = os.path.join(args.input_dir, 'test.pt')
    test_loader = DataLoader(vocab_json, test_pt, args.batch_size)
    
    logging.info("Create model.........")
    _, model_class, tokenizer_class = (AutoConfig, BartForConditionalGeneration, AutoTokenizer)
    tokenizer = tokenizer_class.from_pretrained(args.model_name_or_path)
    model = model_class.from_pretrained(args.ckpt)
    model.resize_token_embeddings(len(tokenizer))
    model = model.to(device)

    _, outputs = validate(args, model, test_loader, device, tokenizer)
    
    with open(os.path.join(args.output_dir, 'pred_queries.txt'), 'w') as f:
        for output in outputs:
            f.write('{}\n'.format(output))
            

def main():
    parser = argparse.ArgumentParser()
    # input and output
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True, help='path to save files')
    parser.add_argument('--config', required=True)
    parser.add_argument('--model_name_or_path', required = True)
    parser.add_argument('--ckpt', required=True)

    # training parameters
    parser.add_argument('--batch_size', default=256, type=int)
    parser.add_argument('--seed', type=int, default=42, help='random seed')

    parser.add_argument('--ir_mode', default=None, choices=['graphq', 'cfq'])
    parser.add_argument('--self_correct', action='store_false')

    # model hyperparameters
    parser.add_argument('--dim_hidden', default=1024, type=int)
    parser.add_argument('--alpha', default=1e-4, type = float)

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)
    time_ = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    fileHandler = logging.FileHandler(os.path.join(args.output_dir, '{}.predict.log'.format(time_)))
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)
    
    for k, v in vars(args).items():
        logging.info(k+':'+str(v))

    set_seed(args.seed)

    inference(args)


if __name__ == '__main__':
    main()

