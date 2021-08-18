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



def get_program_seq(program):
    seq = []
    for item in program:
        func = item['function']
        inputs = item['inputs']
        seq.append(func + '(' + '<c>'.join(inputs) + ')')
    seq = '<b>'.join(seq)

    return seq

def encode_dataset(dataset, vocab, tokenizer, pretrain=False):
    questions = []
    programs = []
    if not pretrain:
        choices = []
        answers = []

    for item in tqdm(dataset):
        question = item['origin'] if 'origin' in item.keys() else item['text']
        questions.append(question)
        if not pretrain:
            _ = [vocab['answer_token_to_idx'][w] for w in item['choices']]
            choices.append(_)
            answers.append(vocab['answer_token_to_idx'].get(item['answer']))
        program = item['program']
        program = get_program_seq(program)
        programs.append(program)
               
    sequences = questions + programs
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(questions, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    
    target_ids = tokenizer.batch_encode_plus(programs, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    target_ids = np.array(target_ids['input_ids'], dtype = np.int32)
    if not pretrain:
        choices = np.array(choices, dtype = np.int32)
        answers = np.array(answers, dtype = np.int32)
        return source_ids, source_mask, target_ids, choices, answers
    else:
        return source_ids, source_mask, target_ids
    
    


def del_repeat(pretrain_corpus, val_set, test_set):
    sparql_set = (item['sparql'] for item in chain(val_set, test_set))
    filtered_corpus = []
    filter_count = 0
    for item in tqdm(pretrain_corpus):
        if item['sparql'] not in sparql_set:
            filtered_corpus.append(item)
        else:
            filter_count += 1
    print("Filterd %d entries in pretrain corpus" % filter_count)
    return filtered_corpus

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--full_data_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--model_name_or_path', required=True)
    args = parser.parse_args()

    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }
    print('Load questions')
    pretrain_corpus = [json.loads(line) for line in open(os.path.join(args.full_data_dir, 'qa.json'))]
    val_set = json.load(open(os.path.join(args.input_dir, 'val.json')))
    test_set = json.load(open(os.path.join(args.input_dir, 'test.json')))

    print('Filtering pretrain corpus')
    pretrain_corpus = del_repeat(pretrain_corpus, val_set, test_set)

    for question in chain(pretrain_corpus, val_set, test_set):
        if 'choices' in question.keys():
            for a in question['choices']:
                if not a in vocab['answer_token_to_idx']:
                    vocab['answer_token_to_idx'][a] = len(vocab['answer_token_to_idx'])
        else:
            for a in question['answer']:
                if not a in vocab['answer_token_to_idx']:
                    vocab['answer_token_to_idx'][a] = len(vocab['answer_token_to_idx'])


    if not os.path.isdir(args.output_dir):
        os.mkdir(args.output_dir)
    fn = os.path.join(args.output_dir, 'vocab.json')
    print('Dump vocab to {}'.format(fn))
    with open(fn, 'w') as f:
        json.dump(vocab, f, indent=2)
    for k in vocab:
        print('{}:{}'.format(k, len(vocab[k])))
    
    tokenizer = BartTokenizer.from_pretrained(args.model_name_or_path)
    
    for name, dataset in zip(('val', 'test_ans'), (val_set, test_set)):
    # for name, dataset in zip(('train', 'val', 'test_ans'), (pretrain_corpus, val_set, test_set)):
        print('Encode {} set'.format(name))
        outputs = encode_dataset(dataset, vocab, tokenizer, name=='pretrain')
        if name=='pretrain':
            assert len(outputs) == 3
        else:
            assert len(outputs) == 5

        print('Save {} set'.format(name))
        with open(os.path.join(args.output_dir, '{}.pt'.format(name)), 'wb') as f:
            for o in outputs:
                pickle.dump(o, f)
                
if __name__ == '__main__':
    main()