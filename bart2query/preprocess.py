import os
import json
import pickle
import argparse
import numpy as np
from itertools import chain
from tqdm import tqdm
import re

from utils.misc import init_vocab
from transformers import *

def get_program_seq(program):
    seq = []
    for item in program:
        func = item['function']
        inputs = item['inputs']
        seq.append(func + '(' + '<c>'.join(inputs) + ')')
    seq = '<b>'.join(seq)
    return seq

def get_program_seq_ordered(program, idx=-1):
    func = program[idx]

    if len(func['dependencies']) == 0:
        seq = func['function'] + '(' + '<c>'.join(func['inputs']) + ')'

    elif len(func['dependencies']) == 1:
        child_idx = func['dependencies'][0]
        child_seq = get_program_seq_ordered(program, child_idx)
        current_seq = func['function'] + '(' + '<c>'.join(func['inputs']) + ')'
        seq = child_seq + '<b>' + current_seq

    elif len(func['dependencies']) == 2:
        left_idx = func['dependencies'][0]
        left_seq = get_program_seq_ordered(program, left_idx)
        right_idx = func['dependencies'][1]
        right_seq = get_program_seq_ordered(program, right_idx)

        current_seq = func['function'] + '(' + '<c>'.join(func['inputs']) + ')'

        if func['function'] in ['And', 'Or', 'SelectBetween'] and left_seq > right_seq:
            seq = right_seq + '<b>' + left_seq + '<b>' + current_seq
        else:
            seq = left_seq + '<b>' + right_seq + '<b>' + current_seq
    else:
        raise ValueError("Functions are not allowed to have more than 2 dependencies")

    return seq

def encode_dataset(mode, dataset, vocab, tokenizer, test = False):
    questions = []
    target_queries = []
    choices = []
    answers = []
    for item in tqdm(dataset):
        question = item['rewrite'] if 'rewrite' in item.keys() else item['question']
        questions.append(question)
        _ = [vocab['answer_token_to_idx'][w] for w in item['choices']]
        choices.append(_)
        if not test:
            if mode == 'program':
                target_query = get_program_seq_ordered(item['program'])  
            elif mode == 'sparql':
                target_query = item['sparql']
            target_queries.append(target_query)
            answers.append(vocab['answer_token_to_idx'].get(item['answer']))
    
    sequences = questions + target_queries
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(questions, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    if not test:
        target_ids = tokenizer.batch_encode_plus(target_queries, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
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
    parser.add_argument('--model_name_or_path', required=True)

    parser.add_argument('--mode', required=True, choices=["program", "sparql"])
    args = parser.parse_args()

    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }
    print('Load questions')
    train_set = json.load(open(os.path.join(args.input_dir, 'train.json')))
    val_set = json.load(open(os.path.join(args.input_dir, 'val.json')))
    test_set = json.load(open(os.path.join(args.input_dir, 'test.json')))
    for question in chain(train_set, val_set, test_set):
        for a in question['choices']:
            if not a in vocab['answer_token_to_idx']:
                vocab['answer_token_to_idx'][a] = len(vocab['answer_token_to_idx'])

    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir, exist_ok = True)
    fn = os.path.join(args.output_dir, 'vocab.json')
    print('Dump vocab to {}'.format(fn))
    with open(fn, 'w') as f:
        json.dump(vocab, f, indent=2)
    for k in vocab:
        print('{}:{}'.format(k, len(vocab[k])))

    tokenizer = BartTokenizer.from_pretrained(args.model_name_or_path)
    
    for name, dataset in zip(('train', 'val', 'test'), (train_set, val_set, test_set, test_set)):
        print('Encode {} set'.format(name))
        outputs = encode_dataset(args.mode, dataset, vocab, tokenizer)
        assert len(outputs) == 5
        with open(os.path.join(args.output_dir, '{}.pt'.format(name)), 'wb') as f:
            for o in outputs:
                pickle.dump(o, f)

if __name__ == '__main__':
    main()