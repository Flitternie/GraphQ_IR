import sys
import json
from itertools import chain
from tqdm import tqdm

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .overnight.overnightLexer import overnightLexer
from .overnight.overnightParser import overnightParser

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class ParsingOvernight():
    def __init__(self):
        self.walker = ParseTreeWalker() 
        self.errors = []

    def parse(self, line):
        input_stream = InputStream(line)
        lexer = overnightLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = overnightParser(token_stream)
        
        try:
            tree = parser.root()
            # lisp_tree_str = tree.toStringTree(recog=parser)
            # print(lisp_tree_str)
        except Exception:
            self.errors.append(line)
        
