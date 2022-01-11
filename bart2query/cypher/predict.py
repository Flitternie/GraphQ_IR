import os
import torch
import numpy as np
from tqdm import tqdm
from utils.data import DataLoader
from transformers import BartConfig, BartForConditionalGeneration, BartTokenizer
import logging

from nltk.translate.bleu_score import sentence_bleu

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query


def cal_performance(pred, gold, tokenizer):
    batch_bleu = 0.0
    batch_correct = 0
    for x, y in zip(pred, gold):
        y = tokenizer.decode(y, skip_special_tokens = True, clean_up_tokenization_spaces = True)
        x = tokenizer.decode(x, skip_special_tokens = True, clean_up_tokenization_spaces = True)
        batch_bleu += sentence_bleu([y], x)
        batch_correct += x==y
    return batch_bleu, batch_correct


def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    all_outputs = []
    all_targets = []
    
    with torch.no_grad():
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, _, target_ids, _ = [x.to(device) for x in batch]
            outputs = model.module.generate(
                input_ids=source_ids,
                max_length = 500,
            ) if hasattr(model, "module") else model.generate(
                input_ids=source_ids,
                max_length = 500,
            ) 

            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            
        assert len(all_outputs) == len(all_targets) 
        all_bleu, all_correct = cal_performance(all_outputs, all_targets, tokenizer)
        acc = all_correct/len(all_outputs)
        avg_bleu = all_bleu/len(all_outputs)
        logging.info('accuracy: {}, bleu: {}'.format(acc, avg_bleu))

        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for output_id in all_outputs]
        
    return acc, outputs


def predict(args, kb, model, data, device, tokenizer):
    all_outputs = []
    all_targets = []
    
    with torch.no_grad():
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, _, target_ids, _ = [x.to(device) for x in batch]
            outputs = model.module.generate(
                input_ids=source_ids,
                max_length = 500,
            ) if hasattr(model, "module") else model.generate(
                input_ids=source_ids,
                max_length = 500,
            ) 

            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            
        assert len(all_outputs) == len(all_targets) 
        all_bleu, all_correct = cal_performance(all_outputs, all_targets, tokenizer)
        acc = all_correct/len(all_outputs)
        avg_bleu = all_bleu/len(all_outputs)
        logging.info('accuracy: {}, bleu: {}'.format(acc, avg_bleu))

        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for output_id in all_outputs]
        
    with open(os.path.join(args.save_dir, 'predict.txt'), 'w') as f:
        for output in tqdm(outputs):
            f.write(output + '\n')
    
def prepare(dataset, args):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    print("Preparing %s data........." % dataset)
    vocab_json = os.path.join(args.input_dir, 'vocab.json')
    val_pt = os.path.join(args.input_dir, '%s.pt' % dataset)
    val_loader = DataLoader(vocab_json, val_pt, args.batch_size)
    
    config_class, model_class, tokenizer_class = (BartConfig, BartForConditionalGeneration, BartTokenizer)
    tokenizer = tokenizer_class.from_pretrained(args.model_name_or_path)
    model = model_class.from_pretrained(args.ckpt)
    model.resize_token_embeddings(len(tokenizer))
    model = model.to(device)
    
    _, outputs = validate(args, None, model, val_loader, device, tokenizer)

    return outputs

