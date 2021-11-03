import sys
import json
from itertools import chain
from tqdm import tqdm

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .ProgramLexer import ProgramLexer
from .ProgramParser import ProgramParser
from .ProgramListener import ProgramListener

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

if __name__ == '__main__':
    train_data = json.load(open("./dataset_new/train.json"))
    train_program = [get_program_seq(item['program']) for item in train_data]
    val_data = json.load(open("./dataset_new/val.json"))
    val_program = [get_program_seq(item['program']) for item in val_data]
    test_data = json.load(open("./dataset_new/test.json"))
    test_program = [get_program_seq(item['program']) for item in test_data]
    
    count = 0
    err_file = open("./err_programs.txt", "w+")
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
    
