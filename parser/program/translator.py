from antlr4 import *
from antlr4.InputStream import InputStream

from .ProgramLexer import ProgramLexer
from .ProgramParser import ProgramParser
from .ProgramListener import ProgramListener
from .IREmitter import IREmitter


def get_program_seq(program):
    seq = []
    for item in program:
        func = item['function']
        inputs = item['inputs']
        seq.append(func + '(' + '<c>'.join(inputs) + ')')
    seq = '<b>'.join(seq)
    return seq

class Translator():
    def __init__(self):
        self.emitter = IREmitter()
        self.walker = ParseTreeWalker() 
    
    def parse(self, logical_form):
        input_stream = InputStream(logical_form)
        lexer = ProgramLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = ProgramParser(token_stream)
        
        return parser.root()

    def to_ir(self, logical_form):
        logical_form = get_program_seq(logical_form)
        tree = self.parse(logical_form)
        self.walker.walk(self.emitter, tree)
        ir = self.emitter.get_ir(tree)
        
        return ir

if __name__ == '__main__':
    translator = Translator()
    ir = ''''''
    ir = translator.to_ir(ir)
    print(ir)

    