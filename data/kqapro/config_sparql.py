import os
import re
import json
import pickle

import numpy as np
from itertools import chain
from tqdm import tqdm
from datetime import date

from data.kqapro.utils.load_kb import DataForSPARQL
from data.kqapro.utils.sparql_engine import get_sparql_answer

special_tokens = []
domains = []

def load_data(args):
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
        for ans in question['choices']:
            if not ans in vocab['answer_token_to_idx']:
                vocab['answer_token_to_idx'][ans] = len(vocab['answer_token_to_idx'])
        question['input'] = question.pop('rewrite')
        all_sparqls.append(question['sparql'])        
        question['target'] = question.pop('sparql')
    
    if args.ir_mode is None:
        return  train_set, val_set, test_set, vocab
    if args.ir_mode == 'graphq':
        from graphq_ir.sparql.translator import Translator
        translator = Translator()
        for question in chain(train_set, val_set, test_set):
            question['target'] = translator.to_ir(question['program'])
    elif args.ir_mode == 'cfq':
        from cfq_ir import KqaParser
        translator = KqaParser(all_sparqls)
        parser_path = os.path.join(args.output_dir, 'parser.pkl')
        print('Dump CFQ translator to {}'.format(parser_path))
        with open(parser_path, 'wb') as f:
            pickle.dump(translator, f)
        for question in chain(train_set, val_set, test_set):
            question['target'] = translator.f_reversible(question['target'])
    elif args.ir_mode == 'canonical':
        for question in chain(train_set, val_set, test_set):
            question['target'] = question['origin']
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)
        
    return train_set, val_set, test_set, vocab

def reorder(sparql):
    import random
    import regex

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

def whether_equal(answer, pred):
    """
    check whether the two arguments are equal as attribute value
    """
    def truncate_float(x):
        # convert answer from '100.0 meters' to '100 meters'
        try:
            v, *u = x.split()
            v = float(v)
            if v - int(v) < 1e-5:
                v = int(v)
            if len(u) == 0:
                x = str(v)
            else:
                x = '{} {}'.format(str(v), ' '.join(u))
        except:
            pass
        return x

    def equal_as_date(x, y):
        # check whether x and y are equal as type of date or year
        try:
            x_split = x.split('-')
            y_split = y.split('-')
            if len(x_split) == 3:
                x = date(int(x_split[0]), int(x_split[1]), int(x_split[2]))
            else:
                x = int(x)
            if len(y_split) == 3:
                y = date(int(y_split[0]), int(y_split[1]), int(y_split[2]))
            else:
                y = int(y)
            if isinstance(x, date) and isinstance(y, date):
                return x == y
            else:
                x = x.year if isinstance(x, date) else x
                y = y.year if isinstance(y, date) else y
                return x == y
        except:
            return False

    answer = truncate_float(answer)
    pred = truncate_float(pred)
    if equal_as_date(answer, pred):
        return True
    else:
        return answer == pred

def post_process(text):
    pattern = re.compile(r'".*?"')
    nes = []
    for item in pattern.finditer(text):
        nes.append((item.group(), item.span()))
    pos = [0]
    for name, span in nes:
        pos += [span[0], span[1]]
    pos.append(len(text))
    assert len(pos) % 2 == 0
    assert len(pos) / 2 == len(nes) + 1
    chunks = [text[pos[i]: pos[i+1]] for i in range(0, len(pos), 2)]
    for i in range(len(chunks)):
        chunks[i] = chunks[i].replace('?', ' ?').replace('.', ' .')
    bingo = ''
    for i in range(len(chunks) - 1):
        bingo += chunks[i] + nes[i][0]
    bingo += chunks[-1]
    return bingo

def evaluate(args, outputs, targets, all_answers, data):
    given_answer = [data.vocab['answer_idx_to_token'][a] for a in all_answers]

    if ( not args.ir_mode ) or args.ir_mode == 'cfq':
            outputs = [post_process(output) for output in outputs]
    if args.ir_mode:
        with open(os.path.join(args.output_dir, 'pred_ir.txt'), 'w') as f:
            for output in outputs:
                f.write('{}\n'.format(output))
        outputs = translate(args, outputs)    

    kb = DataForSPARQL(os.path.join(os.path.dirname(__file__), 'data/kb.json'))

    count, correct = 0, 0
    pred_answers = []
    for a, s in tqdm(zip(given_answer, outputs)):
        pred_answer = get_sparql_answer(s, kb)
        if pred_answer == None:
            pred_answer = 'no'
        is_match = whether_equal(a, pred_answer)
        if is_match:
            correct += 1
        count += 1
        pred_answers.append(pred_answer)

    with open(os.path.join(args.output_dir, 'pred_answers.txt'), 'w') as f:
        for a in pred_answers:
            f.write('{}\n'.format(a))

    return correct / count

def translate(args, outputs):
    if args.ir_mode == 'graphq':
        from graphq_ir.ir.translator import Translator    
        translator = Translator()
        if args.self_correct:
            from corrector import Corrector
            corrector = Corrector()
        translated_outputs = []
        for output in outputs:
            try:
                output = corrector.correct(output) if args.self_correct else output
                output = translator.to_sparql(output).replace('  ?', ' ?')
                translated_outputs.append(output)
            except Exception as e:
                translated_outputs.append("")
    elif args.ir_mode == 'cfq':
        try:
            with open(os.path.join(args.input_dir, 'parser.pkl'), 'rb') as f:
                parser = pickle.load(f)
        except:
            raise Exception('CFQ translator not found')
        translated_outputs = [parser.f_reversible_inverse(sparql).replace('  ?', ' ?') for sparql in outputs]
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)

    return translated_outputs