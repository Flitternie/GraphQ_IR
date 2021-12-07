import sys
import json
from itertools import chain
from tqdm import tqdm

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .program_v2.ProgramLexer import ProgramLexer
from .program_v2.ProgramParser import ProgramParser
from .program_v2.ProgramListener import ProgramListener

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ex = ParseCancellationException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        raise ex

def get_program_seq(program):
    seq = []
    for item in program:
        func = item['function']
        inputs = item['inputs']
        seq.append(func + '(' + '<c>'.join(inputs) + ')')
    seq = '<b>'.join(seq)
    return seq

class ParsingProgram():
    def __init__(self):
        self.walker = ParseTreeWalker() 
        self.err_count = 0

    def parse(self, program):
        program = get_program_seq(program)
        input_stream = InputStream(program)
        lexer = ProgramLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = ProgramParser(token_stream)
        
        try:
            tree = parser.query()
            lisp_tree_str = tree.toStringTree(recog=parser)
            # print(lisp_tree_str)
        except Exception:
            self.err_count += 1
        

if __name__ == '__main__':
    train_data = json.load(open("./full_dataset/train.json"))
    train_program = [get_program_seq(item['program']) for item in train_data]
    val_data = json.load(open("./full_dataset/val.json"))
    val_program = [get_program_seq(item['program']) for item in val_data]
    test_data = json.load(open("./full_dataset/test.json"))
    test_program = [get_program_seq(item['program']) for item in test_data]
    
    count = 0
    err_file = open("./err_programs.txt", "a+")
    for program in tqdm(chain(train_program,val_program,test_program)):
        input_stream = InputStream(program)
        
        lexer = ProgramLexer(input_stream)
        # lexer.removeErrorListeners()
        # lexer.addErrorListener(ThrowingErrorListener())
        
        token_stream = CommonTokenStream(lexer)
        
        parser = ProgramParser(token_stream)
        # lexer.removeErrorListeners()
        # lexer.addErrorListener(ThrowingErrorListener())
        
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
    
