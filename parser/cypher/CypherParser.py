# Generated from ./parser/cypher/Cypher.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\60\n\4\3\5\3\5\3\5")
        buf.write("\3\5\5\5\66\n\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7J\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\n\6\nS\n\n\r\n\16\nT\3\n\2\2\13\2\4\6")
        buf.write("\b\n\f\16\20\22\2\3\5\2\3\3\f\17\23\24\2T\2\25\3\2\2\2")
        buf.write("\4\34\3\2\2\2\6/\3\2\2\2\b\61\3\2\2\2\n:\3\2\2\2\fI\3")
        buf.write("\2\2\2\16K\3\2\2\2\20O\3\2\2\2\22R\3\2\2\2\24\26\5\4\3")
        buf.write("\2\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2")
        buf.write("\2\2\30\31\3\2\2\2\31\32\7\22\2\2\32\33\5\20\t\2\33\3")
        buf.write("\3\2\2\2\34\35\7\20\2\2\35 \5\6\4\2\36\37\7\21\2\2\37")
        buf.write("!\5\f\7\2 \36\3\2\2\2 !\3\2\2\2!\5\3\2\2\2\"#\5\b\5\2")
        buf.write("#$\7\3\2\2$%\5\n\6\2%&\7\4\2\2&\'\5\b\5\2\'\60\3\2\2\2")
        buf.write("()\5\b\5\2)*\7\5\2\2*+\5\n\6\2+,\7\3\2\2,-\5\b\5\2-\60")
        buf.write("\3\2\2\2.\60\5\b\5\2/\"\3\2\2\2/(\3\2\2\2/.\3\2\2\2\60")
        buf.write("\7\3\2\2\2\61\65\7\6\2\2\62\63\5\20\t\2\63\64\7\7\2\2")
        buf.write("\64\66\3\2\2\2\65\62\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2")
        buf.write("\2\678\5\22\n\289\7\b\2\29\t\3\2\2\2:;\7\t\2\2;<\7\7\2")
        buf.write("\2<=\5\22\n\2=>\7\n\2\2>\13\3\2\2\2?@\5\16\b\2@A\7\13")
        buf.write("\2\2AB\7\25\2\2BC\5\22\n\2CD\7\25\2\2DJ\3\2\2\2EF\5\16")
        buf.write("\b\2FG\7\13\2\2GH\5\22\n\2HJ\3\2\2\2I?\3\2\2\2IE\3\2\2")
        buf.write("\2J\r\3\2\2\2KL\5\20\t\2LM\7\f\2\2MN\5\22\n\2N\17\3\2")
        buf.write("\2\2OP\5\22\n\2P\21\3\2\2\2QS\t\2\2\2RQ\3\2\2\2ST\3\2")
        buf.write("\2\2TR\3\2\2\2TU\3\2\2\2U\23\3\2\2\2\b\27 /\65IT")
        return buf.getvalue()


class CypherParser ( Parser ):

    grammarFileName = "Cypher.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'->'", "'<-'", "'('", "':'", "')'", 
                     "'['", "']'", "'='", "'.'", "','", "'_'", "' '", "'MATCH'", 
                     "'WHERE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Match", "Where", "Return", 
                      "INTEGER", "STRING_LITERAL", "SEP", "WS" ]

    RULE_root = 0
    RULE_query = 1
    RULE_triple = 2
    RULE_node = 3
    RULE_relationship = 4
    RULE_constraint = 5
    RULE_attribute = 6
    RULE_var = 7
    RULE_string = 8

    ruleNames =  [ "root", "query", "triple", "node", "relationship", "constraint", 
                   "attribute", "var", "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    Match=14
    Where=15
    Return=16
    INTEGER=17
    STRING_LITERAL=18
    SEP=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(CypherParser.Return, 0)

        def var(self):
            return self.getTypedRuleContext(CypherParser.VarContext,0)


        def query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CypherParser.QueryContext)
            else:
                return self.getTypedRuleContext(CypherParser.QueryContext,i)


        def getRuleIndex(self):
            return CypherParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = CypherParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.query()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CypherParser.Match):
                    break

            self.state = 23
            self.match(CypherParser.Return)
            self.state = 24
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Match(self):
            return self.getToken(CypherParser.Match, 0)

        def triple(self):
            return self.getTypedRuleContext(CypherParser.TripleContext,0)


        def Where(self):
            return self.getToken(CypherParser.Where, 0)

        def constraint(self):
            return self.getTypedRuleContext(CypherParser.ConstraintContext,0)


        def getRuleIndex(self):
            return CypherParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = CypherParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CypherParser.Match)
            self.state = 27
            self.triple()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CypherParser.Where:
                self.state = 28
                self.match(CypherParser.Where)
                self.state = 29
                self.constraint()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TripleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CypherParser.RULE_triple

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NodeTripleContext(TripleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CypherParser.TripleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def node(self):
            return self.getTypedRuleContext(CypherParser.NodeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeTriple" ):
                listener.enterNodeTriple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeTriple" ):
                listener.exitNodeTriple(self)


    class ForwardTripleContext(TripleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CypherParser.TripleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CypherParser.NodeContext)
            else:
                return self.getTypedRuleContext(CypherParser.NodeContext,i)

        def relationship(self):
            return self.getTypedRuleContext(CypherParser.RelationshipContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardTriple" ):
                listener.enterForwardTriple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardTriple" ):
                listener.exitForwardTriple(self)


    class BackwardTripleContext(TripleContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CypherParser.TripleContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CypherParser.NodeContext)
            else:
                return self.getTypedRuleContext(CypherParser.NodeContext,i)

        def relationship(self):
            return self.getTypedRuleContext(CypherParser.RelationshipContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackwardTriple" ):
                listener.enterBackwardTriple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackwardTriple" ):
                listener.exitBackwardTriple(self)



    def triple(self):

        localctx = CypherParser.TripleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_triple)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = CypherParser.ForwardTripleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.node()
                self.state = 33
                self.match(CypherParser.T__0)
                self.state = 34
                self.relationship()
                self.state = 35
                self.match(CypherParser.T__1)
                self.state = 36
                self.node()
                pass

            elif la_ == 2:
                localctx = CypherParser.BackwardTripleContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.node()
                self.state = 39
                self.match(CypherParser.T__2)
                self.state = 40
                self.relationship()
                self.state = 41
                self.match(CypherParser.T__0)
                self.state = 42
                self.node()
                pass

            elif la_ == 3:
                localctx = CypherParser.NodeTripleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.node()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(CypherParser.StringContext,0)


        def var(self):
            return self.getTypedRuleContext(CypherParser.VarContext,0)


        def getRuleIndex(self):
            return CypherParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)




    def node(self):

        localctx = CypherParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(CypherParser.T__3)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 48
                self.var()
                self.state = 49
                self.match(CypherParser.T__4)


            self.state = 53
            self.string()
            self.state = 54
            self.match(CypherParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationshipContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(CypherParser.StringContext,0)


        def getRuleIndex(self):
            return CypherParser.RULE_relationship

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationship" ):
                listener.enterRelationship(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationship" ):
                listener.exitRelationship(self)




    def relationship(self):

        localctx = CypherParser.RelationshipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_relationship)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(CypherParser.T__6)
            self.state = 57
            self.match(CypherParser.T__4)
            self.state = 58
            self.string()
            self.state = 59
            self.match(CypherParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(CypherParser.AttributeContext,0)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(CypherParser.SEP)
            else:
                return self.getToken(CypherParser.SEP, i)

        def string(self):
            return self.getTypedRuleContext(CypherParser.StringContext,0)


        def getRuleIndex(self):
            return CypherParser.RULE_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraint" ):
                listener.enterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraint" ):
                listener.exitConstraint(self)




    def constraint(self):

        localctx = CypherParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_constraint)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.attribute()
                self.state = 62
                self.match(CypherParser.T__8)
                self.state = 63
                self.match(CypherParser.SEP)
                self.state = 64
                self.string()
                self.state = 65
                self.match(CypherParser.SEP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.attribute()
                self.state = 68
                self.match(CypherParser.T__8)
                self.state = 69
                self.string()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(CypherParser.VarContext,0)


        def string(self):
            return self.getTypedRuleContext(CypherParser.StringContext,0)


        def getRuleIndex(self):
            return CypherParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = CypherParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.var()
            self.state = 74
            self.match(CypherParser.T__9)
            self.state = 75
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(CypherParser.StringContext,0)


        def getRuleIndex(self):
            return CypherParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = CypherParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(CypherParser.STRING_LITERAL)
            else:
                return self.getToken(CypherParser.STRING_LITERAL, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(CypherParser.INTEGER)
            else:
                return self.getToken(CypherParser.INTEGER, i)

        def getRuleIndex(self):
            return CypherParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = CypherParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 79
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CypherParser.T__0) | (1 << CypherParser.T__9) | (1 << CypherParser.T__10) | (1 << CypherParser.T__11) | (1 << CypherParser.T__12) | (1 << CypherParser.INTEGER) | (1 << CypherParser.STRING_LITERAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 82 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





