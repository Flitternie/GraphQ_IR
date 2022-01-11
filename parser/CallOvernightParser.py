import sys
import json
from itertools import chain
from tqdm import tqdm

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .overnight.OvernightLexer import OvernightLexer
from .overnight.OvernightParser import OvernightParser

class ParsingOvernight():
    def __init__(self):
        self.walker = ParseTreeWalker() 
        self.errors = []

    def parse(self, input):
        input_stream = InputStream(input)
        lexer = OvernightLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = OvernightParser(token_stream)
        
        try:
            tree = parser.root()
            lisp_tree_str = tree.toStringTree(recog=parser)
        except Exception:
            self.errors.append(input)
            return None

        return lisp_tree_str
