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

from utils.misc import init_vocab
from transformers import *
from IR_CFQ.sparql_parser import KqaParser

def encode_dataset(dataset, parser, vocab, tokenizer, ir_mode, test = False):
    questions = []
    sparqls = []
    choices = []
    answers = []
    for item in tqdm(dataset):
        question = item['rewrite'] if 'rewrite' in item.keys() else item['question']
        questions.append(question)
        _ = [vocab['answer_token_to_idx'][w] for w in item['choices']]
        choices.append(_)
        if not test:
            sparql = parser.f_reversible(item['sparql']) if ir_mode == 'rir' else parser.f_lossy(item['sparql'])
            sparqls.append(sparql)
            answers.append(vocab['answer_token_to_idx'].get(item['answer']))
    
    sequences = questions + sparqls
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(questions, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    if not test:
        target_ids = tokenizer.batch_encode_plus(sparqls, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
        target_ids = np.array(target_ids['input_ids'], dtype = np.int32)
    else:
        target_ids = np.array([], dtype = np.int32)
    choices = np.array(choices, dtype = np.int32)
    answers = np.array(answers, dtype = np.int32)
    return source_ids, source_mask, target_ids, choices, answers



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--ir_mode', choices=['rir', 'lir'], required=True)
    parser.add_argument('--model_name_or_path', required=True)
    args = parser.parse_args()

    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }
    print('Load questions')
    train_set = json.load(open(os.path.join(args.input_dir, 'train.json')))
    val_set = json.load(open(os.path.join(args.input_dir, 'val.json')))
    test_set = json.load(open(os.path.join(args.input_dir, 'test.json')))

    all_sparqls = []
    for question in chain(train_set, val_set, test_set):
        for a in question['choices']:
            if not a in vocab['answer_token_to_idx']:
                vocab['answer_token_to_idx'][a] = len(vocab['answer_token_to_idx'])
        all_sparqls.append(question['sparql'])

    parser = KqaParser(all_sparqls)
    if not os.path.isdir(args.output_dir):
        os.mkdir(args.output_dir)
    fn = os.path.join(args.output_dir, 'parser.pkl')
    print('Dump parser to {}'.format(fn))
    with open(fn, 'wb') as f:
        pickle.dump(parser, f)

    fn = os.path.join(args.output_dir, 'vocab.json')
    print('Dump vocab to {}'.format(fn))
    with open(fn, 'w') as f:
        json.dump(vocab, f, indent=2)
    for k in vocab:
        print('{}:{}'.format(k, len(vocab[k])))
    
    tokenizer = BartTokenizer.from_pretrained(args.model_name_or_path)
    
    for name, dataset in zip(('train', 'val', 'test_ans'), (train_set, val_set, test_set)):
        # print('Encode {} set'.format(name))
        outputs = encode_dataset(dataset, parser, vocab, tokenizer, args.ir_mode, name=='test')
        assert len(outputs) == 5
        # print('shape of input_ids of questions, attention_mask of questions, input_ids of sparqls, choices and answers:')
        with open(os.path.join(args.output_dir, '{}.pt'.format(name)), 'wb') as f:
            for o in outputs:
                # print(o.shape)
                pickle.dump(o, f)
if __name__ == '__main__':
    main()