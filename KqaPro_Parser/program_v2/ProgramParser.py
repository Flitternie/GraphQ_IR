# Generated from ./KqaPro_Parser/program_v2/Program.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u01b3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0080\n\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\5\7\u0093\n\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00a4\n\13\3\13")
        buf.write("\5\13\u00a7\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00b2\n\13\7\13\u00b4\n\13\f\13\16\13\u00b7")
        buf.write("\13\13\3\f\3\f\5\f\u00bb\n\f\3\f\5\f\u00be\n\f\3\r\3\r")
        buf.write("\5\r\u00c2\n\r\3\r\5\r\u00c5\n\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\5\22\u00d1\n\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u00db\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u0117\n\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("%\3%\3&\3&\3&\3&\5&\u0147\n&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\5\60\u0179\n\60\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\5\62\u0181\n\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\5\65\u0189\n\65\3\66\3\66\3\67\3\67\38\38\39")
        buf.write("\39\39\39\39\39\69\u0197\n9\r9\169\u0198\3:\6:\u019c\n")
        buf.write(":\r:\16:\u019d\3:\3:\6:\u01a2\n:\r:\16:\u01a3\3:\3:\6")
        buf.write(":\u01a8\n:\r:\16:\u01a9\3;\3;\3;\3;\3;\3<\3<\3<\5\u019d")
        buf.write("\u01a3\u01a9\3\24=\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtv\2\6\3\2\36!\3\2\"#\3\2$%\3\2*,\2\u019f\2\177\3\2")
        buf.write("\2\2\4\u0083\3\2\2\2\6\u0086\3\2\2\2\b\u0089\3\2\2\2\n")
        buf.write("\u008c\3\2\2\2\f\u008f\3\2\2\2\16\u0096\3\2\2\2\20\u0099")
        buf.write("\3\2\2\2\22\u009c\3\2\2\2\24\u00a6\3\2\2\2\26\u00b8\3")
        buf.write("\2\2\2\30\u00bf\3\2\2\2\32\u00c6\3\2\2\2\34\u00c8\3\2")
        buf.write("\2\2\36\u00ca\3\2\2\2 \u00cc\3\2\2\2\"\u00d0\3\2\2\2$")
        buf.write("\u00d2\3\2\2\2&\u00d4\3\2\2\2(\u00da\3\2\2\2*\u00dc\3")
        buf.write("\2\2\2,\u00e2\3\2\2\2.\u00ea\3\2\2\2\60\u00f2\3\2\2\2")
        buf.write("\62\u00fa\3\2\2\2\64\u00fc\3\2\2\2\66\u0106\3\2\2\28\u010e")
        buf.write("\3\2\2\2:\u0116\3\2\2\2<\u0118\3\2\2\2>\u011c\3\2\2\2")
        buf.write("@\u0122\3\2\2\2B\u0128\3\2\2\2D\u012e\3\2\2\2F\u0136\3")
        buf.write("\2\2\2H\u013c\3\2\2\2J\u0146\3\2\2\2L\u0148\3\2\2\2N\u014e")
        buf.write("\3\2\2\2P\u0156\3\2\2\2R\u015e\3\2\2\2T\u0166\3\2\2\2")
        buf.write("V\u016a\3\2\2\2X\u016e\3\2\2\2Z\u0170\3\2\2\2\\\u0172")
        buf.write("\3\2\2\2^\u0178\3\2\2\2`\u017a\3\2\2\2b\u0180\3\2\2\2")
        buf.write("d\u0182\3\2\2\2f\u0184\3\2\2\2h\u0188\3\2\2\2j\u018a\3")
        buf.write("\2\2\2l\u018c\3\2\2\2n\u018e\3\2\2\2p\u0196\3\2\2\2r\u019b")
        buf.write("\3\2\2\2t\u01ab\3\2\2\2v\u01b0\3\2\2\2x\u0080\5\4\3\2")
        buf.write("y\u0080\5\6\4\2z\u0080\5\b\5\2{\u0080\5\n\6\2|\u0080\5")
        buf.write("\f\7\2}\u0080\5\16\b\2~\u0080\5\20\t\2\177x\3\2\2\2\177")
        buf.write("y\3\2\2\2\177z\3\2\2\2\177{\3\2\2\2\177|\3\2\2\2\177}")
        buf.write("\3\2\2\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082")
        buf.write("\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084\5\24\13\2\u0084\u0085")
        buf.write("\5\34\17\2\u0085\5\3\2\2\2\u0086\u0087\5\24\13\2\u0087")
        buf.write("\u0088\5\36\20\2\u0088\7\3\2\2\2\u0089\u008a\5\24\13\2")
        buf.write("\u008a\u008b\58\35\2\u008b\t\3\2\2\2\u008c\u008d\5\22")
        buf.write("\n\2\u008d\u008e\5\62\32\2\u008e\13\3\2\2\2\u008f\u0092")
        buf.write("\5\24\13\2\u0090\u0093\5\66\34\2\u0091\u0093\58\35\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0095\5:\36\2\u0095\r\3\2\2\2\u0096\u0097\5\24")
        buf.write("\13\2\u0097\u0098\5D#\2\u0098\17\3\2\2\2\u0099\u009a\5")
        buf.write("\22\n\2\u009a\u009b\5F$\2\u009b\21\3\2\2\2\u009c\u009d")
        buf.write("\5\24\13\2\u009d\u009e\5\24\13\2\u009e\23\3\2\2\2\u009f")
        buf.write("\u00a0\b\13\1\2\u00a0\u00a3\5 \21\2\u00a1\u00a4\5\30\r")
        buf.write("\2\u00a2\u00a4\5\32\16\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a7\5V,\2\u00a6\u009f")
        buf.write("\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00b5\3\2\2\2\u00a8")
        buf.write("\u00a9\f\7\2\2\u00a9\u00aa\5\24\13\2\u00aa\u00ab\5\"\22")
        buf.write("\2\u00ab\u00b4\3\2\2\2\u00ac\u00ad\f\6\2\2\u00ad\u00b4")
        buf.write("\5\64\33\2\u00ae\u00b1\f\5\2\2\u00af\u00b2\5\26\f\2\u00b0")
        buf.write("\u00b2\5\30\r\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2")
        buf.write("\2\u00b2\u00b4\3\2\2\2\u00b3\u00a8\3\2\2\2\u00b3\u00ac")
        buf.write("\3\2\2\2\u00b3\u00ae\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\25\3\2\2\2\u00b7")
        buf.write("\u00b5\3\2\2\2\u00b8\u00ba\5H%\2\u00b9\u00bb\5J&\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2")
        buf.write("\u00bc\u00be\5T+\2\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2")
        buf.write("\2\2\u00be\27\3\2\2\2\u00bf\u00c1\5(\25\2\u00c0\u00c2")
        buf.write("\5J&\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4")
        buf.write("\3\2\2\2\u00c3\u00c5\5T+\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\31\3\2\2\2\u00c6\u00c7\5T+\2\u00c7\33\3")
        buf.write("\2\2\2\u00c8\u00c9\7\3\2\2\u00c9\35\3\2\2\2\u00ca\u00cb")
        buf.write("\7\4\2\2\u00cb\37\3\2\2\2\u00cc\u00cd\7\5\2\2\u00cd!\3")
        buf.write("\2\2\2\u00ce\u00d1\5$\23\2\u00cf\u00d1\5&\24\2\u00d0\u00ce")
        buf.write("\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1#\3\2\2\2\u00d2\u00d3")
        buf.write("\7\6\2\2\u00d3%\3\2\2\2\u00d4\u00d5\7\7\2\2\u00d5\'\3")
        buf.write("\2\2\2\u00d6\u00db\5*\26\2\u00d7\u00db\5,\27\2\u00d8\u00db")
        buf.write("\5.\30\2\u00d9\u00db\5\60\31\2\u00da\u00d6\3\2\2\2\u00da")
        buf.write("\u00d7\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00db)\3\2\2\2\u00dc\u00dd\7\b\2\2\u00dd\u00de\5\\/\2")
        buf.write("\u00de\u00df\7\60\2\2\u00df\u00e0\5^\60\2\u00e0\u00e1")
        buf.write("\7\t\2\2\u00e1+\3\2\2\2\u00e2\u00e3\7\n\2\2\u00e3\u00e4")
        buf.write("\5\\/\2\u00e4\u00e5\7\60\2\2\u00e5\u00e6\5^\60\2\u00e6")
        buf.write("\u00e7\7\60\2\2\u00e7\u00e8\5h\65\2\u00e8\u00e9\7\t\2")
        buf.write("\2\u00e9-\3\2\2\2\u00ea\u00eb\7\13\2\2\u00eb\u00ec\5\\")
        buf.write("/\2\u00ec\u00ed\7\60\2\2\u00ed\u00ee\5^\60\2\u00ee\u00ef")
        buf.write("\7\60\2\2\u00ef\u00f0\5h\65\2\u00f0\u00f1\7\t\2\2\u00f1")
        buf.write("/\3\2\2\2\u00f2\u00f3\7\f\2\2\u00f3\u00f4\5\\/\2\u00f4")
        buf.write("\u00f5\7\60\2\2\u00f5\u00f6\5^\60\2\u00f6\u00f7\7\60\2")
        buf.write("\2\u00f7\u00f8\5h\65\2\u00f8\u00f9\7\t\2\2\u00f9\61\3")
        buf.write("\2\2\2\u00fa\u00fb\7\r\2\2\u00fb\63\3\2\2\2\u00fc\u00fd")
        buf.write("\7\16\2\2\u00fd\u00fe\5\\/\2\u00fe\u00ff\7\60\2\2\u00ff")
        buf.write("\u0100\5h\65\2\u0100\u0101\7\60\2\2\u0101\u0102\5d\63")
        buf.write("\2\u0102\u0103\7\60\2\2\u0103\u0104\5f\64\2\u0104\u0105")
        buf.write("\7\t\2\2\u0105\65\3\2\2\2\u0106\u0107\7\17\2\2\u0107\u0108")
        buf.write("\5\\/\2\u0108\u0109\7\60\2\2\u0109\u010a\5`\61\2\u010a")
        buf.write("\u010b\7\60\2\2\u010b\u010c\5b\62\2\u010c\u010d\7\t\2")
        buf.write("\2\u010d\67\3\2\2\2\u010e\u010f\7\20\2\2\u010f\u0110\5")
        buf.write("\\/\2\u0110\u0111\7\t\2\2\u01119\3\2\2\2\u0112\u0117\5")
        buf.write("<\37\2\u0113\u0117\5> \2\u0114\u0117\5@!\2\u0115\u0117")
        buf.write("\5B\"\2\u0116\u0112\3\2\2\2\u0116\u0113\3\2\2\2\u0116")
        buf.write("\u0114\3\2\2\2\u0116\u0115\3\2\2\2\u0117;\3\2\2\2\u0118")
        buf.write("\u0119\7\21\2\2\u0119\u011a\5^\60\2\u011a\u011b\7\t\2")
        buf.write("\2\u011b=\3\2\2\2\u011c\u011d\7\22\2\2\u011d\u011e\5^")
        buf.write("\60\2\u011e\u011f\7\60\2\2\u011f\u0120\5h\65\2\u0120\u0121")
        buf.write("\7\t\2\2\u0121?\3\2\2\2\u0122\u0123\7\23\2\2\u0123\u0124")
        buf.write("\5^\60\2\u0124\u0125\7\60\2\2\u0125\u0126\5h\65\2\u0126")
        buf.write("\u0127\7\t\2\2\u0127A\3\2\2\2\u0128\u0129\7\24\2\2\u0129")
        buf.write("\u012a\5^\60\2\u012a\u012b\7\60\2\2\u012b\u012c\5h\65")
        buf.write("\2\u012c\u012d\7\t\2\2\u012dC\3\2\2\2\u012e\u012f\7\25")
        buf.write("\2\2\u012f\u0130\5\\/\2\u0130\u0131\7\60\2\2\u0131\u0132")
        buf.write("\5^\60\2\u0132\u0133\7\60\2\2\u0133\u0134\5`\61\2\u0134")
        buf.write("\u0135\7\t\2\2\u0135E\3\2\2\2\u0136\u0137\7\26\2\2\u0137")
        buf.write("\u0138\5Z.\2\u0138\u0139\7\60\2\2\u0139\u013a\5`\61\2")
        buf.write("\u013a\u013b\7\t\2\2\u013bG\3\2\2\2\u013c\u013d\7\27\2")
        buf.write("\2\u013d\u013e\5Z.\2\u013e\u013f\7\60\2\2\u013f\u0140")
        buf.write("\5n8\2\u0140\u0141\7\t\2\2\u0141I\3\2\2\2\u0142\u0147")
        buf.write("\5L\'\2\u0143\u0147\5N(\2\u0144\u0147\5P)\2\u0145\u0147")
        buf.write("\5R*\2\u0146\u0142\3\2\2\2\u0146\u0143\3\2\2\2\u0146\u0144")
        buf.write("\3\2\2\2\u0146\u0145\3\2\2\2\u0147K\3\2\2\2\u0148\u0149")
        buf.write("\7\30\2\2\u0149\u014a\5`\61\2\u014a\u014b\7\60\2\2\u014b")
        buf.write("\u014c\5b\62\2\u014c\u014d\7\t\2\2\u014dM\3\2\2\2\u014e")
        buf.write("\u014f\7\31\2\2\u014f\u0150\5`\61\2\u0150\u0151\7\60\2")
        buf.write("\2\u0151\u0152\5b\62\2\u0152\u0153\7\60\2\2\u0153\u0154")
        buf.write("\5h\65\2\u0154\u0155\7\t\2\2\u0155O\3\2\2\2\u0156\u0157")
        buf.write("\7\32\2\2\u0157\u0158\5`\61\2\u0158\u0159\7\60\2\2\u0159")
        buf.write("\u015a\5b\62\2\u015a\u015b\7\60\2\2\u015b\u015c\5h\65")
        buf.write("\2\u015c\u015d\7\t\2\2\u015dQ\3\2\2\2\u015e\u015f\7\33")
        buf.write("\2\2\u015f\u0160\5`\61\2\u0160\u0161\7\60\2\2\u0161\u0162")
        buf.write("\5b\62\2\u0162\u0163\7\60\2\2\u0163\u0164\5h\65\2\u0164")
        buf.write("\u0165\7\t\2\2\u0165S\3\2\2\2\u0166\u0167\7\34\2\2\u0167")
        buf.write("\u0168\5X-\2\u0168\u0169\7\t\2\2\u0169U\3\2\2\2\u016a")
        buf.write("\u016b\7\35\2\2\u016b\u016c\5p9\2\u016c\u016d\7\t\2\2")
        buf.write("\u016dW\3\2\2\2\u016e\u016f\5p9\2\u016fY\3\2\2\2\u0170")
        buf.write("\u0171\5p9\2\u0171[\3\2\2\2\u0172\u0173\5p9\2\u0173]\3")
        buf.write("\2\2\2\u0174\u0179\5r:\2\u0175\u0179\5t;\2\u0176\u0179")
        buf.write("\5v<\2\u0177\u0179\5p9\2\u0178\u0174\3\2\2\2\u0178\u0175")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("_\3\2\2\2\u017a\u017b\5p9\2\u017ba\3\2\2\2\u017c\u0181")
        buf.write("\5r:\2\u017d\u0181\5t;\2\u017e\u0181\5v<\2\u017f\u0181")
        buf.write("\5p9\2\u0180\u017c\3\2\2\2\u0180\u017d\3\2\2\2\u0180\u017e")
        buf.write("\3\2\2\2\u0180\u017f\3\2\2\2\u0181c\3\2\2\2\u0182\u0183")
        buf.write("\5p9\2\u0183e\3\2\2\2\u0184\u0185\5p9\2\u0185g\3\2\2\2")
        buf.write("\u0186\u0189\5j\66\2\u0187\u0189\5l\67\2\u0188\u0186\3")
        buf.write("\2\2\2\u0188\u0187\3\2\2\2\u0189i\3\2\2\2\u018a\u018b")
        buf.write("\t\2\2\2\u018bk\3\2\2\2\u018c\u018d\t\3\2\2\u018dm\3\2")
        buf.write("\2\2\u018e\u018f\t\4\2\2\u018fo\3\2\2\2\u0190\u0197\7")
        buf.write(")\2\2\u0191\u0192\7&\2\2\u0192\u0193\5p9\2\u0193\u0194")
        buf.write("\7\t\2\2\u0194\u0197\3\2\2\2\u0195\u0197\5n8\2\u0196\u0190")
        buf.write("\3\2\2\2\u0196\u0191\3\2\2\2\u0196\u0195\3\2\2\2\u0197")
        buf.write("\u0198\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199q\3\2\2\2\u019a\u019c\7.\2\2\u019b\u019a\3\2\2\2")
        buf.write("\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2\u019d\u019b\3")
        buf.write("\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\7\'\2\2\u01a0\u01a2")
        buf.write("\7.\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\3\2\2\2")
        buf.write("\u01a5\u01a7\7\'\2\2\u01a6\u01a8\7.\2\2\u01a7\u01a6\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01aas\3\2\2\2\u01ab\u01ac\7.\2\2\u01ac\u01ad")
        buf.write("\7.\2\2\u01ad\u01ae\7.\2\2\u01ae\u01af\7.\2\2\u01afu\3")
        buf.write("\2\2\2\u01b0\u01b1\t\5\2\2\u01b1w\3\2\2\2\31\177\u0092")
        buf.write("\u00a3\u00a6\u00b1\u00b3\u00b5\u00ba\u00bd\u00c1\u00c4")
        buf.write("\u00d0\u00da\u0116\u0146\u0178\u0180\u0188\u0196\u0198")
        buf.write("\u019d\u01a3\u01a9")
        return buf.getvalue()


class ProgramParser ( Parser ):

    grammarFileName = "Program.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'What()'", "'Count()'", "'FindAll()'", 
                     "'And()'", "'Or()'", "'FilterStr('", "')'", "'FilterNum('", 
                     "'FilterYear('", "'FilterDate('", "'QueryRelation()'", 
                     "'Select('", "'QueryAttrUnderCondition('", "'QueryAttr('", 
                     "'VerifyStr('", "'VerifyNum('", "'VerifyYear('", "'VerifyDate('", 
                     "'QueryAttrQualifier('", "'QueryRelationQualifier('", 
                     "'Relate('", "'QFilterStr('", "'QFilterNum('", "'QFilterYear('", 
                     "'QFilterDate('", "'FilterConcept('", "'Find('", "'='", 
                     "'<'", "'>'", "'!='", "'largest'", "'smallest'", "'forward'", 
                     "'backward'", "'('", "'-'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<b>'", "'<c>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WS", "STRING_LITERAL", 
                      "INTEGER", "DECIMAL", "DOUBLE", "EXPONENT", "DIGIT", 
                      "FUNC_SEP", "IN_FUNC_SEP" ]

    RULE_query = 0
    RULE_whatEntityQuery = 1
    RULE_howManyEntityQuery = 2
    RULE_whatAttributeQuery = 3
    RULE_whatRelationQuery = 4
    RULE_attributeSatisfyQuery = 5
    RULE_whatAttributeQualifierQuery = 6
    RULE_whatRelationQualifierQuery = 7
    RULE_entitySetGroup = 8
    RULE_entitySet = 9
    RULE_entityFilterByRelation = 10
    RULE_entityFilterByAttribute = 11
    RULE_entityFilterByConcept = 12
    RULE_queryName = 13
    RULE_count = 14
    RULE_findAll = 15
    RULE_setOP = 16
    RULE_intersect = 17
    RULE_union = 18
    RULE_filterAttr = 19
    RULE_filterStr = 20
    RULE_filterNum = 21
    RULE_filterYear = 22
    RULE_filterDate = 23
    RULE_queryRelation = 24
    RULE_select = 25
    RULE_queryAttributeUnderCondition = 26
    RULE_queryAttribute = 27
    RULE_verify = 28
    RULE_verifyStr = 29
    RULE_verifyNum = 30
    RULE_verifyYear = 31
    RULE_verifyDate = 32
    RULE_queryAttrQualifier = 33
    RULE_queryRelationQualifier = 34
    RULE_relate = 35
    RULE_filterQualifier = 36
    RULE_filterStrQualifier = 37
    RULE_filterNumQualifier = 38
    RULE_filterYearQualifier = 39
    RULE_filterDateQualifier = 40
    RULE_filterConcept = 41
    RULE_entity = 42
    RULE_concept = 43
    RULE_predicate = 44
    RULE_key = 45
    RULE_value = 46
    RULE_qkey = 47
    RULE_qvalue = 48
    RULE_topk = 49
    RULE_start = 50
    RULE_op = 51
    RULE_symbolOP = 52
    RULE_stringOP = 53
    RULE_direction = 54
    RULE_string = 55
    RULE_date = 56
    RULE_year = 57
    RULE_number = 58

    ruleNames =  [ "query", "whatEntityQuery", "howManyEntityQuery", "whatAttributeQuery", 
                   "whatRelationQuery", "attributeSatisfyQuery", "whatAttributeQualifierQuery", 
                   "whatRelationQualifierQuery", "entitySetGroup", "entitySet", 
                   "entityFilterByRelation", "entityFilterByAttribute", 
                   "entityFilterByConcept", "queryName", "count", "findAll", 
                   "setOP", "intersect", "union", "filterAttr", "filterStr", 
                   "filterNum", "filterYear", "filterDate", "queryRelation", 
                   "select", "queryAttributeUnderCondition", "queryAttribute", 
                   "verify", "verifyStr", "verifyNum", "verifyYear", "verifyDate", 
                   "queryAttrQualifier", "queryRelationQualifier", "relate", 
                   "filterQualifier", "filterStrQualifier", "filterNumQualifier", 
                   "filterYearQualifier", "filterDateQualifier", "filterConcept", 
                   "entity", "concept", "predicate", "key", "value", "qkey", 
                   "qvalue", "topk", "start", "op", "symbolOP", "stringOP", 
                   "direction", "string", "date", "year", "number" ]

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
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    WS=38
    STRING_LITERAL=39
    INTEGER=40
    DECIMAL=41
    DOUBLE=42
    EXPONENT=43
    DIGIT=44
    FUNC_SEP=45
    IN_FUNC_SEP=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ProgramParser.EOF, 0)

        def whatEntityQuery(self):
            return self.getTypedRuleContext(ProgramParser.WhatEntityQueryContext,0)


        def howManyEntityQuery(self):
            return self.getTypedRuleContext(ProgramParser.HowManyEntityQueryContext,0)


        def whatAttributeQuery(self):
            return self.getTypedRuleContext(ProgramParser.WhatAttributeQueryContext,0)


        def whatRelationQuery(self):
            return self.getTypedRuleContext(ProgramParser.WhatRelationQueryContext,0)


        def attributeSatisfyQuery(self):
            return self.getTypedRuleContext(ProgramParser.AttributeSatisfyQueryContext,0)


        def whatAttributeQualifierQuery(self):
            return self.getTypedRuleContext(ProgramParser.WhatAttributeQualifierQueryContext,0)


        def whatRelationQualifierQuery(self):
            return self.getTypedRuleContext(ProgramParser.WhatRelationQualifierQueryContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = ProgramParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 118
                self.whatEntityQuery()
                pass

            elif la_ == 2:
                self.state = 119
                self.howManyEntityQuery()
                pass

            elif la_ == 3:
                self.state = 120
                self.whatAttributeQuery()
                pass

            elif la_ == 4:
                self.state = 121
                self.whatRelationQuery()
                pass

            elif la_ == 5:
                self.state = 122
                self.attributeSatisfyQuery()
                pass

            elif la_ == 6:
                self.state = 123
                self.whatAttributeQualifierQuery()
                pass

            elif la_ == 7:
                self.state = 124
                self.whatRelationQualifierQuery()
                pass


            self.state = 127
            self.match(ProgramParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhatEntityQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySet(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetContext,0)


        def queryName(self):
            return self.getTypedRuleContext(ProgramParser.QueryNameContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_whatEntityQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhatEntityQuery" ):
                listener.enterWhatEntityQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhatEntityQuery" ):
                listener.exitWhatEntityQuery(self)




    def whatEntityQuery(self):

        localctx = ProgramParser.WhatEntityQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_whatEntityQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.entitySet(0)
            self.state = 130
            self.queryName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HowManyEntityQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySet(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetContext,0)


        def count(self):
            return self.getTypedRuleContext(ProgramParser.CountContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_howManyEntityQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHowManyEntityQuery" ):
                listener.enterHowManyEntityQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHowManyEntityQuery" ):
                listener.exitHowManyEntityQuery(self)




    def howManyEntityQuery(self):

        localctx = ProgramParser.HowManyEntityQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_howManyEntityQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.entitySet(0)
            self.state = 133
            self.count()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhatAttributeQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySet(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetContext,0)


        def queryAttribute(self):
            return self.getTypedRuleContext(ProgramParser.QueryAttributeContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_whatAttributeQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhatAttributeQuery" ):
                listener.enterWhatAttributeQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhatAttributeQuery" ):
                listener.exitWhatAttributeQuery(self)




    def whatAttributeQuery(self):

        localctx = ProgramParser.WhatAttributeQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whatAttributeQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.entitySet(0)
            self.state = 136
            self.queryAttribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhatRelationQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySetGroup(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetGroupContext,0)


        def queryRelation(self):
            return self.getTypedRuleContext(ProgramParser.QueryRelationContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_whatRelationQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhatRelationQuery" ):
                listener.enterWhatRelationQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhatRelationQuery" ):
                listener.exitWhatRelationQuery(self)




    def whatRelationQuery(self):

        localctx = ProgramParser.WhatRelationQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whatRelationQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.entitySetGroup()
            self.state = 139
            self.queryRelation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeSatisfyQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySet(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetContext,0)


        def verify(self):
            return self.getTypedRuleContext(ProgramParser.VerifyContext,0)


        def queryAttributeUnderCondition(self):
            return self.getTypedRuleContext(ProgramParser.QueryAttributeUnderConditionContext,0)


        def queryAttribute(self):
            return self.getTypedRuleContext(ProgramParser.QueryAttributeContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_attributeSatisfyQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeSatisfyQuery" ):
                listener.enterAttributeSatisfyQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeSatisfyQuery" ):
                listener.exitAttributeSatisfyQuery(self)




    def attributeSatisfyQuery(self):

        localctx = ProgramParser.AttributeSatisfyQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributeSatisfyQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.entitySet(0)
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProgramParser.T__12]:
                self.state = 142
                self.queryAttributeUnderCondition()
                pass
            elif token in [ProgramParser.T__13]:
                self.state = 143
                self.queryAttribute()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 146
            self.verify()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhatAttributeQualifierQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySet(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetContext,0)


        def queryAttrQualifier(self):
            return self.getTypedRuleContext(ProgramParser.QueryAttrQualifierContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_whatAttributeQualifierQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhatAttributeQualifierQuery" ):
                listener.enterWhatAttributeQualifierQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhatAttributeQualifierQuery" ):
                listener.exitWhatAttributeQualifierQuery(self)




    def whatAttributeQualifierQuery(self):

        localctx = ProgramParser.WhatAttributeQualifierQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whatAttributeQualifierQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.entitySet(0)
            self.state = 149
            self.queryAttrQualifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhatRelationQualifierQueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySetGroup(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetGroupContext,0)


        def queryRelationQualifier(self):
            return self.getTypedRuleContext(ProgramParser.QueryRelationQualifierContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_whatRelationQualifierQuery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhatRelationQualifierQuery" ):
                listener.enterWhatRelationQualifierQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhatRelationQualifierQuery" ):
                listener.exitWhatRelationQualifierQuery(self)




    def whatRelationQualifierQuery(self):

        localctx = ProgramParser.WhatRelationQualifierQueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whatRelationQualifierQuery)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.entitySetGroup()
            self.state = 152
            self.queryRelationQualifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntitySetGroupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def entitySet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.EntitySetContext)
            else:
                return self.getTypedRuleContext(ProgramParser.EntitySetContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_entitySetGroup

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitySetGroup" ):
                listener.enterEntitySetGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitySetGroup" ):
                listener.exitEntitySetGroup(self)




    def entitySetGroup(self):

        localctx = ProgramParser.EntitySetGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_entitySetGroup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.entitySet(0)
            self.state = 155
            self.entitySet(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntitySetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_entitySet

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EntitySetByFilterContext(EntitySetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramParser.EntitySetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def findAll(self):
            return self.getTypedRuleContext(ProgramParser.FindAllContext,0)

        def entityFilterByAttribute(self):
            return self.getTypedRuleContext(ProgramParser.EntityFilterByAttributeContext,0)

        def entityFilterByConcept(self):
            return self.getTypedRuleContext(ProgramParser.EntityFilterByConceptContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitySetByFilter" ):
                listener.enterEntitySetByFilter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitySetByFilter" ):
                listener.exitEntitySetByFilter(self)


    class EntitySetAtomContext(EntitySetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramParser.EntitySetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def entity(self):
            return self.getTypedRuleContext(ProgramParser.EntityContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitySetAtom" ):
                listener.enterEntitySetAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitySetAtom" ):
                listener.exitEntitySetAtom(self)


    class EntitySetByRankContext(EntitySetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramParser.EntitySetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def entitySet(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetContext,0)

        def select(self):
            return self.getTypedRuleContext(ProgramParser.SelectContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitySetByRank" ):
                listener.enterEntitySetByRank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitySetByRank" ):
                listener.exitEntitySetByRank(self)


    class EntitySetByOPContext(EntitySetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramParser.EntitySetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def entitySet(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.EntitySetContext)
            else:
                return self.getTypedRuleContext(ProgramParser.EntitySetContext,i)

        def setOP(self):
            return self.getTypedRuleContext(ProgramParser.SetOPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitySetByOP" ):
                listener.enterEntitySetByOP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitySetByOP" ):
                listener.exitEntitySetByOP(self)


    class EntitySetNestedContext(EntitySetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramParser.EntitySetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def entitySet(self):
            return self.getTypedRuleContext(ProgramParser.EntitySetContext,0)

        def entityFilterByRelation(self):
            return self.getTypedRuleContext(ProgramParser.EntityFilterByRelationContext,0)

        def entityFilterByAttribute(self):
            return self.getTypedRuleContext(ProgramParser.EntityFilterByAttributeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntitySetNested" ):
                listener.enterEntitySetNested(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntitySetNested" ):
                listener.exitEntitySetNested(self)



    def entitySet(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ProgramParser.EntitySetContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_entitySet, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProgramParser.T__2]:
                localctx = ProgramParser.EntitySetByFilterContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 158
                self.findAll()
                self.state = 161
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ProgramParser.T__5, ProgramParser.T__7, ProgramParser.T__8, ProgramParser.T__9]:
                    self.state = 159
                    self.entityFilterByAttribute()
                    pass
                elif token in [ProgramParser.T__25]:
                    self.state = 160
                    self.entityFilterByConcept()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [ProgramParser.T__26]:
                localctx = ProgramParser.EntitySetAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.entity()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 177
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = ProgramParser.EntitySetByOPContext(self, ProgramParser.EntitySetContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_entitySet)
                        self.state = 166
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 167
                        self.entitySet(0)
                        self.state = 168
                        self.setOP()
                        pass

                    elif la_ == 2:
                        localctx = ProgramParser.EntitySetByRankContext(self, ProgramParser.EntitySetContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_entitySet)
                        self.state = 170
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 171
                        self.select()
                        pass

                    elif la_ == 3:
                        localctx = ProgramParser.EntitySetNestedContext(self, ProgramParser.EntitySetContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_entitySet)
                        self.state = 172
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 175
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [ProgramParser.T__20]:
                            self.state = 173
                            self.entityFilterByRelation()
                            pass
                        elif token in [ProgramParser.T__5, ProgramParser.T__7, ProgramParser.T__8, ProgramParser.T__9]:
                            self.state = 174
                            self.entityFilterByAttribute()
                            pass
                        else:
                            raise NoViableAltException(self)

                        pass

             
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EntityFilterByRelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relate(self):
            return self.getTypedRuleContext(ProgramParser.RelateContext,0)


        def filterQualifier(self):
            return self.getTypedRuleContext(ProgramParser.FilterQualifierContext,0)


        def filterConcept(self):
            return self.getTypedRuleContext(ProgramParser.FilterConceptContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_entityFilterByRelation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityFilterByRelation" ):
                listener.enterEntityFilterByRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityFilterByRelation" ):
                listener.exitEntityFilterByRelation(self)




    def entityFilterByRelation(self):

        localctx = ProgramParser.EntityFilterByRelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_entityFilterByRelation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.relate()
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 183
                self.filterQualifier()


            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 186
                self.filterConcept()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityFilterByAttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterAttr(self):
            return self.getTypedRuleContext(ProgramParser.FilterAttrContext,0)


        def filterQualifier(self):
            return self.getTypedRuleContext(ProgramParser.FilterQualifierContext,0)


        def filterConcept(self):
            return self.getTypedRuleContext(ProgramParser.FilterConceptContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_entityFilterByAttribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityFilterByAttribute" ):
                listener.enterEntityFilterByAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityFilterByAttribute" ):
                listener.exitEntityFilterByAttribute(self)




    def entityFilterByAttribute(self):

        localctx = ProgramParser.EntityFilterByAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_entityFilterByAttribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.filterAttr()
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 190
                self.filterQualifier()


            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 193
                self.filterConcept()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityFilterByConceptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterConcept(self):
            return self.getTypedRuleContext(ProgramParser.FilterConceptContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_entityFilterByConcept

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityFilterByConcept" ):
                listener.enterEntityFilterByConcept(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityFilterByConcept" ):
                listener.exitEntityFilterByConcept(self)




    def entityFilterByConcept(self):

        localctx = ProgramParser.EntityFilterByConceptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_entityFilterByConcept)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.filterConcept()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_queryName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryName" ):
                listener.enterQueryName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryName" ):
                listener.exitQueryName(self)




    def queryName(self):

        localctx = ProgramParser.QueryNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_queryName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(ProgramParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_count

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCount" ):
                listener.enterCount(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCount" ):
                listener.exitCount(self)




    def count(self):

        localctx = ProgramParser.CountContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_count)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ProgramParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FindAllContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_findAll

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFindAll" ):
                listener.enterFindAll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFindAll" ):
                listener.exitFindAll(self)




    def findAll(self):

        localctx = ProgramParser.FindAllContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_findAll)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(ProgramParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetOPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intersect(self):
            return self.getTypedRuleContext(ProgramParser.IntersectContext,0)


        def union(self):
            return self.getTypedRuleContext(ProgramParser.UnionContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_setOP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetOP" ):
                listener.enterSetOP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetOP" ):
                listener.exitSetOP(self)




    def setOP(self):

        localctx = ProgramParser.SetOPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_setOP)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProgramParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.intersect()
                pass
            elif token in [ProgramParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.union()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntersectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_intersect

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AndContext(IntersectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramParser.IntersectContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)



    def intersect(self):

        localctx = ProgramParser.IntersectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_intersect)
        try:
            localctx = ProgramParser.AndContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(ProgramParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_union

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OrContext(UnionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ProgramParser.UnionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)



    def union(self):

        localctx = ProgramParser.UnionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_union)
        try:
            localctx = ProgramParser.OrContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ProgramParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterAttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterStr(self):
            return self.getTypedRuleContext(ProgramParser.FilterStrContext,0)


        def filterNum(self):
            return self.getTypedRuleContext(ProgramParser.FilterNumContext,0)


        def filterYear(self):
            return self.getTypedRuleContext(ProgramParser.FilterYearContext,0)


        def filterDate(self):
            return self.getTypedRuleContext(ProgramParser.FilterDateContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterAttr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterAttr" ):
                listener.enterFilterAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterAttr" ):
                listener.exitFilterAttr(self)




    def filterAttr(self):

        localctx = ProgramParser.FilterAttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_filterAttr)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProgramParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.filterStr()
                pass
            elif token in [ProgramParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.filterNum()
                pass
            elif token in [ProgramParser.T__8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.filterYear()
                pass
            elif token in [ProgramParser.T__9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 215
                self.filterDate()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ProgramParser.KeyContext,0)


        def IN_FUNC_SEP(self):
            return self.getToken(ProgramParser.IN_FUNC_SEP, 0)

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterStr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStr" ):
                listener.enterFilterStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStr" ):
                listener.exitFilterStr(self)




    def filterStr(self):

        localctx = ProgramParser.FilterStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_filterStr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ProgramParser.T__5)
            self.state = 219
            self.key()
            self.state = 220
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 221
            self.value()
            self.state = 222
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterNumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ProgramParser.KeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterNum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterNum" ):
                listener.enterFilterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterNum" ):
                listener.exitFilterNum(self)




    def filterNum(self):

        localctx = ProgramParser.FilterNumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_filterNum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(ProgramParser.T__7)
            self.state = 225
            self.key()
            self.state = 226
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 227
            self.value()
            self.state = 228
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 229
            self.op()
            self.state = 230
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterYearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ProgramParser.KeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterYear

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterYear" ):
                listener.enterFilterYear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterYear" ):
                listener.exitFilterYear(self)




    def filterYear(self):

        localctx = ProgramParser.FilterYearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_filterYear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(ProgramParser.T__8)
            self.state = 233
            self.key()
            self.state = 234
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 235
            self.value()
            self.state = 236
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 237
            self.op()
            self.state = 238
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterDateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ProgramParser.KeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterDate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterDate" ):
                listener.enterFilterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterDate" ):
                listener.exitFilterDate(self)




    def filterDate(self):

        localctx = ProgramParser.FilterDateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_filterDate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(ProgramParser.T__9)
            self.state = 241
            self.key()
            self.state = 242
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 243
            self.value()
            self.state = 244
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 245
            self.op()
            self.state = 246
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryRelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_queryRelation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryRelation" ):
                listener.enterQueryRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryRelation" ):
                listener.exitQueryRelation(self)




    def queryRelation(self):

        localctx = ProgramParser.QueryRelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_queryRelation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(ProgramParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ProgramParser.KeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def topk(self):
            return self.getTypedRuleContext(ProgramParser.TopkContext,0)


        def start(self):
            return self.getTypedRuleContext(ProgramParser.StartContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)




    def select(self):

        localctx = ProgramParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_select)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(ProgramParser.T__11)
            self.state = 251
            self.key()
            self.state = 252
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 253
            self.op()
            self.state = 254
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 255
            self.topk()
            self.state = 256
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 257
            self.start()
            self.state = 258
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryAttributeUnderConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ProgramParser.KeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def qkey(self):
            return self.getTypedRuleContext(ProgramParser.QkeyContext,0)


        def qvalue(self):
            return self.getTypedRuleContext(ProgramParser.QvalueContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_queryAttributeUnderCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryAttributeUnderCondition" ):
                listener.enterQueryAttributeUnderCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryAttributeUnderCondition" ):
                listener.exitQueryAttributeUnderCondition(self)




    def queryAttributeUnderCondition(self):

        localctx = ProgramParser.QueryAttributeUnderConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_queryAttributeUnderCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(ProgramParser.T__12)
            self.state = 261
            self.key()
            self.state = 262
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 263
            self.qkey()
            self.state = 264
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 265
            self.qvalue()
            self.state = 266
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryAttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ProgramParser.KeyContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_queryAttribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryAttribute" ):
                listener.enterQueryAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryAttribute" ):
                listener.exitQueryAttribute(self)




    def queryAttribute(self):

        localctx = ProgramParser.QueryAttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_queryAttribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(ProgramParser.T__13)
            self.state = 269
            self.key()
            self.state = 270
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerifyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verifyStr(self):
            return self.getTypedRuleContext(ProgramParser.VerifyStrContext,0)


        def verifyNum(self):
            return self.getTypedRuleContext(ProgramParser.VerifyNumContext,0)


        def verifyYear(self):
            return self.getTypedRuleContext(ProgramParser.VerifyYearContext,0)


        def verifyDate(self):
            return self.getTypedRuleContext(ProgramParser.VerifyDateContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_verify

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerify" ):
                listener.enterVerify(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerify" ):
                listener.exitVerify(self)




    def verify(self):

        localctx = ProgramParser.VerifyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_verify)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProgramParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.verifyStr()
                pass
            elif token in [ProgramParser.T__15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.verifyNum()
                pass
            elif token in [ProgramParser.T__16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 274
                self.verifyYear()
                pass
            elif token in [ProgramParser.T__17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 275
                self.verifyDate()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerifyStrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_verifyStr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerifyStr" ):
                listener.enterVerifyStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerifyStr" ):
                listener.exitVerifyStr(self)




    def verifyStr(self):

        localctx = ProgramParser.VerifyStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_verifyStr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ProgramParser.T__14)
            self.state = 279
            self.value()
            self.state = 280
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerifyNumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def IN_FUNC_SEP(self):
            return self.getToken(ProgramParser.IN_FUNC_SEP, 0)

        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_verifyNum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerifyNum" ):
                listener.enterVerifyNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerifyNum" ):
                listener.exitVerifyNum(self)




    def verifyNum(self):

        localctx = ProgramParser.VerifyNumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_verifyNum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(ProgramParser.T__15)
            self.state = 283
            self.value()
            self.state = 284
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 285
            self.op()
            self.state = 286
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerifyYearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def IN_FUNC_SEP(self):
            return self.getToken(ProgramParser.IN_FUNC_SEP, 0)

        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_verifyYear

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerifyYear" ):
                listener.enterVerifyYear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerifyYear" ):
                listener.exitVerifyYear(self)




    def verifyYear(self):

        localctx = ProgramParser.VerifyYearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_verifyYear)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ProgramParser.T__16)
            self.state = 289
            self.value()
            self.state = 290
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 291
            self.op()
            self.state = 292
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerifyDateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def IN_FUNC_SEP(self):
            return self.getToken(ProgramParser.IN_FUNC_SEP, 0)

        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_verifyDate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerifyDate" ):
                listener.enterVerifyDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerifyDate" ):
                listener.exitVerifyDate(self)




    def verifyDate(self):

        localctx = ProgramParser.VerifyDateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_verifyDate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ProgramParser.T__17)
            self.state = 295
            self.value()
            self.state = 296
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 297
            self.op()
            self.state = 298
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryAttrQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def key(self):
            return self.getTypedRuleContext(ProgramParser.KeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def value(self):
            return self.getTypedRuleContext(ProgramParser.ValueContext,0)


        def qkey(self):
            return self.getTypedRuleContext(ProgramParser.QkeyContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_queryAttrQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryAttrQualifier" ):
                listener.enterQueryAttrQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryAttrQualifier" ):
                listener.exitQueryAttrQualifier(self)




    def queryAttrQualifier(self):

        localctx = ProgramParser.QueryAttrQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_queryAttrQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(ProgramParser.T__18)
            self.state = 301
            self.key()
            self.state = 302
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 303
            self.value()
            self.state = 304
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 305
            self.qkey()
            self.state = 306
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryRelationQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(ProgramParser.PredicateContext,0)


        def IN_FUNC_SEP(self):
            return self.getToken(ProgramParser.IN_FUNC_SEP, 0)

        def qkey(self):
            return self.getTypedRuleContext(ProgramParser.QkeyContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_queryRelationQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryRelationQualifier" ):
                listener.enterQueryRelationQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryRelationQualifier" ):
                listener.exitQueryRelationQualifier(self)




    def queryRelationQualifier(self):

        localctx = ProgramParser.QueryRelationQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_queryRelationQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ProgramParser.T__19)
            self.state = 309
            self.predicate()
            self.state = 310
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 311
            self.qkey()
            self.state = 312
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self):
            return self.getTypedRuleContext(ProgramParser.PredicateContext,0)


        def IN_FUNC_SEP(self):
            return self.getToken(ProgramParser.IN_FUNC_SEP, 0)

        def direction(self):
            return self.getTypedRuleContext(ProgramParser.DirectionContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_relate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelate" ):
                listener.enterRelate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelate" ):
                listener.exitRelate(self)




    def relate(self):

        localctx = ProgramParser.RelateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_relate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(ProgramParser.T__20)
            self.state = 315
            self.predicate()
            self.state = 316
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 317
            self.direction()
            self.state = 318
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterStrQualifier(self):
            return self.getTypedRuleContext(ProgramParser.FilterStrQualifierContext,0)


        def filterNumQualifier(self):
            return self.getTypedRuleContext(ProgramParser.FilterNumQualifierContext,0)


        def filterYearQualifier(self):
            return self.getTypedRuleContext(ProgramParser.FilterYearQualifierContext,0)


        def filterDateQualifier(self):
            return self.getTypedRuleContext(ProgramParser.FilterDateQualifierContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterQualifier" ):
                listener.enterFilterQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterQualifier" ):
                listener.exitFilterQualifier(self)




    def filterQualifier(self):

        localctx = ProgramParser.FilterQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_filterQualifier)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProgramParser.T__21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.filterStrQualifier()
                pass
            elif token in [ProgramParser.T__22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.filterNumQualifier()
                pass
            elif token in [ProgramParser.T__23]:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.filterYearQualifier()
                pass
            elif token in [ProgramParser.T__24]:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.filterDateQualifier()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStrQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qkey(self):
            return self.getTypedRuleContext(ProgramParser.QkeyContext,0)


        def IN_FUNC_SEP(self):
            return self.getToken(ProgramParser.IN_FUNC_SEP, 0)

        def qvalue(self):
            return self.getTypedRuleContext(ProgramParser.QvalueContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterStrQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStrQualifier" ):
                listener.enterFilterStrQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStrQualifier" ):
                listener.exitFilterStrQualifier(self)




    def filterStrQualifier(self):

        localctx = ProgramParser.FilterStrQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_filterStrQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(ProgramParser.T__21)
            self.state = 327
            self.qkey()
            self.state = 328
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 329
            self.qvalue()
            self.state = 330
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterNumQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qkey(self):
            return self.getTypedRuleContext(ProgramParser.QkeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def qvalue(self):
            return self.getTypedRuleContext(ProgramParser.QvalueContext,0)


        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterNumQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterNumQualifier" ):
                listener.enterFilterNumQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterNumQualifier" ):
                listener.exitFilterNumQualifier(self)




    def filterNumQualifier(self):

        localctx = ProgramParser.FilterNumQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_filterNumQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(ProgramParser.T__22)
            self.state = 333
            self.qkey()
            self.state = 334
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 335
            self.qvalue()
            self.state = 336
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 337
            self.op()
            self.state = 338
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterYearQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qkey(self):
            return self.getTypedRuleContext(ProgramParser.QkeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def qvalue(self):
            return self.getTypedRuleContext(ProgramParser.QvalueContext,0)


        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterYearQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterYearQualifier" ):
                listener.enterFilterYearQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterYearQualifier" ):
                listener.exitFilterYearQualifier(self)




    def filterYearQualifier(self):

        localctx = ProgramParser.FilterYearQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_filterYearQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(ProgramParser.T__23)
            self.state = 341
            self.qkey()
            self.state = 342
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 343
            self.qvalue()
            self.state = 344
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 345
            self.op()
            self.state = 346
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterDateQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qkey(self):
            return self.getTypedRuleContext(ProgramParser.QkeyContext,0)


        def IN_FUNC_SEP(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.IN_FUNC_SEP)
            else:
                return self.getToken(ProgramParser.IN_FUNC_SEP, i)

        def qvalue(self):
            return self.getTypedRuleContext(ProgramParser.QvalueContext,0)


        def op(self):
            return self.getTypedRuleContext(ProgramParser.OpContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterDateQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterDateQualifier" ):
                listener.enterFilterDateQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterDateQualifier" ):
                listener.exitFilterDateQualifier(self)




    def filterDateQualifier(self):

        localctx = ProgramParser.FilterDateQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_filterDateQualifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(ProgramParser.T__24)
            self.state = 349
            self.qkey()
            self.state = 350
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 351
            self.qvalue()
            self.state = 352
            self.match(ProgramParser.IN_FUNC_SEP)
            self.state = 353
            self.op()
            self.state = 354
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterConceptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concept(self):
            return self.getTypedRuleContext(ProgramParser.ConceptContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_filterConcept

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterConcept" ):
                listener.enterFilterConcept(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterConcept" ):
                listener.exitFilterConcept(self)




    def filterConcept(self):

        localctx = ProgramParser.FilterConceptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_filterConcept)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ProgramParser.T__25)
            self.state = 357
            self.concept()
            self.state = 358
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)




    def entity(self):

        localctx = ProgramParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_entity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(ProgramParser.T__26)
            self.state = 361
            self.string()
            self.state = 362
            self.match(ProgramParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConceptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_concept

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcept" ):
                listener.enterConcept(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcept" ):
                listener.exitConcept(self)




    def concept(self):

        localctx = ProgramParser.ConceptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_concept)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = ProgramParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKey" ):
                listener.enterKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKey" ):
                listener.exitKey(self)




    def key(self):

        localctx = ProgramParser.KeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def date(self):
            return self.getTypedRuleContext(ProgramParser.DateContext,0)


        def year(self):
            return self.getTypedRuleContext(ProgramParser.YearContext,0)


        def number(self):
            return self.getTypedRuleContext(ProgramParser.NumberContext,0)


        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ProgramParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_value)
        try:
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.date()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.year()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                self.number()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 373
                self.string()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QkeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_qkey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQkey" ):
                listener.enterQkey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQkey" ):
                listener.exitQkey(self)




    def qkey(self):

        localctx = ProgramParser.QkeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_qkey)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def date(self):
            return self.getTypedRuleContext(ProgramParser.DateContext,0)


        def year(self):
            return self.getTypedRuleContext(ProgramParser.YearContext,0)


        def number(self):
            return self.getTypedRuleContext(ProgramParser.NumberContext,0)


        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_qvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQvalue" ):
                listener.enterQvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQvalue" ):
                listener.exitQvalue(self)




    def qvalue(self):

        localctx = ProgramParser.QvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_qvalue)
        try:
            self.state = 382
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.date()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.year()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 380
                self.number()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 381
                self.string()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_topk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopk" ):
                listener.enterTopk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopk" ):
                listener.exitTopk(self)




    def topk(self):

        localctx = ProgramParser.TopkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_topk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(ProgramParser.StringContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = ProgramParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbolOP(self):
            return self.getTypedRuleContext(ProgramParser.SymbolOPContext,0)


        def stringOP(self):
            return self.getTypedRuleContext(ProgramParser.StringOPContext,0)


        def getRuleIndex(self):
            return ProgramParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = ProgramParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_op)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ProgramParser.T__27, ProgramParser.T__28, ProgramParser.T__29, ProgramParser.T__30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.symbolOP()
                pass
            elif token in [ProgramParser.T__31, ProgramParser.T__32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.stringOP()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolOPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_symbolOP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbolOP" ):
                listener.enterSymbolOP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbolOP" ):
                listener.exitSymbolOP(self)




    def symbolOP(self):

        localctx = ProgramParser.SymbolOPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_symbolOP)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ProgramParser.T__27) | (1 << ProgramParser.T__28) | (1 << ProgramParser.T__29) | (1 << ProgramParser.T__30))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringOPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_stringOP

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringOP" ):
                listener.enterStringOP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringOP" ):
                listener.exitStringOP(self)




    def stringOP(self):

        localctx = ProgramParser.StringOPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_stringOP)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            _la = self._input.LA(1)
            if not(_la==ProgramParser.T__31 or _la==ProgramParser.T__32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProgramParser.RULE_direction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirection" ):
                listener.enterDirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirection" ):
                listener.exitDirection(self)




    def direction(self):

        localctx = ProgramParser.DirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_direction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            _la = self._input.LA(1)
            if not(_la==ProgramParser.T__33 or _la==ProgramParser.T__34):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
                return self.getTokens(ProgramParser.STRING_LITERAL)
            else:
                return self.getToken(ProgramParser.STRING_LITERAL, i)

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.StringContext)
            else:
                return self.getTypedRuleContext(ProgramParser.StringContext,i)


        def direction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProgramParser.DirectionContext)
            else:
                return self.getTypedRuleContext(ProgramParser.DirectionContext,i)


        def getRuleIndex(self):
            return ProgramParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = ProgramParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 404
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ProgramParser.STRING_LITERAL]:
                    self.state = 398
                    self.match(ProgramParser.STRING_LITERAL)
                    pass
                elif token in [ProgramParser.T__35]:
                    self.state = 399
                    self.match(ProgramParser.T__35)
                    self.state = 400
                    self.string()
                    self.state = 401
                    self.match(ProgramParser.T__6)
                    pass
                elif token in [ProgramParser.T__33, ProgramParser.T__34]:
                    self.state = 403
                    self.direction()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 406 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ProgramParser.T__33) | (1 << ProgramParser.T__34) | (1 << ProgramParser.T__35) | (1 << ProgramParser.STRING_LITERAL))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.DIGIT)
            else:
                return self.getToken(ProgramParser.DIGIT, i)

        def getRuleIndex(self):
            return ProgramParser.RULE_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)




    def date(self):

        localctx = ProgramParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 408
                    self.match(ProgramParser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 411 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 413
            self.match(ProgramParser.T__36)
            self.state = 415 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 414
                    self.match(ProgramParser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 417 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 419
            self.match(ProgramParser.T__36)
            self.state = 421 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 420
                    self.match(ProgramParser.DIGIT)

                else:
                    raise NoViableAltException(self)
                self.state = 423 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YearContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ProgramParser.DIGIT)
            else:
                return self.getToken(ProgramParser.DIGIT, i)

        def getRuleIndex(self):
            return ProgramParser.RULE_year

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYear" ):
                listener.enterYear(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYear" ):
                listener.exitYear(self)




    def year(self):

        localctx = ProgramParser.YearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_year)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(ProgramParser.DIGIT)
            self.state = 426
            self.match(ProgramParser.DIGIT)
            self.state = 427
            self.match(ProgramParser.DIGIT)
            self.state = 428
            self.match(ProgramParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ProgramParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(ProgramParser.DECIMAL, 0)

        def DOUBLE(self):
            return self.getToken(ProgramParser.DOUBLE, 0)

        def getRuleIndex(self):
            return ProgramParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = ProgramParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ProgramParser.INTEGER) | (1 << ProgramParser.DECIMAL) | (1 << ProgramParser.DOUBLE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.entitySet_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def entitySet_sempred(self, localctx:EntitySetContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




