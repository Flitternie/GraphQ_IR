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


def string_match_performance(pred, gold):
    return np.mean([sentence_bleu([g], p) for g, p in zip(pred, gold)]), np.mean([1 if p.strip() == g.strip() else 0 for p, g in zip(pred, gold)])
    
def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    all_outputs = []
    all_targets = []
    with torch.no_grad():
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, choices, target_ids, answer = [x.to(device) for x in batch]
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
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for output_id in all_outputs]
        targets = [tokenizer.decode(target_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for target_id in all_targets]

    acc, bleu = string_match_performance(outputs, targets)
    logging.info('accuracy: {}, bleu: {}'.format(acc, bleu))
    
    return acc, outputs

    
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

