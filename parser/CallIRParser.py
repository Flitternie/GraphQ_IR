import sys
import json
from itertools import chain
from tqdm import tqdm
from importlib import reload

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .ir.UnifiedIRLexer import UnifiedIRLexer
from .ir.UnifiedIRParser import UnifiedIRParser

class ParsingIR():
    def __init__(self):
        self.walker = ParseTreeWalker() 
        self.errors = []

    def parse(self, input):
        input_stream = InputStream(input)
        lexer = UnifiedIRLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = UnifiedIRParser(token_stream)
        
        try:
            tree = parser.query()
            lisp_tree_str = tree.toStringTree(recog=parser)
        except Exception:
            self.errors.append(input)
            return None
        
        return lisp_tree_str
        
