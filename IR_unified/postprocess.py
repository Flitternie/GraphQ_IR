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

from bart2ir.predict import prepare
from IR_unified.self_correct import IRCorrector

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

def encode_dataset(dataset, vocab, tokenizer, args):
    irs = []
    targets = []
    choices = []
    answers = []

    if "new" in args.data_dir and "new" in args.input_dir:
        from KqaPro_Parser.program_v2 import ProgramIRTranslator 
    else:
        from KqaPro_Parser.program import ProgramIRTranslator 
    translator = ProgramIRTranslator.IR_translator()

    for item in tqdm(dataset):
        ir = translator.program_to_ir(item['program'])
        irs.append(ir)
        _ = [vocab['answer_token_to_idx'][w] for w in item['choices']]
        choices.append(_)
        
        if args.mode == "program":
            program = get_program_seq(item['program'])
            targets.append(program)
        elif args.mode == "sparql":
            targets.append(item['sparql'])
        answers.append(vocab['answer_token_to_idx'].get(item['answer']))
    
    sequences = irs + targets
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(irs, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    
    target_ids = tokenizer.batch_encode_plus(targets, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    target_ids = np.array(target_ids['input_ids'], dtype = np.int32)
    
    choices = np.array(choices, dtype = np.int32)
    answers = np.array(answers, dtype = np.int32)
    return source_ids, source_mask, target_ids, choices, answers


def encode_test_dataset(predicted_ir, dataset, vocab, tokenizer, args):
    assert len(predicted_ir) == len(dataset)

    irs = []
    targets = []
    choices = []
    answers = []

    for item in tqdm(dataset):
        irs = predicted_ir
        _ = [vocab['answer_token_to_idx'][w] for w in item['choices']]
        choices.append(_)
        
        if args.mode == "program":
            program = get_program_seq(item['program'])
            targets.append(program)
        elif args.mode == "sparql":
            targets.append(item['sparql'])
        answers.append(vocab['answer_token_to_idx'].get(item['answer']))
    
    sequences = irs + targets
    encoded_inputs = tokenizer(sequences, padding = True)
    max_seq_length = len(encoded_inputs['input_ids'][0])
    
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(irs, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)

    target_ids = tokenizer.batch_encode_plus(targets, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    target_ids = np.array(target_ids['input_ids'], dtype = np.int32)

    choices = np.array(choices, dtype = np.int32)
    answers = np.array(answers, dtype = np.int32)
    return source_ids, source_mask, target_ids, choices, answers



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--data_dir', required=True, help="path to dataset")
    parser.add_argument('--input_dir', required=True, help="path to processed NLQ2IR dataloaders")
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--model_name_or_path', required=True)
    parser.add_argument('--ckpt', required=True)

    parser.add_argument('--mode', required=True, choices=["program", "sparql"])
    parser.add_argument('--no_correct', action="store_true")

    # training parameters
    parser.add_argument('--batch_size', default=256, type=int)
    parser.add_argument('--seed', type=int, default=666, help='random seed')
    
    args = parser.parse_args()

    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }   

    train_set = json.load(open(os.path.join(args.data_dir, 'train.json')))
    val_set = json.load(open(os.path.join(args.data_dir, 'val.json')))
    test_set = json.load(open(os.path.join(args.data_dir, 'test.json')))
    for question in chain(train_set, val_set, test_set):
        for a in question['choices']:
            if not a in vocab['answer_token_to_idx']:
                vocab['answer_token_to_idx'][a] = len(vocab['answer_token_to_idx'])

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)
    
    fn = os.path.join(args.output_dir, 'vocab.json')
    print('Dump vocab to {}'.format(fn))
    
    with open(fn, 'w') as f:
        json.dump(vocab, f, indent=2)
    
    for k in vocab:
        print('{}:{}'.format(k, len(vocab[k])))
    
    tokenizer = BartTokenizer.from_pretrained(args.model_name_or_path)
    ir_corrector = IRCorrector()
 
    for name, dataset in zip(('train', 'val', 'test'), (train_set, val_set, test_set)):
        if 'test' in name or 'val' in name:
            ir = [line.strip() for line in prepare(name, args)]
            if not args.no_correct:
                ir = [ir_corrector.self_correct(line) for line in ir]
                print(ir_corrector.correct_num)
            outputs = encode_test_dataset(ir, dataset, vocab, tokenizer, args)
        else:
            outputs = encode_dataset(dataset, vocab, tokenizer, args)
            
        assert len(outputs) == 5
        
        with open(os.path.join(args.output_dir, '{}.pt'.format(name)), 'wb') as f:
            for o in outputs:
                pickle.dump(o, f)

if __name__ == '__main__':
    main()