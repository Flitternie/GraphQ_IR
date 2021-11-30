from IPython import get_ipython

import re
import os
import sys
import json
import random
from importlib import reload

random.seed(666)


import builtins
from IPython.lib import deepreload
builtins.reload = deepreload.reload


# new data
train_data = json.load(open("./dataset_new/train.json"))
train_sparql = [item['sparql'] for item in train_data]
train_program = [item['program'] for item in train_data]

val_data = json.load(open("./dataset_new/val.json"))
val_sparql = [item['sparql'] for item in val_data]
val_program = [item['program'] for item in val_data]


import KqaPro_Parser.program_v2.ProgramIRTranslator
reload(KqaPro_Parser.program_v2.ProgramIRTranslator)
from KqaPro_Parser.program_v2.ProgramIRTranslator import IR_translator
ir_translator = IR_translator()

def gen_ir(i):
    ir = ir_translator.program_to_ir(i)
    for token in ["<E>","</E>","<ES>","</ES>","<A>","</A>","<R>","</R>","<V>","</V>","<Q>","</Q>","<C>","</C>"]:
        ir = ir.replace(" {}".format(token), token)
        ir = ir.replace("{} ".format(token), token)
    return ir

ir_list = []
for point in train_program:
    ir = gen_ir(point)
    ir_list.append(ir)
    
from utils.load_kb import DataForSPARQL
from utils.data import DataLoader

input_dir = "./exp_files_new/UIR/full/end2end/sparql/"
vocab_json = os.path.join(input_dir, 'vocab.json')
data = os.path.join(input_dir, 'train.pt')
data = DataLoader(vocab_json, data, 128)
kb = DataForSPARQL(os.path.join("./dataset_new/", 'kb.json'))

import KqaPro_Parser.ir.SparqlTranslator
from KqaPro_Parser.ir.SparqlTranslator import Sparql_translator
sparql_translator = Sparql_translator()

pred_list = [sparql_translator.ir_to_sparql(ir) for ir in ir_list]

from bart2query.sparql.predict import whether_equal, post_process
from tqdm import tqdm
from bart2query.sparql.sparql_engine import get_sparql_answer

count, correct = 0, 0
all_answers = []
for batch in tqdm(data, total=len(data)):
    source_ids, source_mask, choices, target_ids, answer = [x.to('cpu') for x in batch]
    all_answers.extend(answer.cpu().numpy())
    
given_answer = [data.vocab['answer_idx_to_token'][a] for a in all_answers]

assert len(pred_list) == len(given_answer)
len(pred_list), len(given_answer)

count, correct = 0, 0
wrong_list = []
for s, ir, d in tqdm(zip(pred_list, ir_list, train_data)):
    pred_answer = get_sparql_answer(s, kb)
    gold_answer = get_sparql_answer(d["sparql"], kb)

    is_match = whether_equal(gold_answer, pred_answer)
    if is_match:
        correct += 1
    else:
        wrong_list.append([d["sparql"], s, ir, d["origin"], d["program"]])

    count += 1

acc = correct / count
print('acc: {}'.format(acc))

count, correct 

with open("./sparql_wrong_list.txt", "w+") as f: 
    for i in wrong_list:
        f.write(i[0]+"\n")
        f.write(i[1]+"\n")
        f.write(i[2]+"\n")
        f.write(i[3]+"\n")
        f.write('\n')

for a, s in tqdm(zip(given_answer, pred_list)):
    pred_answer = get_sparql_answer(s, kb)
    
    is_match = whether_equal(a, pred_answer)
    if is_match:
        correct += 1

    count += 1

acc = correct / count
print('acc: {}'.format(acc))


