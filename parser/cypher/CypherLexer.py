# Generated from ./parser/cypher/Cypher.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("\u0081\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21g\n\21\3\22\6\22j\n\22\r")
        buf.write("\22\16\22k\3\23\6\23o\n\23\r\23\16\23p\3\24\5\24t\n\24")
        buf.write("\3\25\5\25w\n\25\3\26\3\26\3\27\6\27|\n\27\r\27\16\27")
        buf.write("}\3\27\3\27\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\2)\2+\25-\26\3\2\4\4\2$$))\5\2\13\f\17\17\"\"\4?\2\62")
        buf.write("\2;\2\u00b4\2\u00b5\2\u00bb\2\u00bb\2\u00be\2\u00c0\2")
        buf.write("\u09f6\2\u09fb\2\u0b74\2\u0b79\2\u0bf2\2\u0bf4\2\u0c7a")
        buf.write("\2\u0c80\2\u0d5a\2\u0d60\2\u0d72\2\u0d7a\2\u0f2c\2\u0f35")
        buf.write("\2\u136b\2\u137e\2\u17f2\2\u17fb\2\u19dc\2\u19dc\2\u2072")
        buf.write("\2\u2072\2\u2076\2\u207b\2\u2082\2\u208b\2\u2152\2\u2161")
        buf.write("\2\u218b\2\u218b\2\u2462\2\u249d\2\u24ec\2\u2501\2\u2778")
        buf.write("\2\u2795\2\u2cff\2\u2cff\2\u3194\2\u3197\2\u3222\2\u322b")
        buf.write("\2\u324a\2\u3251\2\u3253\2\u3261\2\u3282\2\u328b\2\u32b3")
        buf.write("\2\u32c1\2\ua832\2\ua837\2\u0109\3\u0135\3\u0177\3\u017a")
        buf.write("\3\u018c\3\u018d\3\u02e3\3\u02fd\3\u0322\3\u0325\3\u085a")
        buf.write("\3\u0861\3\u087b\3\u0881\3\u08a9\3\u08b1\3\u08fd\3\u0901")
        buf.write("\3\u0918\3\u091d\3\u09be\3\u09bf\3\u09c2\3\u09d1\3\u09d4")
        buf.write("\3\u0a01\3\u0a42\3\u0a49\3\u0a7f\3\u0a80\3\u0a9f\3\u0aa1")
        buf.write("\3\u0aed\3\u0af1\3\u0b5a\3\u0b61\3\u0b7a\3\u0b81\3\u0bab")
        buf.write("\3\u0bb1\3\u0cfc\3\u0d01\3\u0e62\3\u0e80\3\u1054\3\u1067")
        buf.write("\3\u11e3\3\u11f6\3\u173c\3\u173d\3\u18ec\3\u18f4\3\u1c5c")
        buf.write("\3\u1c6e\3\u6b5d\3\u6b63\3\ud362\3\ud373\3\ue8c9\3\ue8d1")
        buf.write("\3\uf102\3\uf10e\3\u00bd\2#\2#\2&\2\'\2)\2)\2,\2-\2\61")
        buf.write("\2\61\2>\2A\2C\2\\\2c\2|\2~\2~\2\u0080\2\u0080\2\u00a3")
        buf.write("\2\u00a7\2\u00ae\2\u00ae\2\u00b3\2\u00b3\2\u00b7\2\u00b7")
        buf.write("\2\u00c2\2\u01bc\2\u01be\2\u01c1\2\u01c6\2\u01c6\2\u01c8")
        buf.write("\2\u01c9\2\u01cb\2\u01cc\2\u01ce\2\u01f3\2\u01f5\2\u0295")
        buf.write("\2\u0297\2\u02b1\2\u0372\2\u0375\2\u0378\2\u0379\2\u037d")
        buf.write("\2\u037f\2\u0381\2\u0381\2\u0388\2\u0388\2\u038a\2\u038c")
        buf.write("\2\u038e\2\u038e\2\u0390\2\u03a3\2\u03a5\2\u0483\2\u048c")
        buf.write("\2\u0531\2\u0533\2\u0558\2\u0563\2\u0589\2\u0591\2\u0591")
        buf.write("\2\u0608\2\u060a\2\u060d\2\u060d\2\u09f4\2\u09f5\2\u09fd")
        buf.write("\2\u09fd\2\u0af3\2\u0af3\2\u0bfb\2\u0bfb\2\u0e41\2\u0e41")
        buf.write("\2\u10a2\2\u10c7\2\u10c9\2\u10c9\2\u10cf\2\u10cf\2\u13a2")
        buf.write("\2\u13f7\2\u13fa\2\u13ff\2\u17dd\2\u17dd\2\u1c82\2\u1c8a")
        buf.write("\2\u1d02\2\u1d2d\2\u1d6d\2\u1d79\2\u1d7b\2\u1d9c\2\u1e02")
        buf.write("\2\u1f17\2\u1f1a\2\u1f1f\2\u1f22\2\u1f47\2\u1f4a\2\u1f4f")
        buf.write("\2\u1f52\2\u1f59\2\u1f5b\2\u1f5b\2\u1f5d\2\u1f5d\2\u1f5f")
        buf.write("\2\u1f5f\2\u1f61\2\u1f7f\2\u1f82\2\u1f89\2\u1f92\2\u1f99")
        buf.write("\2\u1fa2\2\u1fa9\2\u1fb2\2\u1fb6\2\u1fb8\2\u1fbd\2\u1fc0")
        buf.write("\2\u1fc0\2\u1fc4\2\u1fc6\2\u1fc8\2\u1fcd\2\u1fd2\2\u1fd5")
        buf.write("\2\u1fd8\2\u1fdd\2\u1fe2\2\u1fee\2\u1ff4\2\u1ff6\2\u1ff8")
        buf.write("\2\u1ffd\2\u2046\2\u2046\2\u2054\2\u2054\2\u207c\2\u207e")
        buf.write("\2\u208c\2\u208e\2\u20a2\2\u20c1\2\u2104\2\u2104\2\u2109")
        buf.write("\2\u2109\2\u210c\2\u2115\2\u2117\2\u2117\2\u211a\2\u211f")
        buf.write("\2\u2126\2\u2126\2\u2128\2\u2128\2\u212a\2\u212a\2\u212c")
        buf.write("\2\u212f\2\u2131\2\u2136\2\u213b\2\u213b\2\u213e\2\u214b")
        buf.write("\2\u214d\2\u214d\2\u2150\2\u2150\2\u2185\2\u2186\2\u2192")
        buf.write("\2\u2196\2\u219c\2\u219d\2\u21a2\2\u21a2\2\u21a5\2\u21a5")
        buf.write("\2\u21a8\2\u21a8\2\u21b0\2\u21b0\2\u21d0\2\u21d1\2\u21d4")
        buf.write("\2\u21d4\2\u21d6\2\u21d6\2\u21f6\2\u2301\2\u2322\2\u2323")
        buf.write("\2\u237e\2\u237e\2\u239d\2\u23b5\2\u23de\2\u23e3\2\u25b9")
        buf.write("\2\u25b9\2\u25c3\2\u25c3\2\u25fa\2\u2601\2\u2671\2\u2671")
        buf.write("\2\u27c2\2\u27c6\2\u27c9\2\u27e7\2\u27f2\2\u2801\2\u2902")
        buf.write("\2\u2984\2\u299b\2\u29d9\2\u29de\2\u29fd\2\u2a00\2\u2b01")
        buf.write("\2\u2b32\2\u2b46\2\u2b49\2\u2b4e\2\u2c02\2\u2c30\2\u2c32")
        buf.write("\2\u2c60\2\u2c62\2\u2c7d\2\u2c80\2\u2ce6\2\u2ced\2\u2cf0")
        buf.write("\2\u2cf4\2\u2cf5\2\u2d02\2\u2d27\2\u2d29\2\u2d29\2\u2d2f")
        buf.write("\2\u2d2f\2\ua642\2\ua66f\2\ua682\2\ua69d\2\ua724\2\ua771")
        buf.write("\2\ua773\2\ua789\2\ua78d\2\ua790\2\ua792\2\ua7b0\2\ua7b2")
        buf.write("\2\ua7b9\2\ua7fc\2\ua7fc\2\ua83a\2\ua83a\2\uab32\2\uab5c")
        buf.write("\2\uab62\2\uab67\2\uab72\2\uabc1\2\ufb02\2\ufb08\2\ufb15")
        buf.write("\2\ufb19\2\ufb2b\2\ufb2b\2\ufdfe\2\ufdfe\2\ufe64\2\ufe64")
        buf.write("\2\ufe66\2\ufe68\2\ufe6b\2\ufe6b\2\uff06\2\uff06\2\uff0d")
        buf.write("\2\uff0d\2\uff1e\2\uff20\2\uff23\2\uff3c\2\uff43\2\uff5c")
        buf.write("\2\uff5e\2\uff5e\2\uff60\2\uff60\2\uffe2\2\uffe4\2\uffe7")
        buf.write("\2\uffe8\2\uffeb\2\uffee\2\u0402\3\u0451\3\u04b2\3\u04d5")
        buf.write("\3\u04da\3\u04fd\3\u0c82\3\u0cb4\3\u0cc2\3\u0cf4\3\u18a2")
        buf.write("\3\u18e1\3\ud402\3\ud456\3\ud458\3\ud49e\3\ud4a0\3\ud4a1")
        buf.write("\3\ud4a4\3\ud4a4\3\ud4a7\3\ud4a8\3\ud4ab\3\ud4ae\3\ud4b0")
        buf.write("\3\ud4bb\3\ud4bd\3\ud4bd\3\ud4bf\3\ud4c5\3\ud4c7\3\ud507")
        buf.write("\3\ud509\3\ud50c\3\ud50f\3\ud516\3\ud518\3\ud51e\3\ud520")
        buf.write("\3\ud53b\3\ud53d\3\ud540\3\ud542\3\ud546\3\ud548\3\ud548")
        buf.write("\3\ud54c\3\ud552\3\ud554\3\ud6a7\3\ud6aa\3\ud7cd\3\ue902")
        buf.write("\3\ue945\3\ueef2\3\ueef3\3\u0082\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2+\3\2\2\2\2-")
        buf.write("\3\2\2\2\3/\3\2\2\2\5\61\3\2\2\2\7\64\3\2\2\2\t\67\3\2")
        buf.write("\2\2\139\3\2\2\2\r;\3\2\2\2\17=\3\2\2\2\21?\3\2\2\2\23")
        buf.write("A\3\2\2\2\25C\3\2\2\2\27E\3\2\2\2\31G\3\2\2\2\33I\3\2")
        buf.write("\2\2\35K\3\2\2\2\37Q\3\2\2\2!W\3\2\2\2#i\3\2\2\2%n\3\2")
        buf.write("\2\2\'s\3\2\2\2)v\3\2\2\2+x\3\2\2\2-{\3\2\2\2/\60\7/\2")
        buf.write("\2\60\4\3\2\2\2\61\62\7/\2\2\62\63\7@\2\2\63\6\3\2\2\2")
        buf.write("\64\65\7>\2\2\65\66\7/\2\2\66\b\3\2\2\2\678\7*\2\28\n")
        buf.write("\3\2\2\29:\7<\2\2:\f\3\2\2\2;<\7+\2\2<\16\3\2\2\2=>\7")
        buf.write("]\2\2>\20\3\2\2\2?@\7_\2\2@\22\3\2\2\2AB\7?\2\2B\24\3")
        buf.write("\2\2\2CD\7\60\2\2D\26\3\2\2\2EF\7.\2\2F\30\3\2\2\2GH\7")
        buf.write("a\2\2H\32\3\2\2\2IJ\7\"\2\2J\34\3\2\2\2KL\7O\2\2LM\7C")
        buf.write("\2\2MN\7V\2\2NO\7E\2\2OP\7J\2\2P\36\3\2\2\2QR\7Y\2\2R")
        buf.write("S\7J\2\2ST\7G\2\2TU\7T\2\2UV\7G\2\2V \3\2\2\2WX\7T\2\2")
        buf.write("XY\7G\2\2YZ\7V\2\2Z[\7W\2\2[\\\7T\2\2\\]\7P\2\2]f\3\2")
        buf.write("\2\2^_\7F\2\2_`\7K\2\2`a\7U\2\2ab\7V\2\2bc\7K\2\2cd\7")
        buf.write("P\2\2de\7E\2\2eg\7V\2\2f^\3\2\2\2fg\3\2\2\2g\"\3\2\2\2")
        buf.write("hj\5\'\24\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2\2l$")
        buf.write("\3\2\2\2mo\5)\25\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2")
        buf.write("\2\2q&\3\2\2\2rt\t\4\2\2sr\3\2\2\2t(\3\2\2\2uw\t\5\2\2")
        buf.write("vu\3\2\2\2w*\3\2\2\2xy\t\2\2\2y,\3\2\2\2z|\t\3\2\2{z\3")
        buf.write("\2\2\2|}\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0080\b\27\2\2\u0080.\3\2\2\2\t\2fkpsv}\3\b\2\2")
        return buf.getvalue()


class CypherLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    Match = 14
    Where = 15
    Return = 16
    INTEGER = 17
    STRING_LITERAL = 18
    SEP = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'->'", "'<-'", "'('", "':'", "')'", "'['", "']'", "'='", 
            "'.'", "','", "'_'", "' '", "'MATCH'", "'WHERE'" ]

    symbolicNames = [ "<INVALID>",
            "Match", "Where", "Return", "INTEGER", "STRING_LITERAL", "SEP", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "Match", 
                  "Where", "Return", "INTEGER", "STRING_LITERAL", "DIGIT", 
                  "CHAR", "SEP", "WS" ]

    grammarFileName = "Cypher.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


