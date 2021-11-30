"""
We need the last function to help extract the final answer of SPARQL, used in check_sparql
"""

import os
import json
import pickle
import argparse
import numpy as np
from nltk import word_tokenize
from collections import Counter
from itertools import chain
from tqdm import tqdm
import re
import random

from utils.misc import init_vocab
from transformers import *

overnight_domains = ['basketball', 'blocks', 'calendar', 'housing', 'publications', 'recipes', 'restaurants', 'socialnetwork']

def read_data(path, domain_idx):
    ex_list = []
    with open(path, 'r') as infile:
        lines = [line.strip() for line in infile]
        for i in range(len(lines))[::8]:
            ex = {}
            ex['q'] = re.findall(r'''\"(.*?)\"''',lines[i+1])[0]
            ex['tir'] = re.findall(r'''\"(.*?)\"''',lines[i+2])[0]
            ex['domain'] = domain_idx
            ex_list.append(ex)
    return ex_list

def encode_dataset(dataset, vocab, tokenizer):
    queries = []
    irs = []
    domain_idx = []
    
    for item in tqdm(dataset):
        queries.append(item['q'])
        irs.append(item['tir'])
        domain_idx.append(item['domain'])
            
    sequences = queries + irs
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(queries, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    target_ids = tokenizer.batch_encode_plus(irs, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    target_ids = np.array(target_ids['input_ids'], dtype = np.int32)
    
    choices = np.array([0]*len(queries), dtype = np.int32)
    answers = np.array(domain_idx, dtype = np.int32)
    
    return source_ids, source_mask, target_ids, choices, answers



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--model_name_or_path', required=True)
    parser.add_argument('--domain', choices=overnight_domains, default='all')
    args = parser.parse_args()

    args.domain = overnight_domains if args.domain == 'all' else [args.domain]
    set_seed(666)

    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }
    print('Load queries')

    train_set, val_set, test_set = [], [], []
    for domain in args.domain:
        idx = overnight_domains.index(domain)
        train_data = read_data(os.path.join(args.input_dir, domain + '.paraphrases.train.examples'), idx)
        random.shuffle(train_data)
        train_set += train_data[:int(len(train_data) * 0.8)]
        val_set += train_data[int(len(train_data) * 0.8):]
        test_set += read_data(os.path.join(args.input_dir, domain + '.paraphrases.test.examples'), idx)
    
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)

    fn = os.path.join(args.output_dir, 'vocab.json')
    print('Dump vocab to {}'.format(fn))

    with open(fn, 'w') as f:
        json.dump(vocab, f, indent=2)

    tokenizer = BartTokenizer.from_pretrained(args.model_name_or_path)
    
    for name, dataset in zip(('train', 'val', 'test'), (train_set, val_set, test_set)):
        outputs = encode_dataset(dataset, vocab, tokenizer)
        assert len(outputs) == 5
        with open(os.path.join(args.output_dir, '{}.pt'.format(name)), 'wb') as f:
            for o in outputs:
                pickle.dump(o, f)

if __name__ == '__main__':
    main()