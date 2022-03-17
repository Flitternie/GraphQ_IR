import sys
import json
from itertools import chain
from tqdm import tqdm

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .program.ProgramLexer import ProgramLexer
from .program.ProgramParser import ProgramParser
from .program.ProgramListener import ProgramListener

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

class Parser():
    def __init__(self):
        self.walker = ParseTreeWalker() 
        self.errors = []

    def parse(self, input):
        program = get_program_seq(input)
        input_stream = InputStream(program)
        lexer = ProgramLexer(input_stream)       
        # lexer.removeErrorListeners()
        # lexer.addErrorListener(ThrowingErrorListener())
        token_stream = CommonTokenStream(lexer)
        parser = ProgramParser(token_stream)
        
        try:
            tree = parser.query()
            lisp_tree_str = tree.toStringTree(recog=parser)
        except Exception:
            self.errors.append(input)
            return None

        return lisp_tree_str        
    
