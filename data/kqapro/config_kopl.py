import os
import re
import json
from itertools import chain
from tqdm import tqdm
import numpy as np

from data.kqapro.utils.executor_rule_new import RuleExecutor 

special_tokens = ['<c>', '<b>']
domains = []

def get_program_seq(program):
    seq = []
    for item in program:
        func = item['function']
        inputs = item['inputs']
        seq.append(func + '(' + '<c>'.join(inputs) + ')')
    seq = '<b>'.join(seq)
    return seq

def load_data(args):
    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }
    print('Load questions')
    train_set = json.load(open(os.path.join(args.input_dir, 'train.json')))
    val_set = json.load(open(os.path.join(args.input_dir, 'val.json')))
    test_set = json.load(open(os.path.join(args.input_dir, 'test.json')))
    for question in chain(train_set, val_set, test_set):
        for ans in question['choices']:
            if not ans in vocab['answer_token_to_idx']:
                vocab['answer_token_to_idx'][ans] = len(vocab['answer_token_to_idx'])
        question['input'] = question.pop('rewrite')
        question['target'] = get_program_seq(question.pop('program'))
    
    if args.ir_mode == 'graphq':
        from graphq_ir.kopl.translator import Translator
        translator = Translator()
        for question in chain(train_set, val_set, test_set):
            question['target'] = translator.to_ir(question['target'])
    elif args.ir_mode == 'canonical':
        for question in chain(train_set, val_set, test_set):
            question['target'] = question['origin']
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)
    return train_set, val_set, test_set, vocab

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

def sequence_to_program(input):
    chunks = input.split('<b>')
    func_list = []
    inputs_list = []
    pattern = re.compile(r'(.*?)\((.*?)\)')
    for chunk in chunks:
        res = pattern.findall(chunk)
        if len(res) == 0:
            continue
        res = res[0]
        func, inputs = res[0], res[1]
        if inputs == '':
            inputs = []
        else:
            inputs = inputs.split('<c>')
        
        func_list.append(func)
        inputs_list.append(inputs)
    return func_list, inputs_list

def translate(args, outputs):
    if args.mode == 'graphq':
        from graphq_ir.ir.translator import Translator
        translator = Translator()
        translated_outputs = []
        for output in outputs:
            try:
                translated_outputs.append(translator.to_program(output))
            except:
                translated_outputs.append("")
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)

    return translated_outputs

def evaluate(args, outputs, targets, all_answers, data):
    given_answer = [data.vocab['answer_idx_to_token'][a] for a in all_answers]

    if args.ir_mode:
        outputs = translate(args, outputs)
    
    executor = RuleExecutor(os.path.join(os.path.dirname(__file__), 'data/kb.json'))
    count, correct = 0, 0

    for a, output in tqdm(zip(given_answer, outputs)):
        func_list, inputs_list = sequence_to_program(output)
        ans = executor.forward(func_list, inputs_list, ignore_error = True)
        if ans == None:
            ans = 'no'
        if ans == a:
            correct += 1
        count += 1
    acc = correct / count
    return acc
