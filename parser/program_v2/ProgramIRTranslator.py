from os import set_inheritable
import os
import sys
import json
from itertools import chain
from tqdm import tqdm
import argparse

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .ProgramLexer import ProgramLexer
from .ProgramParser import ProgramParser
from .ProgramListener import ProgramListener
from .ProgramIREmitter import IREmitter

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

class IR_translator():
    def __init__(self):
        self.listener = IREmitter()
        self.walker = ParseTreeWalker() 

    def program_to_ir(self, program):
        program = get_program_seq(program)
        input_stream = InputStream(program)
        lexer = ProgramLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = ProgramParser(token_stream)
        
        tree = parser.query()
        self.walker.walk(self.listener, tree)
        ir = self.listener.getIR(tree)

        return ir

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    train_data = json.load(open(os.path.join(args.input_dir, 'train.json')))
    train_program = [item['program'] for item in train_data]
    val_data = json.load(open(os.path.join(args.input_dir, 'val.json')))
    val_program = [item['program'] for item in val_data]
    test_data = json.load(open(os.path.join(args.input_dir, 'test.json')))
    test_program = [item['program'] for item in test_data]
        
    translator = IR_translator()

    for name, program_file in zip(["train", "val", "test"], [train_program, val_program, test_program]):
        print("Processing {} set IRs".format(name))
        file = open(os.path.join(args.output_dir, "{}_IR.txt".format(name)), "w+")
        for program in tqdm(program_file):
            ir = translator.program_to_ir(program)
            file.write(ir + "\n")
        file.close()

    