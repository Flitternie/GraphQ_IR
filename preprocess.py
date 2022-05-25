import os
import json
import pickle
import argparse
import importlib
import numpy as np
from tqdm import tqdm

from transformers import BartTokenizer, set_seed

def encode_dataset(dataset, vocab, tokenizer):
    inputs = []
    targets = []
    choices = []
    answers = []
    
    for item in tqdm(dataset):
        inputs.append(item['input'])
        targets.append(item['target'])

        if vocab and 'choices' in item.keys() and 'answer' in item.keys():
            choices.append([vocab['answer_token_to_idx'][w] for w in item['choices']])
            answers.append(vocab['answer_token_to_idx'].get(item['answer']))
        elif 'domain' in item.keys():
            answers.append(item['domain'])
        
    sequences = inputs + targets
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(inputs, max_length = max_seq_length, padding='max_length', truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    
    target_ids = tokenizer.batch_encode_plus(targets, max_length = max_seq_length, padding='max_length', truncation = True)
    target_ids = np.array(target_ids['input_ids'], dtype = np.int32)
    
    choices = np.array(choices, dtype = np.int32) if choices else np.array([0]*len(inputs), dtype = np.int32)
    answers = np.array(answers) if answers else np.array([0]*len(inputs), dtype = np.int32)
    
    return source_ids, source_mask, target_ids, choices, answers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--config', required=True)
    parser.add_argument('--model_name_or_path', required=True)

    parser.add_argument('--seed', type=int, default=666)
    parser.add_argument('--ir_mode', default=None, choices=['graphq', 'cfq', 'canonical'])
    parser.add_argument('--domain', default='all')
    parser.add_argument('--cross_domain', action='store_true')
    parser.add_argument('--low_resource', default=100, type=int)
    
    args = parser.parse_args()

    set_seed(args.seed)

    try:
        spec = importlib.util.spec_from_file_location("config", args.config)
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
        train_set, val_set, test_set, vocab = config.load_data(args)
        task_special_tokens = config.special_tokens
    except:
        raise Exception('Error loading config file')
    
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir, exist_ok=True)

    fn = os.path.join(args.output_dir, 'vocab.json')
    with open(fn, 'w') as f:
        json.dump(vocab, f, indent=2)
    
    tokenizer = BartTokenizer.from_pretrained(args.model_name_or_path)
    tokenizer.add_tokens(task_special_tokens)
    print('Tokenizer loaded with domain specific special tokens added:')
    print(tokenizer.get_added_vocab())
    
    for name, dataset in zip(('train', 'val', 'test'), (train_set, val_set, test_set)):
        print('Encode {} set'.format(name))
        outputs = encode_dataset(dataset, vocab, tokenizer)
        assert len(outputs) == 5
        with open(os.path.join(args.output_dir, '{}.pt'.format(name)), 'wb') as f:
            for o in outputs:
                pickle.dump(o, f)

if __name__ == '__main__':
    main()