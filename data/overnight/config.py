import os
import random
from itertools import chain
import numpy as np
import pandas as pd
import logging

from data.overnight.evaluator.domain_base import Domain

special_tokens = []
overnight_domains = ['basketball', 'blocks', 'calendar', 'housing', 'publications', 'recipes', 'restaurants', 'socialnetwork']

def load_data(args):
    args.domain = overnight_domains if args.domain == 'all' else [args.domain]
    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }

    print('Load questions')
    train_set, val_set, test_set = [], [], []
    if args.cross_domain:
        for domain in list(filter(lambda x: x not in args.domain, overnight_domains)):
            idx = overnight_domains.index(domain)
            train_set += read_overnight(os.path.join(args.input_dir, domain + '_train.tsv'), idx)
        domain = args.domain[0]
        val_set += read_overnight(os.path.join(args.input_dir, domain + '_train.tsv'), overnight_domains.index(domain))
        test_set += read_overnight(os.path.join(args.input_dir, domain + '_test.tsv'), overnight_domains.index(domain))
    
    else:
        for domain in args.domain:
            idx = overnight_domains.index(domain)
            train_data = read_overnight(os.path.join(args.input_dir, domain + '_train.tsv'), idx)
            random.shuffle(train_data)
            train_set += train_data[:int(len(train_data)*0.8)]
            val_set += train_data[int(len(train_data)*0.8):]
            test_set += read_overnight(os.path.join(args.input_dir, domain + '_test.tsv'), idx)
    
    if args.ir_mode == 'graphq':
        from graphq_trans.overnight.translator import Translator
        translator = Translator()
        for question in chain(train_set, val_set, test_set):
            question['target'] = translator.to_ir(question['target'])
    elif args.ir_mode == 'canonical':
        for question in chain(train_set, val_set, test_set):
            question['target'] = question['canonical']
    elif args.ir_mode:
        raise NotImplementedError("%s not supported" % args.ir_mode)
        
    return train_set, val_set, test_set, vocab

def read_overnight(path, domain_idx):
    ex_list = []
    infile = pd.read_csv(path, sep='\t')
    for idx, row in infile.iterrows():
        ex_list.append({'input': row['utterance'].strip(), 'target': row['logical_form'].strip(), 'canonical': row['original'].strip(), 'domain': domain_idx})
    return ex_list

def evaluate(args, outputs, targets, all_domains, *xargs):
    assert len(outputs) == len(targets)
    if args.ir_mode:
        outputs, targets = translate(args, outputs, targets, all_domains)
    data = [[[],[]] for _ in range(len(all_domains))]
    evaluators = [Domain.from_dataset(domain) for domain in overnight_domains]
    for p, g, d in zip(outputs, targets, all_domains):
        data[d][0].append(p)
        data[d][1].append(g)
    scores = []
    for i, evaluator in enumerate(evaluators):
        domain_score = evaluator.compare_logical_form(data[i][0], data[i][1])
        scores += domain_score
        logging.info("{}-domain accuracy: {}".format(overnight_domains[i], np.mean(domain_score)))
    return np.mean(scores)


def translate(args, outputs, targets, domains):
    if args.ir_mode == 'graphq':
        translated_outputs = []
        translated_targets = []
        from graphq_trans.ir.translator import Translator
        translator = Translator()
        for output, target, domain_idx in zip(outputs, targets, domains):
            translator.set_domain(domain_idx)
            try:
                translated_outputs.append(translator.to_overnight(output))
            except:
                translated_outputs.append("")
            translated_targets.append(translator.to_overnight(target))
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)
    return translated_outputs, translated_targets
