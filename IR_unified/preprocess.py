import os
import json
import pickle
import argparse
import numpy as np
from itertools import chain
from tqdm import tqdm
import random

from transformers import *
from utils.data import load_kqapro, load_overnight, overnight_domains, load_metaqa, load_mixed

def encode_dataset(mode, dataset, vocab, tokenizer):
    questions = []
    irs = []
    choices = []
    answers = []

    if mode == 'program' or mode == 'sparql':
        from parser.program.translator import Translator    
        translator = Translator()
    elif mode == 'overnight':
        from parser.overnight.translator import Translator
        translator = Translator()
    
    for item in tqdm(dataset):
        question = item['rewrite'] if 'rewrite' in item.keys() else item['question']
        questions.append(question)
        
        if mode == 'cypher' or mode == 'mixed':
            irs.append(item['ir'])
        else:
            logical_form = item['program'] if 'program' in item.keys() else item['LF']
            irs.append(translator.to_ir(logical_form))

        if mode == 'program' or mode == 'sparql':
            _ = [vocab['answer_token_to_idx'][w] for w in item['choices']]
            choices.append(_)
            answers.append(vocab['answer_token_to_idx'].get(item['answer']))
        elif mode == 'overnight':
            answers.append(item['domain'])
        # elif mode == 'cypher':
        #     answers.append(vocab['answer_token_to_idx'].get(";".join(item['answer'])))

    sequences = questions + irs
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])
    
    input_ids = tokenizer.batch_encode_plus(questions, max_length = max_seq_length, padding='max_length', truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    
    target_ids = tokenizer.batch_encode_plus(irs, max_length = max_seq_length, padding='max_length', truncation = True)
    target_ids = np.array(target_ids['input_ids'], dtype = np.int32)
    
    choices = np.array(choices, dtype = np.int32) if choices else np.array([0]*len(questions), dtype = np.int32)
    answers = np.array(answers) if answers else np.array([0]*len(questions), dtype = np.int32)

    return source_ids, source_mask, target_ids, choices, answers


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--model_name_or_path', required=True)    

    parser.add_argument('--mode', required=True, choices=['program', 'sparql', 'overnight', 'cypher', 'mixed'])
    parser.add_argument('--domain', choices=overnight_domains, default='all')
    parser.add_argument('--cross_domain', action='store_true')
    parser.add_argument('--low_resource', default=100, type=int)

    args = parser.parse_args() 

    args.domain = overnight_domains if args.domain == 'all' else [args.domain]
    set_seed(666)

    if args.mode == 'program' or args.mode == 'sparql':
        train_set, val_set, test_set, vocab = load_kqapro(args)
    elif args.mode == 'overnight':
        train_set, val_set, test_set, vocab = load_overnight(args)
    elif args.mode == 'cypher':
        train_set, val_set, test_set, vocab = load_metaqa(args)
    elif args.mode == 'mixed':
        train_set, val_set, vocab = load_mixed(args)


    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)

    fn = os.path.join(args.output_dir, 'vocab.json')
    print('Dump vocab to {}'.format(fn))

    with open(fn, 'w') as f:
        json.dump(vocab, f, indent=2)
        
    tokenizer = BartTokenizer.from_pretrained(args.model_name_or_path)
    
    if args.mode == 'mixed':
        name_list, data_list = ('train', 'val'), (train_set, val_set)
    else:
        name_list, data_list = ('train', 'val', 'test'), (train_set, val_set, test_set)

    for name, dataset in zip(name_list, data_list):
        print('Encode {} set'.format(name))
        outputs = encode_dataset(args.mode, dataset, vocab, tokenizer)
        assert len(outputs) == 5
        with open(os.path.join(args.output_dir, '{}.pt'.format(name)), 'wb') as f:
            for o in outputs:
                pickle.dump(o, f)

if __name__ == '__main__':
    main()

