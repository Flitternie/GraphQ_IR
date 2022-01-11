from os import set_inheritable
import os
import sys
import json
from itertools import chain
from tqdm import tqdm
import argparse
import time

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

try:
    from .OvernightLexer import OvernightLexer
    from .OvernightParser import OvernightParser
    from .OvernightListener import OvernightListener
    from .OvernightIREmitter import IREmitter
except:
    from OvernightLexer import OvernightLexer
    from OvernightParser import OvernightParser
    from OvernightListener import OvernightListener
    from OvernightIREmitter import IREmitter

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException



class IR_translator():
    def __init__(self):
        self.listener = IREmitter()
        self.walker = ParseTreeWalker() 

    def lambda_to_ir(self, item):
        input_stream = InputStream(item)
        lexer = OvernightLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = OvernightParser(token_stream)
        
        tree = parser.root()
        self.walker.walk(self.listener, tree)
        ir = self.listener.getIR(tree)

        return ir

if __name__ == '__main__':
    translator = IR_translator()
    ir = '''( call SW.listValue ( call SW.concat ( date 2015 1 2 ) ( date 2015 1 3 ) ) )'''
    ir = translator.lambda_to_ir(ir)
    print(ir)
    
    