import sys
import json
from itertools import chain
from tqdm import tqdm

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .ir.UnifiedIRLexer import UnifiedIRLexer
from .ir.UnifiedIRParser import UnifiedIRParser

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ex = ParseCancellationException(f'line {line}: {column} {msg}')
        ex.line = line
        ex.column = column
        raise ex

class ParsingIR():
    def __init__(self):
        self.walker = ParseTreeWalker() 
        self.err_ir = []

    def parse(self, IR):
        input_stream = InputStream(IR)
        lexer = UnifiedIRLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = UnifiedIRParser(token_stream)
        
        try:
            tree = parser.query()
            # lisp_tree_str = tree.toStringTree(recog=parser)
            # print(lisp_tree_str)
        except Exception:
            self.err_ir.append(IR)
        
