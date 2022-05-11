from antlr4 import *
from antlr4.InputStream import InputStream

from .SparqlLexer import SparqlLexer
from .SparqlParser import SparqlParser
from .SparqlListener import SparqlListener
from .IREmitter import IREmitter


def get_program_seq(sparql):
    seq = []
    for item in sparql:
        func = item['function']
        inputs = item['inputs']
        seq.append(func + '(' + '<c>'.join(inputs) + ')')
    seq = '<b>'.join(seq)
    return seq

class Translator():
    def __init__(self):
        self.emitter = IREmitter()
        self.walker = ParseTreeWalker()

    def normalize(self, logical_form):
        return logical_form

    def parse(self, logical_form):
        logical_form = self.normalize(logical_form)
        input_stream = InputStream(logical_form)
        lexer = SparqlLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = SparqlParser(token_stream)

        return parser.query()

    def to_ir(self, logical_form):
        # logical_form = get_program_seq(logical_form)
        tree = self.parse(logical_form)
        self.walker.walk(self.emitter, tree)
        ir = self.emitter.get_ir(tree)
        return ir
