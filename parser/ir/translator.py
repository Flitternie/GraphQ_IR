from antlr4 import *
from antlr4.InputStream import InputStream

from .UnifiedIRLexer import UnifiedIRLexer
from .UnifiedIRParser import UnifiedIRParser
from .UnifiedIRParserListener import UnifiedIRParserListener
from .SparqlEmitter import SparqlEmitter
from .OvernightEmitter import OvernightEmitter, overnight_domains
from .KoplEmitter import KoplEmitter

def post_process_ir(ir):
    for token in ["<E>","</E>","<ES>","</ES>","<A>","</A>","<R>","</R>","<V>","</V>","<Q>","</Q>","<C>","</C>"]:
        ir = ir.replace(" {}".format(token), token)
        ir = ir.replace("{} ".format(token), token)
    return ir

class Translator():
    def __init__(self):
        self.sparql_emitter = SparqlEmitter()
        self.kopl_emitter = KoplEmitter()
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
        ir = post_process_ir(ir)
        tree = self.parse(ir)
        self.walker.walk(self.sparql_emitter, tree)
        logical_form = self.sparql_emitter.get_logical_form(tree)
        return logical_form
    
    def to_kopl(self, ir):
        ir = post_process_ir(ir)
        tree = self.parse(ir)
        self.walker.walk(self.kopl_emitter, tree)
        logical_form = self.kopl_emitter.get_logical_form(tree)
        return logical_form
    
    def to_overnight(self, ir, domain_idx=None):
        if domain_idx != None and self.overnight_emitter.domain != overnight_domains[domain_idx]:
            self.set_domain(domain_idx)
        tree = self.parse(ir)
        self.walker.walk(self.overnight_emitter, tree)
        logical_form = self.overnight_emitter.get_logical_form(tree)
        return logical_form
    
    def to_cypher(self, ir):
        raise NotImplementedError()

    