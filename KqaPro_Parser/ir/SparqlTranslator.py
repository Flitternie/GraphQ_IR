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

from .UnifiedIRLexer import UnifiedIRLexer
from .UnifiedIRParser import UnifiedIRParser
from .UnifiedIRParserListener import UnifiedIRParserListener
from .SparqlEmitter import SparqlEmitter

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException



class Sparql_translator():
    def __init__(self):
        self.listener = SparqlEmitter()
        self.walker = ParseTreeWalker() 

    def ir_to_sparql(self, ir):
        input_stream = InputStream(ir)
        lexer = UnifiedIRLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = UnifiedIRParser(token_stream)
        
        tree = parser.query()
        self.walker.walk(self.listener, tree)
        # start = time.perf_counter()
        sparql = self.listener.getSPARQL(tree)
        # end = time.perf_counter()
        # print("Time: {}".format(end - start))

        return sparql

if __name__ == '__main__':
    translator = Sparql_translator()

    ir = '''what is<ES><E>entity1</E>that<R>relation1</R>backward to<E>entity2</E>(<Q>QUALIFIER</Q>is text<V>VALUE</V>)</ES>'''
    sparql = translator.ir_to_sparql(ir)
    print(sparql)
    
    