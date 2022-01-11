from antlr4 import *
from antlr4.InputStream import InputStream

from .UnifiedIRLexer import UnifiedIRLexer
from .UnifiedIRParser import UnifiedIRParser
from .UnifiedIRParserListener import UnifiedIRParserListener
from .SparqlEmitter import SparqlEmitter
from .OvernightEmitter import OvernightEmitter, overnight_domains


class Translator():
    def __init__(self):
        self.sparql_emitter = SparqlEmitter()
        self.overnight_emitter = OvernightEmitter()
        self.walker = ParseTreeWalker() 
    
    def set_domain(self, domain_idx: int):
        assert domain_idx < len(overnight_domains)
        self.overnight_emitter.set_domain(overnight_domains[domain_idx])
    
    def parse(self, ir):
        input_stream = InputStream(ir)
        lexer = UnifiedIRLexer(input_stream)       
        token_stream = CommonTokenStream(lexer)
        parser = UnifiedIRParser(token_stream)

        return parser.root()

    def to_sparql(self, ir):
        tree = self.parse(ir)
        self.walker.walk(self.sparql_emitter, tree)
        logical_form = self.sparql_emitter.get_logical_form(tree)
        
        return logical_form
    
    def to_overnight(self, ir):
        tree = self.parse(ir)
        self.walker.walk(self.overnight_emitter, tree)
        logical_form = self.overnight_emitter.get_logical_form(tree)
        
        return logical_form

if __name__ == '__main__':
    translator = Translator()
    ir = ''''''
    logical_form = translator.to_sparql(ir)
    print(logical_form)
    
    