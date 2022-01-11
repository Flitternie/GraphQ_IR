# Generated from ./parser/ir/UnifiedIRLexer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u0272\b\1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write("\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write("\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write("\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write("\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35")
        buf.write("\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4")
        buf.write("%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t")
        buf.write("-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63")
        buf.write("\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4")
        buf.write(":\t:\4;\t;\4<\t<\4=\t=\4>\t>\3\2\6\2\u0080\n\2\r\2\16")
        buf.write("\2\u0081\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3\u00cb\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u0111\n")
        buf.write("\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u015c\n\32\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0170\n\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0186")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u019d\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u01bb\n \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u01ca\n!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)")
        buf.write("\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\6\60\u021b\n\60\r\60\16\60\u021c\3")
        buf.write("\61\6\61\u0220\n\61\r\61\16\61\u0221\3\61\3\61\7\61\u0226")
        buf.write("\n\61\f\61\16\61\u0229\13\61\3\61\3\61\6\61\u022d\n\61")
        buf.write("\r\61\16\61\u022e\5\61\u0231\n\61\3\62\3\62\3\63\3\63")
        buf.write("\3\63\6\63\u0238\n\63\r\63\16\63\u0239\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\38\38\38\38\39\39\39\39\39\39\39\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3=\6")
        buf.write("=\u026d\n=\r=\16=\u026e\3>\3>\2\2?\4\3\6\4\b\5\n\6\f\7")
        buf.write("\16\b\20\t\22\n\24\13\26\f\30\r\32\16\34\17\36\20 \21")
        buf.write("\"\22$\23&\24(\25*\26,\27.\30\60\31\62\32\64\33\66\34")
        buf.write("8\35:\36<\37> @!B\"D#F$H%J&L\'N(P)R*T+V,X-Z.\\/^\60`\61")
        buf.write("b\62d\63f\64h\2j\2l\2n\65p\66r\67t8v9x:z;|\2\4\2\3\6\4")
        buf.write("\2\13\f\17\17\t\2##.\61<<AAC\\aac|\6\2\"\"*+>>@@\4\2>")
        buf.write(">@@\2\u0280\2\4\3\2\2\2\2\6\3\2\2\2\2\b\3\2\2\2\2\n\3")
        buf.write("\2\2\2\2\f\3\2\2\2\2\16\3\2\2\2\2\20\3\2\2\2\2\22\3\2")
        buf.write("\2\2\2\24\3\2\2\2\2\26\3\2\2\2\2\30\3\2\2\2\2\32\3\2\2")
        buf.write("\2\2\34\3\2\2\2\2\36\3\2\2\2\2 \3\2\2\2\2\"\3\2\2\2\2")
        buf.write("$\3\2\2\2\2&\3\2\2\2\2(\3\2\2\2\2*\3\2\2\2\2,\3\2\2\2")
        buf.write("\2.\3\2\2\2\2\60\3\2\2\2\2\62\3\2\2\2\2\64\3\2\2\2\2\66")
        buf.write("\3\2\2\2\28\3\2\2\2\2:\3\2\2\2\2<\3\2\2\2\2>\3\2\2\2\2")
        buf.write("@\3\2\2\2\2B\3\2\2\2\2D\3\2\2\2\2F\3\2\2\2\2H\3\2\2\2")
        buf.write("\2J\3\2\2\2\2L\3\2\2\2\2N\3\2\2\2\2P\3\2\2\2\2R\3\2\2")
        buf.write("\2\2T\3\2\2\2\2V\3\2\2\2\2X\3\2\2\2\2Z\3\2\2\2\2\\\3\2")
        buf.write("\2\2\2^\3\2\2\2\2`\3\2\2\2\2b\3\2\2\2\2d\3\2\2\2\2f\3")
        buf.write("\2\2\2\3n\3\2\2\2\3p\3\2\2\2\3r\3\2\2\2\3t\3\2\2\2\3v")
        buf.write("\3\2\2\2\3x\3\2\2\2\3z\3\2\2\2\4\177\3\2\2\2\6\u00ca\3")
        buf.write("\2\2\2\b\u00cc\3\2\2\2\n\u00de\3\2\2\2\f\u00e7\3\2\2\2")
        buf.write("\16\u00ef\3\2\2\2\20\u00f2\3\2\2\2\22\u00f7\3\2\2\2\24")
        buf.write("\u00fa\3\2\2\2\26\u0100\3\2\2\2\30\u0110\3\2\2\2\32\u0112")
        buf.write("\3\2\2\2\34\u0116\3\2\2\2\36\u011c\3\2\2\2 \u0121\3\2")
        buf.write("\2\2\"\u0125\3\2\2\2$\u0129\3\2\2\2&\u012b\3\2\2\2(\u012d")
        buf.write("\3\2\2\2*\u0135\3\2\2\2,\u013e\3\2\2\2.\u0142\3\2\2\2")
        buf.write("\60\u0145\3\2\2\2\62\u0149\3\2\2\2\64\u015b\3\2\2\2\66")
        buf.write("\u016f\3\2\2\28\u0185\3\2\2\2:\u019c\3\2\2\2<\u019e\3")
        buf.write("\2\2\2>\u01a7\3\2\2\2@\u01ba\3\2\2\2B\u01c9\3\2\2\2D\u01cb")
        buf.write("\3\2\2\2F\u01d0\3\2\2\2H\u01d7\3\2\2\2J\u01dc\3\2\2\2")
        buf.write("L\u01e1\3\2\2\2N\u01e6\3\2\2\2P\u01ea\3\2\2\2R\u01ef\3")
        buf.write("\2\2\2T\u01f5\3\2\2\2V\u01fb\3\2\2\2X\u0201\3\2\2\2Z\u0207")
        buf.write("\3\2\2\2\\\u020d\3\2\2\2^\u0213\3\2\2\2`\u021a\3\2\2\2")
        buf.write("b\u0230\3\2\2\2d\u0232\3\2\2\2f\u0237\3\2\2\2h\u023b\3")
        buf.write("\2\2\2j\u023d\3\2\2\2l\u023f\3\2\2\2n\u0241\3\2\2\2p\u0248")
        buf.write("\3\2\2\2r\u024f\3\2\2\2t\u0256\3\2\2\2v\u025d\3\2\2\2")
        buf.write("x\u0264\3\2\2\2z\u026c\3\2\2\2|\u0270\3\2\2\2~\u0080\t")
        buf.write("\2\2\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\177\3\2")
        buf.write("\2\2\u0081\u0082\3\2\2\2\u0082\u0083\3\2\2\2\u0083\u0084")
        buf.write("\b\2\2\2\u0084\5\3\2\2\2\u0085\u0086\7y\2\2\u0086\u0087")
        buf.write("\7j\2\2\u0087\u0088\7c\2\2\u0088\u0089\7v\2\2\u0089\u008a")
        buf.write("\7\"\2\2\u008a\u008b\7k\2\2\u008b\u00cb\7u\2\2\u008c\u008d")
        buf.write("\7y\2\2\u008d\u008e\7j\2\2\u008e\u008f\7c\2\2\u008f\u0090")
        buf.write("\7v\2\2\u0090\u0091\7\"\2\2\u0091\u0092\7k\2\2\u0092\u0093")
        buf.write("\7u\2\2\u0093\u0094\7\"\2\2\u0094\u0095\7v\2\2\u0095\u0096")
        buf.write("\7j\2\2\u0096\u0097\7g\2\2\u0097\u0098\7\"\2\2\u0098\u0099")
        buf.write("\7c\2\2\u0099\u009a\7v\2\2\u009a\u009b\7v\2\2\u009b\u009c")
        buf.write("\7t\2\2\u009c\u009d\7k\2\2\u009d\u009e\7d\2\2\u009e\u009f")
        buf.write("\7w\2\2\u009f\u00a0\7v\2\2\u00a0\u00cb\7g\2\2\u00a1\u00a2")
        buf.write("\7y\2\2\u00a2\u00a3\7j\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7v\2\2\u00a5\u00a6\7\"\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8")
        buf.write("\7u\2\2\u00a8\u00a9\7\"\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7j\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7\"\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1")
        buf.write("\7c\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4")
        buf.write("\7q\2\2\u00b4\u00cb\7p\2\2\u00b5\u00b6\7y\2\2\u00b6\u00b7")
        buf.write("\7j\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba")
        buf.write("\7\"\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd")
        buf.write("\7\"\2\2\u00bd\u00be\7v\2\2\u00be\u00bf\7j\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\u00c1\7\"\2\2\u00c1\u00c2\7s\2\2\u00c2\u00c3")
        buf.write("\7w\2\2\u00c3\u00c4\7c\2\2\u00c4\u00c5\7n\2\2\u00c5\u00c6")
        buf.write("\7k\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\u00cb\7t\2\2\u00ca\u0085\3\2\2\2\u00ca\u008c")
        buf.write("\3\2\2\2\u00ca\u00a1\3\2\2\2\u00ca\u00b5\3\2\2\2\u00cb")
        buf.write("\7\3\2\2\2\u00cc\u00cd\7y\2\2\u00cd\u00ce\7j\2\2\u00ce")
        buf.write("\u00cf\7k\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1\7j\2\2\u00d1")
        buf.write("\u00d2\7\"\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4\7p\2\2\u00d4")
        buf.write("\u00d5\7g\2\2\u00d5\u00d6\7\"\2\2\u00d6\u00d7\7j\2\2\u00d7")
        buf.write("\u00d8\7c\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da\7\"\2\2\u00da")
        buf.write("\u00db\7v\2\2\u00db\u00dc\7j\2\2\u00dc\u00dd\7g\2\2\u00dd")
        buf.write("\t\3\2\2\2\u00de\u00df\7j\2\2\u00df\u00e0\7q\2\2\u00e0")
        buf.write("\u00e1\7y\2\2\u00e1\u00e2\7\"\2\2\u00e2\u00e3\7o\2\2\u00e3")
        buf.write("\u00e4\7c\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7{\2\2\u00e6")
        buf.write("\13\3\2\2\2\u00e7\u00e8\7y\2\2\u00e8\u00e9\7j\2\2\u00e9")
        buf.write("\u00ea\7g\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7j\2\2\u00ec")
        buf.write("\u00ed\7g\2\2\u00ed\u00ee\7t\2\2\u00ee\r\3\2\2\2\u00ef")
        buf.write("\u00f0\7q\2\2\u00f0\u00f1\7h\2\2\u00f1\17\3\2\2\2\u00f2")
        buf.write("\u00f3\7h\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5\7q\2\2\u00f5")
        buf.write("\u00f6\7o\2\2\u00f6\21\3\2\2\2\u00f7\u00f8\7v\2\2\u00f8")
        buf.write("\u00f9\7q\2\2\u00f9\23\3\2\2\2\u00fa\u00fb\7c\2\2\u00fb")
        buf.write("\u00fc\7o\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe\7p\2\2\u00fe")
        buf.write("\u00ff\7i\2\2\u00ff\25\3\2\2\2\u0100\u0101\7v\2\2\u0101")
        buf.write("\u0102\7q\2\2\u0102\u0103\7r\2\2\u0103\27\3\2\2\2\u0104")
        buf.write("\u0105\7q\2\2\u0105\u0106\7p\2\2\u0106\u0107\7g\2\2\u0107")
        buf.write("\u0111\7u\2\2\u0108\u0109\7g\2\2\u0109\u010a\7p\2\2\u010a")
        buf.write("\u010b\7v\2\2\u010b\u010c\7k\2\2\u010c\u010d\7v\2\2\u010d")
        buf.write("\u010e\7k\2\2\u010e\u010f\7g\2\2\u010f\u0111\7u\2\2\u0110")
        buf.write("\u0104\3\2\2\2\u0110\u0108\3\2\2\2\u0111\31\3\2\2\2\u0112")
        buf.write("\u0113\7v\2\2\u0113\u0114\7j\2\2\u0114\u0115\7g\2\2\u0115")
        buf.write("\33\3\2\2\2\u0116\u0117\7y\2\2\u0117\u0118\7j\2\2\u0118")
        buf.write("\u0119\7q\2\2\u0119\u011a\7u\2\2\u011a\u011b\7g\2\2\u011b")
        buf.write("\35\3\2\2\2\u011c\u011d\7v\2\2\u011d\u011e\7j\2\2\u011e")
        buf.write("\u011f\7c\2\2\u011f\u0120\7v\2\2\u0120\37\3\2\2\2\u0121")
        buf.write("\u0122\7j\2\2\u0122\u0123\7c\2\2\u0123\u0124\7u\2\2\u0124")
        buf.write("!\3\2\2\2\u0125\u0126\7p\2\2\u0126\u0127\7q\2\2\u0127")
        buf.write("\u0128\7v\2\2\u0128#\3\2\2\2\u0129\u012a\7*\2\2\u012a")
        buf.write("%\3\2\2\2\u012b\u012c\7+\2\2\u012c\'\3\2\2\2\u012d\u012e")
        buf.write("\7h\2\2\u012e\u012f\7q\2\2\u012f\u0130\7t\2\2\u0130\u0131")
        buf.write("\7y\2\2\u0131\u0132\7c\2\2\u0132\u0133\7t\2\2\u0133\u0134")
        buf.write("\7f\2\2\u0134)\3\2\2\2\u0135\u0136\7d\2\2\u0136\u0137")
        buf.write("\7c\2\2\u0137\u0138\7e\2\2\u0138\u0139\7m\2\2\u0139\u013a")
        buf.write("\7y\2\2\u013a\u013b\7c\2\2\u013b\u013c\7t\2\2\u013c\u013d")
        buf.write("\7f\2\2\u013d+\3\2\2\2\u013e\u013f\7c\2\2\u013f\u0140")
        buf.write("\7p\2\2\u0140\u0141\7f\2\2\u0141-\3\2\2\2\u0142\u0143")
        buf.write("\7q\2\2\u0143\u0144\7t\2\2\u0144/\3\2\2\2\u0145\u0146")
        buf.write("\7u\2\2\u0146\u0147\7w\2\2\u0147\u0148\7o\2\2\u0148\61")
        buf.write("\3\2\2\2\u0149\u014a\7c\2\2\u014a\u014b\7x\2\2\u014b\u014c")
        buf.write("\7g\2\2\u014c\u014d\7t\2\2\u014d\u014e\7c\2\2\u014e\u014f")
        buf.write("\7i\2\2\u014f\u0150\7g\2\2\u0150\63\3\2\2\2\u0151\u0152")
        buf.write("\7k\2\2\u0152\u015c\7u\2\2\u0153\u0154\7g\2\2\u0154\u0155")
        buf.write("\7s\2\2\u0155\u0156\7w\2\2\u0156\u0157\7c\2\2\u0157\u0158")
        buf.write("\7n\2\2\u0158\u0159\7\"\2\2\u0159\u015a\7v\2\2\u015a\u015c")
        buf.write("\7q\2\2\u015b\u0151\3\2\2\2\u015b\u0153\3\2\2\2\u015c")
        buf.write("\65\3\2\2\2\u015d\u015e\7k\2\2\u015e\u015f\7u\2\2\u015f")
        buf.write("\u0160\7\"\2\2\u0160\u0161\7p\2\2\u0161\u0162\7q\2\2\u0162")
        buf.write("\u0170\7v\2\2\u0163\u0164\7p\2\2\u0164\u0165\7q\2\2\u0165")
        buf.write("\u0166\7v\2\2\u0166\u0167\7\"\2\2\u0167\u0168\7g\2\2\u0168")
        buf.write("\u0169\7s\2\2\u0169\u016a\7w\2\2\u016a\u016b\7c\2\2\u016b")
        buf.write("\u016c\7n\2\2\u016c\u016d\7\"\2\2\u016d\u016e\7v\2\2\u016e")
        buf.write("\u0170\7q\2\2\u016f\u015d\3\2\2\2\u016f\u0163\3\2\2\2")
        buf.write("\u0170\67\3\2\2\2\u0171\u0172\7n\2\2\u0172\u0173\7c\2")
        buf.write("\2\u0173\u0174\7t\2\2\u0174\u0175\7i\2\2\u0175\u0176\7")
        buf.write("g\2\2\u0176\u0177\7t\2\2\u0177\u0178\7\"\2\2\u0178\u0179")
        buf.write("\7v\2\2\u0179\u017a\7j\2\2\u017a\u017b\7c\2\2\u017b\u0186")
        buf.write("\7p\2\2\u017c\u017d\7o\2\2\u017d\u017e\7q\2\2\u017e\u017f")
        buf.write("\7t\2\2\u017f\u0180\7g\2\2\u0180\u0181\7\"\2\2\u0181\u0182")
        buf.write("\7v\2\2\u0182\u0183\7j\2\2\u0183\u0184\7c\2\2\u0184\u0186")
        buf.write("\7p\2\2\u0185\u0171\3\2\2\2\u0185\u017c\3\2\2\2\u0186")
        buf.write("9\3\2\2\2\u0187\u0188\7u\2\2\u0188\u0189\7o\2\2\u0189")
        buf.write("\u018a\7c\2\2\u018a\u018b\7n\2\2\u018b\u018c\7n\2\2\u018c")
        buf.write("\u018d\7g\2\2\u018d\u018e\7t\2\2\u018e\u018f\7\"\2\2\u018f")
        buf.write("\u0190\7v\2\2\u0190\u0191\7j\2\2\u0191\u0192\7c\2\2\u0192")
        buf.write("\u019d\7p\2\2\u0193\u0194\7n\2\2\u0194\u0195\7g\2\2\u0195")
        buf.write("\u0196\7u\2\2\u0196\u0197\7u\2\2\u0197\u0198\7\"\2\2\u0198")
        buf.write("\u0199\7v\2\2\u0199\u019a\7j\2\2\u019a\u019b\7c\2\2\u019b")
        buf.write("\u019d\7p\2\2\u019c\u0187\3\2\2\2\u019c\u0193\3\2\2\2")
        buf.write("\u019d;\3\2\2\2\u019e\u019f\7c\2\2\u019f\u01a0\7v\2\2")
        buf.write("\u01a0\u01a1\7\"\2\2\u01a1\u01a2\7n\2\2\u01a2\u01a3\7")
        buf.write("g\2\2\u01a3\u01a4\7c\2\2\u01a4\u01a5\7u\2\2\u01a5\u01a6")
        buf.write("\7v\2\2\u01a6=\3\2\2\2\u01a7\u01a8\7c\2\2\u01a8\u01a9")
        buf.write("\7v\2\2\u01a9\u01aa\7\"\2\2\u01aa\u01ab\7o\2\2\u01ab\u01ac")
        buf.write("\7q\2\2\u01ac\u01ad\7u\2\2\u01ad\u01ae\7v\2\2\u01ae?\3")
        buf.write("\2\2\2\u01af\u01b0\7n\2\2\u01b0\u01b1\7c\2\2\u01b1\u01b2")
        buf.write("\7t\2\2\u01b2\u01b3\7i\2\2\u01b3\u01b4\7g\2\2\u01b4\u01b5")
        buf.write("\7u\2\2\u01b5\u01bb\7v\2\2\u01b6\u01b7\7o\2\2\u01b7\u01b8")
        buf.write("\7q\2\2\u01b8\u01b9\7u\2\2\u01b9\u01bb\7v\2\2\u01ba\u01af")
        buf.write("\3\2\2\2\u01ba\u01b6\3\2\2\2\u01bbA\3\2\2\2\u01bc\u01bd")
        buf.write("\7u\2\2\u01bd\u01be\7o\2\2\u01be\u01bf\7c\2\2\u01bf\u01c0")
        buf.write("\7n\2\2\u01c0\u01c1\7n\2\2\u01c1\u01c2\7g\2\2\u01c2\u01c3")
        buf.write("\7u\2\2\u01c3\u01ca\7v\2\2\u01c4\u01c5\7n\2\2\u01c5\u01c6")
        buf.write("\7g\2\2\u01c6\u01c7\7c\2\2\u01c7\u01c8\7u\2\2\u01c8\u01ca")
        buf.write("\7v\2\2\u01c9\u01bc\3\2\2\2\u01c9\u01c4\3\2\2\2\u01ca")
        buf.write("C\3\2\2\2\u01cb\u01cc\7v\2\2\u01cc\u01cd\7g\2\2\u01cd")
        buf.write("\u01ce\7z\2\2\u01ce\u01cf\7v\2\2\u01cfE\3\2\2\2\u01d0")
        buf.write("\u01d1\7p\2\2\u01d1\u01d2\7w\2\2\u01d2\u01d3\7o\2\2\u01d3")
        buf.write("\u01d4\7d\2\2\u01d4\u01d5\7g\2\2\u01d5\u01d6\7t\2\2\u01d6")
        buf.write("G\3\2\2\2\u01d7\u01d8\7f\2\2\u01d8\u01d9\7c\2\2\u01d9")
        buf.write("\u01da\7v\2\2\u01da\u01db\7g\2\2\u01dbI\3\2\2\2\u01dc")
        buf.write("\u01dd\7{\2\2\u01dd\u01de\7g\2\2\u01de\u01df\7c\2\2\u01df")
        buf.write("\u01e0\7t\2\2\u01e0K\3\2\2\2\u01e1\u01e2\7v\2\2\u01e2")
        buf.write("\u01e3\7k\2\2\u01e3\u01e4\7o\2\2\u01e4\u01e5\7g\2\2\u01e5")
        buf.write("M\3\2\2\2\u01e6\u01e7\7\"\2\2\u01e7\u01e8\3\2\2\2\u01e8")
        buf.write("\u01e9\b\'\2\2\u01e9O\3\2\2\2\u01ea\u01eb\7>\2\2\u01eb")
        buf.write("\u01ec\7G\2\2\u01ec\u01ed\7U\2\2\u01ed\u01ee\7@\2\2\u01ee")
        buf.write("Q\3\2\2\2\u01ef\u01f0\7>\2\2\u01f0\u01f1\7\61\2\2\u01f1")
        buf.write("\u01f2\7G\2\2\u01f2\u01f3\7U\2\2\u01f3\u01f4\7@\2\2\u01f4")
        buf.write("S\3\2\2\2\u01f5\u01f6\7>\2\2\u01f6\u01f7\7G\2\2\u01f7")
        buf.write("\u01f8\7@\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\b*\3\2\u01fa")
        buf.write("U\3\2\2\2\u01fb\u01fc\7>\2\2\u01fc\u01fd\7C\2\2\u01fd")
        buf.write("\u01fe\7@\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0200\b+\3\2\u0200")
        buf.write("W\3\2\2\2\u0201\u0202\7>\2\2\u0202\u0203\7T\2\2\u0203")
        buf.write("\u0204\7@\2\2\u0204\u0205\3\2\2\2\u0205\u0206\b,\3\2\u0206")
        buf.write("Y\3\2\2\2\u0207\u0208\7>\2\2\u0208\u0209\7E\2\2\u0209")
        buf.write("\u020a\7@\2\2\u020a\u020b\3\2\2\2\u020b\u020c\b-\3\2\u020c")
        buf.write("[\3\2\2\2\u020d\u020e\7>\2\2\u020e\u020f\7S\2\2\u020f")
        buf.write("\u0210\7@\2\2\u0210\u0211\3\2\2\2\u0211\u0212\b.\3\2\u0212")
        buf.write("]\3\2\2\2\u0213\u0214\7>\2\2\u0214\u0215\7X\2\2\u0215")
        buf.write("\u0216\7@\2\2\u0216\u0217\3\2\2\2\u0217\u0218\b/\3\2\u0218")
        buf.write("_\3\2\2\2\u0219\u021b\5d\62\2\u021a\u0219\3\2\2\2\u021b")
        buf.write("\u021c\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2")
        buf.write("\u021da\3\2\2\2\u021e\u0220\5d\62\2\u021f\u021e\3\2\2")
        buf.write("\2\u0220\u0221\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0227\7\60\2\2\u0224")
        buf.write("\u0226\5d\62\2\u0225\u0224\3\2\2\2\u0226\u0229\3\2\2\2")
        buf.write("\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0231\3")
        buf.write("\2\2\2\u0229\u0227\3\2\2\2\u022a\u022c\7\60\2\2\u022b")
        buf.write("\u022d\5d\62\2\u022c\u022b\3\2\2\2\u022d\u022e\3\2\2\2")
        buf.write("\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0231\3")
        buf.write("\2\2\2\u0230\u021f\3\2\2\2\u0230\u022a\3\2\2\2\u0231c")
        buf.write("\3\2\2\2\u0232\u0233\5h\64\2\u0233e\3\2\2\2\u0234\u0238")
        buf.write("\5j\65\2\u0235\u0238\5d\62\2\u0236\u0238\5l\66\2\u0237")
        buf.write("\u0234\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0236\3\2\2\2")
        buf.write("\u0238\u0239\3\2\2\2\u0239\u0237\3\2\2\2\u0239\u023a\3")
        buf.write("\2\2\2\u023ag\3\2\2\2\u023b\u023c\4\62;\2\u023ci\3\2\2")
        buf.write("\2\u023d\u023e\t\3\2\2\u023ek\3\2\2\2\u023f\u0240\n\4")
        buf.write("\2\2\u0240m\3\2\2\2\u0241\u0242\7>\2\2\u0242\u0243\7\61")
        buf.write("\2\2\u0243\u0244\7G\2\2\u0244\u0245\7@\2\2\u0245\u0246")
        buf.write("\3\2\2\2\u0246\u0247\b\67\4\2\u0247o\3\2\2\2\u0248\u0249")
        buf.write("\7>\2\2\u0249\u024a\7\61\2\2\u024a\u024b\7C\2\2\u024b")
        buf.write("\u024c\7@\2\2\u024c\u024d\3\2\2\2\u024d\u024e\b8\4\2\u024e")
        buf.write("q\3\2\2\2\u024f\u0250\7>\2\2\u0250\u0251\7\61\2\2\u0251")
        buf.write("\u0252\7T\2\2\u0252\u0253\7@\2\2\u0253\u0254\3\2\2\2\u0254")
        buf.write("\u0255\b9\4\2\u0255s\3\2\2\2\u0256\u0257\7>\2\2\u0257")
        buf.write("\u0258\7\61\2\2\u0258\u0259\7E\2\2\u0259\u025a\7@\2\2")
        buf.write("\u025a\u025b\3\2\2\2\u025b\u025c\b:\4\2\u025cu\3\2\2\2")
        buf.write("\u025d\u025e\7>\2\2\u025e\u025f\7\61\2\2\u025f\u0260\7")
        buf.write("S\2\2\u0260\u0261\7@\2\2\u0261\u0262\3\2\2\2\u0262\u0263")
        buf.write("\b;\4\2\u0263w\3\2\2\2\u0264\u0265\7>\2\2\u0265\u0266")
        buf.write("\7\61\2\2\u0266\u0267\7X\2\2\u0267\u0268\7@\2\2\u0268")
        buf.write("\u0269\3\2\2\2\u0269\u026a\b<\4\2\u026ay\3\2\2\2\u026b")
        buf.write("\u026d\5|>\2\u026c\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e")
        buf.write("\u026c\3\2\2\2\u026e\u026f\3\2\2\2\u026f{\3\2\2\2\u0270")
        buf.write("\u0271\n\5\2\2\u0271}\3\2\2\2\25\2\3\u0081\u00ca\u0110")
        buf.write("\u015b\u016f\u0185\u019c\u01ba\u01c9\u021c\u0221\u0227")
        buf.write("\u022e\u0230\u0237\u0239\u026e\5\b\2\2\4\3\2\4\2\2")
        return buf.getvalue()


class UnifiedIRLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAR = 1

    WS = 1
    What = 2
    Select = 3
    Count = 4
    Verify = 5
    Of = 6
    From = 7
    To = 8
    Among = 9
    Top = 10
    Ones = 11
    The = 12
    Whose = 13
    That = 14
    Has = 15
    Not = 16
    LB = 17
    RB = 18
    Forward = 19
    Backward = 20
    And = 21
    Or = 22
    Sum = 23
    Average = 24
    Is = 25
    IsNot = 26
    LargerThan = 27
    SmallerThan = 28
    AtLeast = 29
    AtMost = 30
    Largest = 31
    Smallest = 32
    Text = 33
    Quantity = 34
    Date = 35
    Year = 36
    Time = 37
    SPACE = 38
    ES_START = 39
    ES_END = 40
    ENTI_START = 41
    ATTR_START = 42
    PRED_START = 43
    CONC_START = 44
    QUAL_START = 45
    VALU_START = 46
    INTEGER = 47
    DECIMAL = 48
    DIGIT = 49
    STRING_LITERAL = 50
    ENTI_END = 51
    ATTR_END = 52
    PRED_END = 53
    CONC_END = 54
    QUAL_END = 55
    VALU_END = 56
    LITERAL = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "VAR" ]

    literalNames = [ "<INVALID>",
            "'which one has the'", "'how many'", "'whether'", "'of'", "'from'", 
            "'to'", "'among'", "'top'", "'the'", "'whose'", "'that'", "'has'", 
            "'not'", "'('", "')'", "'forward'", "'backward'", "'and'", "'or'", 
            "'sum'", "'average'", "'at least'", "'at most'", "'text'", "'number'", 
            "'date'", "'year'", "'time'", "' '", "'<ES>'", "'</ES>'", "'<E>'", 
            "'<A>'", "'<R>'", "'<C>'", "'<Q>'", "'<V>'", "'</E>'", "'</A>'", 
            "'</R>'", "'</C>'", "'</Q>'", "'</V>'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "What", "Select", "Count", "Verify", "Of", "From", "To", 
            "Among", "Top", "Ones", "The", "Whose", "That", "Has", "Not", 
            "LB", "RB", "Forward", "Backward", "And", "Or", "Sum", "Average", 
            "Is", "IsNot", "LargerThan", "SmallerThan", "AtLeast", "AtMost", 
            "Largest", "Smallest", "Text", "Quantity", "Date", "Year", "Time", 
            "SPACE", "ES_START", "ES_END", "ENTI_START", "ATTR_START", "PRED_START", 
            "CONC_START", "QUAL_START", "VALU_START", "INTEGER", "DECIMAL", 
            "DIGIT", "STRING_LITERAL", "ENTI_END", "ATTR_END", "PRED_END", 
            "CONC_END", "QUAL_END", "VALU_END", "LITERAL" ]

    ruleNames = [ "WS", "What", "Select", "Count", "Verify", "Of", "From", 
                  "To", "Among", "Top", "Ones", "The", "Whose", "That", 
                  "Has", "Not", "LB", "RB", "Forward", "Backward", "And", 
                  "Or", "Sum", "Average", "Is", "IsNot", "LargerThan", "SmallerThan", 
                  "AtLeast", "AtMost", "Largest", "Smallest", "Text", "Quantity", 
                  "Date", "Year", "Time", "SPACE", "ES_START", "ES_END", 
                  "ENTI_START", "ATTR_START", "PRED_START", "CONC_START", 
                  "QUAL_START", "VALU_START", "INTEGER", "DECIMAL", "DIGIT", 
                  "STRING_LITERAL", "DIGIT_BASE", "CHARS_BASE", "UNICODE", 
                  "ENTI_END", "ATTR_END", "PRED_END", "CONC_END", "QUAL_END", 
                  "VALU_END", "LITERAL", "ANY_CHAR" ]

    grammarFileName = "UnifiedIRLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


