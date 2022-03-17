import os
import json
import pickle
import argparse
import numpy as np
from tqdm import tqdm
import re
import regex
import random

from utils.misc import init_vocab
from transformers import *
from utils.data import load_kqapro, load_overnight, overnight_domains, load_metaqa

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

def reorder(sparql):
    subqueries = regex.search(r'''
    (?<rec> #capturing group rec
    \{ #open parenthesis
    (?: #non-capturing group
    [^{}]++ #anyting but parenthesis one or more times without backtracking
    | #or
    (?&rec) #recursive substitute of group rec
    )*
    \} #close parenthesis
    )
    ''', sparql ,flags=regex.VERBOSE).captures('rec')

    to_reorder = []

    for subquery in subqueries:
        subquery = subquery.strip()[1:-1]
        triples = re.sub(r"(\{.*\})", "", subquery).strip()
        triples = [i.strip() for i in triples.split(" .") if i]
        random.shuffle(triples)
        reordered_subquery = " . ".join(triples) + " . "
        to_reorder.append((subquery, reordered_subquery))

    for i in to_reorder:
        sparql = sparql.replace(i[0], i[1])
        
    return sparql

def encode_dataset(mode, dataset, vocab, tokenizer):
    questions = []
    target_queries = []
    choices = []
    answers = []
    
    for item in tqdm(dataset):
        question = item['rewrite'] if 'rewrite' in item.keys() else item['question']
        questions.append(question)
        
        if mode == 'program':
            target_query = get_program_seq(item['program'])  
        elif mode == 'sparql':
            target_query = item['sparql']
        elif mode == 'overnight':
            target_query = item['LF']
        elif mode == 'cypher':
            target_query = item['LF']
        target_queries.append(target_query)

        if mode == 'program' or mode == 'sparql':
            choices.append([vocab['answer_token_to_idx'][w] for w in item['choices']])
            answers.append(vocab['answer_token_to_idx'].get(item['answer']))
        elif mode == 'overnight':
            answers.append(item['domain'])
        # elif mode == 'cypher':
            # answers.append(vocab['answer_token_to_idx'].get(";".join(item['answer'])))

    sequences = questions + target_queries
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(questions, max_length = max_seq_length, padding='max_length', truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    
    target_ids = tokenizer.batch_encode_plus(target_queries, max_length = max_seq_length, padding='max_length', truncation = True)
    target_ids = np.array(target_ids['input_ids'], dtype = np.int32)
    
    choices = np.array(choices, dtype = np.int32) if choices else np.array([0]*len(questions), dtype = np.int32)
    answers = np.array(answers) if answers else np.array([0]*len(questions), dtype = np.int32)
    
    return source_ids, source_mask, target_ids, choices, answers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--model_name_or_path', required=True)

    parser.add_argument('--mode', required=True, choices=['program', 'sparql', 'overnight', 'cypher'])
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

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)

    fn = os.path.join(args.output_dir, 'vocab.json')
    print('Dump vocab to {}'.format(fn))

    with open(fn, 'w') as f:
        json.dump(vocab, f, indent=2)
    
    tokenizer = BartTokenizer.from_pretrained(args.model_name_or_path)
    
    for name, dataset in zip(('train', 'val', 'test'), (train_set, val_set, test_set)):
        print('Encode {} set'.format(name))
        outputs = encode_dataset(args.mode, dataset, vocab, tokenizer)
        assert len(outputs) == 5
        with open(os.path.join(args.output_dir, '{}.pt'.format(name)), 'wb') as f:
            for o in outputs:
                pickle.dump(o, f)

if __name__ == '__main__':
    main()