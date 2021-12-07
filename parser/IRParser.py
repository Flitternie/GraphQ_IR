import sys
import json
from itertools import chain
from tqdm import tqdm

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from ir.UnifiedIRLexer import UnifiedIRLexer
from ir.UnifiedIRParser import UnifiedIRParser
from program_v2 import ProgramIRTranslator

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

def get_program_seq(program):
    seq = []
    for item in program:
        func = item['function']
        inputs = item['inputs']
        seq.append(func + '(' + '<c>'.join(inputs) + ')')
    seq = '<b>'.join(seq)
    return seq

if __name__ == '__main__':
    translator =  ProgramIRTranslator.IR_translator()

    train_data = json.load(open("./dataset_new/train.json"))
    train_program = [item['program'] for item in train_data]
    val_data = json.load(open("./dataset_new/val.json"))
    val_program = [item['program'] for item in val_data]
    test_data = json.load(open("./dataset_new/test.json"))
    test_program = [item['program'] for item in test_data]
    
    count = 0
    err_file = open("./err_programs.txt", "w+")
    for program in train_program[:10]:
    # for program in tqdm(chain(train_program,val_program,test_program)):
        ir = translator.program_to_ir(program)
        print(ir)
        print(get_program_seq(program))
        input_stream = InputStream(ir)
        lexer = UnifiedIRLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = UnifiedIRParser(token_stream)
        
        try:
            tree = parser.query()
            # lisp_tree_str = tree.toStringTree(recog=parser)
            # print(lisp_tree_str)
        except Exception:
            count += 1
            err_file.write(program.strip()+"\n")
            # raise Exception
    err_file.close()

    print('error count: %d' % count)
    
