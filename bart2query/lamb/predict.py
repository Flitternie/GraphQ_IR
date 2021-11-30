import os
import torch
import numpy as np
from tqdm import tqdm
from utils.data import DataLoader
from transformers import BartConfig, BartForConditionalGeneration, BartTokenizer
import logging

from data.overnight.domain.domain_base import Domain

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query

overnight_domains = ['basketball', 'blocks', 'calendar', 'housing', 'publications', 'recipes', 'restaurants', 'socialnetwork']

def cal_performance(pred, gold, domains):
    assert len(pred) == len(gold)
    data = [[[],[]] for _ in range(len(domains))]
    scores = []
    evaluators = [Domain.from_dataset(domain) for domain in overnight_domains]
    for p, g, d in zip(pred, gold, domains):
        data[d][0].append(p)
        data[d][1].append(g)
    for i, evaluator in enumerate(evaluators):
        domain_score = evaluator.compare_logical_form(data[i][0], data[i][1])
        scores += domain_score
        logging.info("{}-domain accuracy: {}".format(overnight_domains[i], np.mean(domain_score)))
    return np.mean(scores), np.mean([1 if p.strip() == g.strip() else 0 for p, g in zip(pred, gold)])


def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    all_outputs = []
    all_targets = []
    all_domains = []
    with torch.no_grad():
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, _, target_ids, domains = [x.to(device) for x in batch]
            outputs = model.module.generate(
                input_ids=source_ids,
                max_length = 500,
            ) if hasattr(model, "module") else model.generate(
                input_ids=source_ids,
                max_length = 500,
            ) 

            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            all_domains.extend(domains.cpu().numpy())
            
        assert len(all_outputs) == len(all_targets) 
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for output_id in all_outputs]
        targets = [tokenizer.decode(target_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for target_id in all_targets]

        with open("./%s_results.txt"%args.mode, "w+") as f:
            for output in outputs:
                f.write(output.strip() + "\n")
                
        with open("./%s_golds.txt"%args.mode, "w+") as f:
            for output in targets:
                f.write(output.strip() + "\n")

        lf_matching, str_matching = cal_performance(outputs, targets, all_domains)
        logging.info('Logical form matching accuracy: {}, String matching accuracy: {}'.format(lf_matching, str_matching))

    return lf_matching, outputs


def predict(args, kb, model, data, device, tokenizer):
    all_outputs = []
    all_targets = []
    all_domains = []
    with torch.no_grad():
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, _, target_ids, domains = [x.to(device) for x in batch]
            outputs = model.module.generate(
                input_ids=source_ids,
                max_length = 500,
            ) if hasattr(model, "module") else model.generate(
                input_ids=source_ids,
                max_length = 500,
            ) 

            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            all_domains.extend(domains.cpu().numpy())
            
        assert len(all_outputs) == len(all_targets) 
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for output_id in all_outputs]
        targets = [tokenizer.decode(target_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for target_id in all_targets]
        
        lf_matching, str_matching = cal_performance(outputs, targets, all_domains)
        logging.info('Logical form matching accuracy: {}, String matching accuracy: {}'.format(lf_matching, str_matching))

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

