import os
import json
import pandas
import pickle
import argparse
import numpy as np
from tqdm import tqdm
import random
from utils import *
from transformers import *

def read_data(path):
    dataset = []
    with open(path, 'r') as f:
        df = pandas.read_csv(f)
        for _, line in df.iterrows():
            dataset.append({"q": line["query"].strip(), "lf": line["cypher"].strip()})
    return dataset

def encode_dataset(dataset, vocab, tokenizer):
    queries = []
    lfs = []
    
    for item in tqdm(dataset):
        queries.append(item['q'])
        lfs.append(item['lf'])
            
    sequences = queries + lfs
    encoded_inputs = tokenizer(sequences, padding = True)
    
    max_seq_length = len(encoded_inputs['input_ids'][0])
    assert max_seq_length == len(encoded_inputs['input_ids'][-1])

    input_ids = tokenizer.batch_encode_plus(queries, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    source_ids = np.array(input_ids['input_ids'], dtype = np.int32)
    source_mask = np.array(input_ids['attention_mask'], dtype = np.int32)
    target_ids = tokenizer.batch_encode_plus(lfs, max_length = max_seq_length, pad_to_max_length = True, truncation = True)
    target_ids = np.array(target_ids['input_ids'], dtype = np.int32)
    
    choices = np.array([0]*len(queries), dtype = np.int32)
    answers = np.array([0]*len(queries), dtype = np.int32)
    
    return source_ids, source_mask, target_ids, choices, answers



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    parser.add_argument('--model_name_or_path', required=True)
    args = parser.parse_args()

    set_seed(666)

    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }
    print('Load queries')

    train_set, val_set, test_set = [], [], []
    data = read_data(args.input_dir)
    random.shuffle(data)
    train_set = data[:int(len(data)*0.2)]
    val_set = data[int(len(data)*0.2):int(len(data)*0.6)]
    test_set = data[int(len(data)*0.6):]
    
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