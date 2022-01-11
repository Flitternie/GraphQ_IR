# Generated from ./parser/overnight/Overnight.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(")
        buf.write("\u01ad\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3p\n\3\3\4")
        buf.write("\5\4s\n\4\3\4\3\4\3\4\3\4\3\4\5\4z\n\4\3\5\5\5}\n\5\3")
        buf.write("\5\3\5\3\5\5\5\u0082\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0093\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u009f\n\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\5\t\u00b6\n\t\3\t\5\t\u00b9\n\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00c5\n\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00e0")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00eb\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u010b\n\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u012b\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0147\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u016c\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u0176\n\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\6\37\u01a3\n\37\r\37\16\37\u01a4")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3\"\2\2#\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@B\2\3\5\2\23")
        buf.write("\23  &\'\2\u01b7\2D\3\2\2\2\4o\3\2\2\2\6r\3\2\2\2\b|\3")
        buf.write("\2\2\2\n\u0083\3\2\2\2\f\u0092\3\2\2\2\16\u009e\3\2\2")
        buf.write("\2\20\u00c4\3\2\2\2\22\u00df\3\2\2\2\24\u00ea\3\2\2\2")
        buf.write("\26\u010a\3\2\2\2\30\u012a\3\2\2\2\32\u0146\3\2\2\2\34")
        buf.write("\u016b\3\2\2\2\36\u0175\3\2\2\2 \u0177\3\2\2\2\"\u017a")
        buf.write("\3\2\2\2$\u017d\3\2\2\2&\u0180\3\2\2\2(\u0183\3\2\2\2")
        buf.write("*\u0186\3\2\2\2,\u0189\3\2\2\2.\u018c\3\2\2\2\60\u018f")
        buf.write("\3\2\2\2\62\u0192\3\2\2\2\64\u0195\3\2\2\2\66\u0198\3")
        buf.write("\2\2\28\u019b\3\2\2\2:\u019e\3\2\2\2<\u01a2\3\2\2\2>\u01a6")
        buf.write("\3\2\2\2@\u01a8\3\2\2\2B\u01aa\3\2\2\2DE\7\"\2\2EF\5 ")
        buf.write("\21\2FG\5\4\3\2GH\7#\2\2H\3\3\2\2\2Ip\5\24\13\2Jp\5\6")
        buf.write("\4\2KL\7\"\2\2LM\5*\26\2MN\5\4\3\2NO\5\f\7\2OP\7#\2\2")
        buf.write("Pp\3\2\2\2Qp\5\20\t\2RS\7\"\2\2ST\5\64\33\2TU\5\4\3\2")
        buf.write("UV\5\4\3\2VW\7#\2\2Wp\3\2\2\2XY\7\"\2\2YZ\5\62\32\2Z[")
        buf.write("\5\36\20\2[\\\5\4\3\2\\p\3\2\2\2]^\7\"\2\2^_\5\"\22\2")
        buf.write("_`\5\4\3\2`a\7#\2\2ap\3\2\2\2bc\7\"\2\2cd\5*\26\2de\7")
        buf.write("\"\2\2ef\5\24\13\2fg\7\"\2\2gh\5$\23\2hi\5\f\7\2ij\7#")
        buf.write("\2\2jk\7#\2\2kl\5\f\7\2lm\7#\2\2mp\3\2\2\2np\5\22\n\2")
        buf.write("oI\3\2\2\2oJ\3\2\2\2oK\3\2\2\2oQ\3\2\2\2oR\3\2\2\2oX\3")
        buf.write("\2\2\2o]\3\2\2\2ob\3\2\2\2on\3\2\2\2p\5\3\2\2\2qs\7\"")
        buf.write("\2\2rq\3\2\2\2rs\3\2\2\2st\3\2\2\2tu\7\3\2\2uv\5<\37\2")
        buf.write("vw\7\4\2\2wy\5<\37\2xz\7#\2\2yx\3\2\2\2yz\3\2\2\2z\7\3")
        buf.write("\2\2\2{}\7\"\2\2|{\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177\7")
        buf.write("\3\2\2\177\u0081\5<\37\2\u0080\u0082\7#\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\t\3\2\2\2\u0083\u0084")
        buf.write("\7\"\2\2\u0084\u0085\7\5\2\2\u0085\u0086\5<\37\2\u0086")
        buf.write("\u0087\7#\2\2\u0087\13\3\2\2\2\u0088\u0089\7\"\2\2\u0089")
        buf.write("\u008a\7\5\2\2\u008a\u008b\5<\37\2\u008b\u008c\7#\2\2")
        buf.write("\u008c\u0093\3\2\2\2\u008d\u008e\7\"\2\2\u008e\u008f\5")
        buf.write("8\35\2\u008f\u0090\5\f\7\2\u0090\u0091\7#\2\2\u0091\u0093")
        buf.write("\3\2\2\2\u0092\u0088\3\2\2\2\u0092\u008d\3\2\2\2\u0093")
        buf.write("\r\3\2\2\2\u0094\u0095\7\"\2\2\u0095\u0096\5\66\34\2\u0096")
        buf.write("\u0097\5\n\6\2\u0097\u0098\7#\2\2\u0098\u009f\3\2\2\2")
        buf.write("\u0099\u009a\7\"\2\2\u009a\u009b\5\66\34\2\u009b\u009c")
        buf.write("\5\f\7\2\u009c\u009d\7#\2\2\u009d\u009f\3\2\2\2\u009e")
        buf.write("\u0094\3\2\2\2\u009e\u0099\3\2\2\2\u009f\17\3\2\2\2\u00a0")
        buf.write("\u00a1\7\"\2\2\u00a1\u00a2\5\64\33\2\u00a2\u00a3\5\20")
        buf.write("\t\2\u00a3\u00a4\5\20\t\2\u00a4\u00a5\7#\2\2\u00a5\u00c5")
        buf.write("\3\2\2\2\u00a6\u00a7\7\"\2\2\u00a7\u00a8\5*\26\2\u00a8")
        buf.write("\u00a9\5\4\3\2\u00a9\u00aa\5\f\7\2\u00aa\u00ab\7#\2\2")
        buf.write("\u00ab\u00c5\3\2\2\2\u00ac\u00ad\7\"\2\2\u00ad\u00ae\5")
        buf.write(":\36\2\u00ae\u00af\5\4\3\2\u00af\u00b0\7#\2\2\u00b0\u00c5")
        buf.write("\3\2\2\2\u00b1\u00b2\7\"\2\2\u00b2\u00b3\7\6\2\2\u00b3")
        buf.write("\u00b8\5B\"\2\u00b4\u00b6\7\3\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\5")
        buf.write("<\37\2\u00b8\u00b5\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba")
        buf.write("\3\2\2\2\u00ba\u00bb\7#\2\2\u00bb\u00c5\3\2\2\2\u00bc")
        buf.write("\u00bd\7\"\2\2\u00bd\u00be\5> \2\u00be\u00bf\7#\2\2\u00bf")
        buf.write("\u00c5\3\2\2\2\u00c0\u00c1\7\"\2\2\u00c1\u00c2\5@!\2\u00c2")
        buf.write("\u00c3\7#\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00a0\3\2\2\2")
        buf.write("\u00c4\u00a6\3\2\2\2\u00c4\u00ac\3\2\2\2\u00c4\u00b1\3")
        buf.write("\2\2\2\u00c4\u00bc\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c5\21")
        buf.write("\3\2\2\2\u00c6\u00c7\7\"\2\2\u00c7\u00c8\5*\26\2\u00c8")
        buf.write("\u00c9\7\"\2\2\u00c9\u00ca\5&\24\2\u00ca\u00cb\5\b\5\2")
        buf.write("\u00cb\u00cc\7#\2\2\u00cc\u00cd\7\"\2\2\u00cd\u00ce\7")
        buf.write("\5\2\2\u00ce\u00cf\7\7\2\2\u00cf\u00d0\7\b\2\2\u00d0\u00d1")
        buf.write("\7#\2\2\u00d1\u00d2\7#\2\2\u00d2\u00e0\3\2\2\2\u00d3\u00e0")
        buf.write("\5\26\f\2\u00d4\u00d5\7\"\2\2\u00d5\u00d6\5*\26\2\u00d6")
        buf.write("\u00d7\5\4\3\2\u00d7\u00d8\5\16\b\2\u00d8\u00d9\7#\2\2")
        buf.write("\u00d9\u00e0\3\2\2\2\u00da\u00db\7\"\2\2\u00db\u00dc\7")
        buf.write("\t\2\2\u00dc\u00dd\5<\37\2\u00dd\u00de\7#\2\2\u00de\u00e0")
        buf.write("\3\2\2\2\u00df\u00c6\3\2\2\2\u00df\u00d3\3\2\2\2\u00df")
        buf.write("\u00d4\3\2\2\2\u00df\u00da\3\2\2\2\u00e0\23\3\2\2\2\u00e1")
        buf.write("\u00e2\7\"\2\2\u00e2\u00e3\7\n\2\2\u00e3\u00e4\5<\37\2")
        buf.write("\u00e4\u00e5\5\24\13\2\u00e5\u00e6\7#\2\2\u00e6\u00eb")
        buf.write("\3\2\2\2\u00e7\u00eb\5\26\f\2\u00e8\u00eb\5\30\r\2\u00e9")
        buf.write("\u00eb\5\32\16\2\u00ea\u00e1\3\2\2\2\u00ea\u00e7\3\2\2")
        buf.write("\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\25\3")
        buf.write("\2\2\2\u00ec\u00ed\7\"\2\2\u00ed\u00ee\5(\25\2\u00ee\u00ef")
        buf.write("\5\22\n\2\u00ef\u00f0\5\n\6\2\u00f0\u00f1\7#\2\2\u00f1")
        buf.write("\u010b\3\2\2\2\u00f2\u00f3\7\"\2\2\u00f3\u00f4\5(\25\2")
        buf.write("\u00f4\u00f5\5\22\n\2\u00f5\u00f6\5\f\7\2\u00f6\u00f7")
        buf.write("\5\34\17\2\u00f7\u00f8\5\20\t\2\u00f8\u00f9\7#\2\2\u00f9")
        buf.write("\u010b\3\2\2\2\u00fa\u00fb\7\"\2\2\u00fb\u00fc\5(\25\2")
        buf.write("\u00fc\u00fd\5\22\n\2\u00fd\u00fe\5\n\6\2\u00fe\u00ff")
        buf.write("\5\34\17\2\u00ff\u0100\5\4\3\2\u0100\u0101\7#\2\2\u0101")
        buf.write("\u010b\3\2\2\2\u0102\u0103\7\"\2\2\u0103\u0104\5(\25\2")
        buf.write("\u0104\u0105\5\22\n\2\u0105\u0106\5\16\b\2\u0106\u0107")
        buf.write("\5\34\17\2\u0107\u0108\5\4\3\2\u0108\u0109\7#\2\2\u0109")
        buf.write("\u010b\3\2\2\2\u010a\u00ec\3\2\2\2\u010a\u00f2\3\2\2\2")
        buf.write("\u010a\u00fa\3\2\2\2\u010a\u0102\3\2\2\2\u010b\27\3\2")
        buf.write("\2\2\u010c\u010d\7\"\2\2\u010d\u010e\5,\27\2\u010e\u010f")
        buf.write("\5\22\n\2\u010f\u0110\5\34\17\2\u0110\u0111\5\f\7\2\u0111")
        buf.write("\u0112\7#\2\2\u0112\u012b\3\2\2\2\u0113\u0114\7\"\2\2")
        buf.write("\u0114\u0115\5.\30\2\u0115\u0116\5\22\n\2\u0116\u0117")
        buf.write("\5\34\17\2\u0117\u0118\5\f\7\2\u0118\u0119\7#\2\2\u0119")
        buf.write("\u012b\3\2\2\2\u011a\u011b\7\"\2\2\u011b\u011c\5.\30\2")
        buf.write("\u011c\u011d\5\22\n\2\u011d\u011e\5\34\17\2\u011e\u011f")
        buf.write("\5\n\6\2\u011f\u0120\5\4\3\2\u0120\u0121\7#\2\2\u0121")
        buf.write("\u012b\3\2\2\2\u0122\u0123\7\"\2\2\u0123\u0124\5.\30\2")
        buf.write("\u0124\u0125\5\22\n\2\u0125\u0126\5\34\17\2\u0126\u0127")
        buf.write("\5\16\b\2\u0127\u0128\5\4\3\2\u0128\u0129\7#\2\2\u0129")
        buf.write("\u012b\3\2\2\2\u012a\u010c\3\2\2\2\u012a\u0113\3\2\2\2")
        buf.write("\u012a\u011a\3\2\2\2\u012a\u0122\3\2\2\2\u012b\31\3\2")
        buf.write("\2\2\u012c\u012d\7\"\2\2\u012d\u012e\5\60\31\2\u012e\u012f")
        buf.write("\5\22\n\2\u012f\u0130\5\f\7\2\u0130\u0131\5\34\17\2\u0131")
        buf.write("\u0132\5\20\t\2\u0132\u0133\7#\2\2\u0133\u0147\3\2\2\2")
        buf.write("\u0134\u0135\7\"\2\2\u0135\u0136\5\60\31\2\u0136\u0137")
        buf.write("\5\22\n\2\u0137\u0138\5\n\6\2\u0138\u0139\5\34\17\2\u0139")
        buf.write("\u013a\5\20\t\2\u013a\u013b\5\4\3\2\u013b\u013c\7#\2\2")
        buf.write("\u013c\u0147\3\2\2\2\u013d\u013e\7\"\2\2\u013e\u013f\5")
        buf.write("\60\31\2\u013f\u0140\5\22\n\2\u0140\u0141\5\16\b\2\u0141")
        buf.write("\u0142\5\34\17\2\u0142\u0143\5\20\t\2\u0143\u0144\5\4")
        buf.write("\3\2\u0144\u0145\7#\2\2\u0145\u0147\3\2\2\2\u0146\u012c")
        buf.write("\3\2\2\2\u0146\u0134\3\2\2\2\u0146\u013d\3\2\2\2\u0147")
        buf.write("\33\3\2\2\2\u0148\u0149\7\"\2\2\u0149\u014a\7\5\2\2\u014a")
        buf.write("\u014b\7\13\2\2\u014b\u016c\7#\2\2\u014c\u014d\7\"\2\2")
        buf.write("\u014d\u014e\7\5\2\2\u014e\u014f\7\7\2\2\u014f\u0150\7")
        buf.write("\13\2\2\u0150\u016c\7#\2\2\u0151\u0152\7\"\2\2\u0152\u0153")
        buf.write("\7\5\2\2\u0153\u0154\7\f\2\2\u0154\u016c\7#\2\2\u0155")
        buf.write("\u0156\7\"\2\2\u0156\u0157\7\5\2\2\u0157\u0158\7\r\2\2")
        buf.write("\u0158\u016c\7#\2\2\u0159\u015a\7\"\2\2\u015a\u015b\7")
        buf.write("\5\2\2\u015b\u015c\7\f\2\2\u015c\u015d\7\13\2\2\u015d")
        buf.write("\u016c\7#\2\2\u015e\u015f\7\"\2\2\u015f\u0160\7\5\2\2")
        buf.write("\u0160\u0161\7\r\2\2\u0161\u0162\7\13\2\2\u0162\u016c")
        buf.write("\7#\2\2\u0163\u0164\7\"\2\2\u0164\u0165\7\5\2\2\u0165")
        buf.write("\u0166\7\16\2\2\u0166\u016c\7#\2\2\u0167\u0168\7\"\2\2")
        buf.write("\u0168\u0169\7\5\2\2\u0169\u016a\7\17\2\2\u016a\u016c")
        buf.write("\7#\2\2\u016b\u0148\3\2\2\2\u016b\u014c\3\2\2\2\u016b")
        buf.write("\u0151\3\2\2\2\u016b\u0155\3\2\2\2\u016b\u0159\3\2\2\2")
        buf.write("\u016b\u015e\3\2\2\2\u016b\u0163\3\2\2\2\u016b\u0167\3")
        buf.write("\2\2\2\u016c\35\3\2\2\2\u016d\u016e\7\"\2\2\u016e\u016f")
        buf.write("\7\5\2\2\u016f\u0170\7\20\2\2\u0170\u0176\7#\2\2\u0171")
        buf.write("\u0172\7\"\2\2\u0172\u0173\7\5\2\2\u0173\u0174\7\21\2")
        buf.write("\2\u0174\u0176\7#\2\2\u0175\u016d\3\2\2\2\u0175\u0171")
        buf.write("\3\2\2\2\u0176\37\3\2\2\2\u0177\u0178\7!\2\2\u0178\u0179")
        buf.write("\7\22\2\2\u0179!\3\2\2\2\u017a\u017b\7!\2\2\u017b\u017c")
        buf.write("\7\23\2\2\u017c#\3\2\2\2\u017d\u017e\7!\2\2\u017e\u017f")
        buf.write("\7\24\2\2\u017f%\3\2\2\2\u0180\u0181\7!\2\2\u0181\u0182")
        buf.write("\7\25\2\2\u0182\'\3\2\2\2\u0183\u0184\7!\2\2\u0184\u0185")
        buf.write("\7\26\2\2\u0185)\3\2\2\2\u0186\u0187\7!\2\2\u0187\u0188")
        buf.write("\7\27\2\2\u0188+\3\2\2\2\u0189\u018a\7!\2\2\u018a\u018b")
        buf.write("\7\30\2\2\u018b-\3\2\2\2\u018c\u018d\7!\2\2\u018d\u018e")
        buf.write("\7\31\2\2\u018e/\3\2\2\2\u018f\u0190\7!\2\2\u0190\u0191")
        buf.write("\7\32\2\2\u0191\61\3\2\2\2\u0192\u0193\7!\2\2\u0193\u0194")
        buf.write("\7\33\2\2\u0194\63\3\2\2\2\u0195\u0196\7!\2\2\u0196\u0197")
        buf.write("\7\34\2\2\u0197\65\3\2\2\2\u0198\u0199\7!\2\2\u0199\u019a")
        buf.write("\7\35\2\2\u019a\67\3\2\2\2\u019b\u019c\7!\2\2\u019c\u019d")
        buf.write("\7\36\2\2\u019d9\3\2\2\2\u019e\u019f\7!\2\2\u019f\u01a0")
        buf.write("\7\37\2\2\u01a0;\3\2\2\2\u01a1\u01a3\t\2\2\2\u01a2\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5=\3\2\2\2\u01a6\u01a7\7$\2\2\u01a7")
        buf.write("?\3\2\2\2\u01a8\u01a9\7%\2\2\u01a9A\3\2\2\2\u01aa\u01ab")
        buf.write("\7&\2\2\u01abC\3\2\2\2\24ory|\u0081\u0092\u009e\u00b5")
        buf.write("\u00b8\u00c4\u00df\u00ea\u010a\u012a\u0146\u016b\u0175")
        buf.write("\u01a4")
        return buf.getvalue()


class OvernightParser ( Parser ):

    grammarFileName = "Overnight.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'en.'", "'.'", "'string'", "'number'", 
                     "'!'", "'type'", "'var'", "'lambda'", "'='", "'<'", 
                     "'>'", "'min'", "'max'", "'sum'", "'avg'", "'listValue'", 
                     "'size'", "'domain'", "'singleton'", "'filter'", "'getProperty'", 
                     "'superlative'", "'countSuperlative'", "'countComparative'", 
                     "'aggregate'", "'concat'", "'reverse'", "'ensureNumericProperty'", 
                     "'ensureNumericEntity'", "'date'", "<INVALID>", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PREFIX", "LB", 
                      "RB", "DATE", "TIME", "INTEGER", "STRING_LITERAL", 
                      "WS" ]

    RULE_root = 0
    RULE_np = 1
    RULE_entity = 2
    RULE_concept = 3
    RULE_predicate = 4
    RULE_relNP = 5
    RULE_reversePredicate = 6
    RULE_value = 7
    RULE_constraintNP = 8
    RULE_cp = 9
    RULE_filterCP = 10
    RULE_superlativeCP = 11
    RULE_comparativeCP = 12
    RULE_op = 13
    RULE_aggregateType = 14
    RULE_listValue = 15
    RULE_size = 16
    RULE_domain = 17
    RULE_singleton = 18
    RULE_filterFunc = 19
    RULE_getProperty = 20
    RULE_superlative = 21
    RULE_countSuperlative = 22
    RULE_countComparative = 23
    RULE_aggregate = 24
    RULE_concat = 25
    RULE_reverse = 26
    RULE_ensureNumericProperty = 27
    RULE_ensureNumericEntity = 28
    RULE_string = 29
    RULE_date = 30
    RULE_time = 31
    RULE_quantity = 32

    ruleNames =  [ "root", "np", "entity", "concept", "predicate", "relNP", 
                   "reversePredicate", "value", "constraintNP", "cp", "filterCP", 
                   "superlativeCP", "comparativeCP", "op", "aggregateType", 
                   "listValue", "size", "domain", "singleton", "filterFunc", 
                   "getProperty", "superlative", "countSuperlative", "countComparative", 
                   "aggregate", "concat", "reverse", "ensureNumericProperty", 
                   "ensureNumericEntity", "string", "date", "time", "quantity" ]

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
    PREFIX=31
    LB=32
    RB=33
    DATE=34
    TIME=35
    INTEGER=36
    STRING_LITERAL=37
    WS=38

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

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)

        def listValue(self):
            return self.getTypedRuleContext(OvernightParser.ListValueContext,0)


        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)


        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = OvernightParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(OvernightParser.LB)
            self.state = 67
            self.listValue()
            self.state = 68
            self.np()
            self.state = 69
            self.match(OvernightParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OvernightParser.RULE_np

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CPNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cp(self):
            return self.getTypedRuleContext(OvernightParser.CpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCPNP" ):
                listener.enterCPNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCPNP" ):
                listener.exitCPNP(self)


    class DomainCPNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(OvernightParser.LB)
            else:
                return self.getToken(OvernightParser.LB, i)
        def getProperty(self):
            return self.getTypedRuleContext(OvernightParser.GetPropertyContext,0)

        def cp(self):
            return self.getTypedRuleContext(OvernightParser.CpContext,0)

        def domain(self):
            return self.getTypedRuleContext(OvernightParser.DomainContext,0)

        def relNP(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OvernightParser.RelNPContext)
            else:
                return self.getTypedRuleContext(OvernightParser.RelNPContext,i)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(OvernightParser.RB)
            else:
                return self.getToken(OvernightParser.RB, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomainCPNP" ):
                listener.enterDomainCPNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomainCPNP" ):
                listener.exitDomainCPNP(self)


    class EntityNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def entity(self):
            return self.getTypedRuleContext(OvernightParser.EntityContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntityNP" ):
                listener.enterEntityNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntityNP" ):
                listener.exitEntityNP(self)


    class GetPropertyNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def getProperty(self):
            return self.getTypedRuleContext(OvernightParser.GetPropertyContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)

        def relNP(self):
            return self.getTypedRuleContext(OvernightParser.RelNPContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetPropertyNP" ):
                listener.enterGetPropertyNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetPropertyNP" ):
                listener.exitGetPropertyNP(self)


    class NumericNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(OvernightParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericNP" ):
                listener.enterNumericNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericNP" ):
                listener.exitNumericNP(self)


    class ConcatNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def concat(self):
            return self.getTypedRuleContext(OvernightParser.ConcatContext,0)

        def np(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OvernightParser.NpContext)
            else:
                return self.getTypedRuleContext(OvernightParser.NpContext,i)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatNP" ):
                listener.enterConcatNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatNP" ):
                listener.exitConcatNP(self)


    class AggregateNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def aggregate(self):
            return self.getTypedRuleContext(OvernightParser.AggregateContext,0)

        def aggregateType(self):
            return self.getTypedRuleContext(OvernightParser.AggregateTypeContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateNP" ):
                listener.enterAggregateNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateNP" ):
                listener.exitAggregateNP(self)


    class FilterNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterNP" ):
                listener.enterFilterNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterNP" ):
                listener.exitFilterNP(self)


    class SizeNPContext(NpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.NpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def size(self):
            return self.getTypedRuleContext(OvernightParser.SizeContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeNP" ):
                listener.enterSizeNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeNP" ):
                listener.exitSizeNP(self)



    def np(self):

        localctx = OvernightParser.NpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_np)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.CPNPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.cp()
                pass

            elif la_ == 2:
                localctx = OvernightParser.EntityNPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.entity()
                pass

            elif la_ == 3:
                localctx = OvernightParser.GetPropertyNPContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(OvernightParser.LB)
                self.state = 74
                self.getProperty()
                self.state = 75
                self.np()
                self.state = 76
                self.relNP()
                self.state = 77
                self.match(OvernightParser.RB)
                pass

            elif la_ == 4:
                localctx = OvernightParser.NumericNPContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.value()
                pass

            elif la_ == 5:
                localctx = OvernightParser.ConcatNPContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(OvernightParser.LB)
                self.state = 81
                self.concat()
                self.state = 82
                self.np()
                self.state = 83
                self.np()
                self.state = 84
                self.match(OvernightParser.RB)
                pass

            elif la_ == 6:
                localctx = OvernightParser.AggregateNPContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 86
                self.match(OvernightParser.LB)
                self.state = 87
                self.aggregate()
                self.state = 88
                self.aggregateType()
                self.state = 89
                self.np()
                pass

            elif la_ == 7:
                localctx = OvernightParser.SizeNPContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.match(OvernightParser.LB)
                self.state = 92
                self.size()
                self.state = 93
                self.np()
                self.state = 94
                self.match(OvernightParser.RB)
                pass

            elif la_ == 8:
                localctx = OvernightParser.DomainCPNPContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 96
                self.match(OvernightParser.LB)
                self.state = 97
                self.getProperty()
                self.state = 98
                self.match(OvernightParser.LB)
                self.state = 99
                self.cp()
                self.state = 100
                self.match(OvernightParser.LB)
                self.state = 101
                self.domain()
                self.state = 102
                self.relNP()
                self.state = 103
                self.match(OvernightParser.RB)
                self.state = 104
                self.match(OvernightParser.RB)
                self.state = 105
                self.relNP()
                self.state = 106
                self.match(OvernightParser.RB)
                pass

            elif la_ == 9:
                localctx = OvernightParser.FilterNPContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 108
                self.constraintNP()
                pass


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

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OvernightParser.StringContext)
            else:
                return self.getTypedRuleContext(OvernightParser.StringContext,i)


        def LB(self):
            return self.getToken(OvernightParser.LB, 0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_entity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntity" ):
                listener.enterEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntity" ):
                listener.exitEntity(self)




    def entity(self):

        localctx = OvernightParser.EntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_entity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OvernightParser.LB:
                self.state = 111
                self.match(OvernightParser.LB)


            self.state = 114
            self.match(OvernightParser.T__0)
            self.state = 115
            self.string()
            self.state = 116
            self.match(OvernightParser.T__1)
            self.state = 117
            self.string()
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 118
                self.match(OvernightParser.RB)


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
            return self.getTypedRuleContext(OvernightParser.StringContext,0)


        def LB(self):
            return self.getToken(OvernightParser.LB, 0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_concept

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcept" ):
                listener.enterConcept(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcept" ):
                listener.exitConcept(self)




    def concept(self):

        localctx = OvernightParser.ConceptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_concept)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==OvernightParser.LB:
                self.state = 121
                self.match(OvernightParser.LB)


            self.state = 124
            self.match(OvernightParser.T__0)
            self.state = 125
            self.string()
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 126
                self.match(OvernightParser.RB)


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

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)

        def string(self):
            return self.getTypedRuleContext(OvernightParser.StringContext,0)


        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = OvernightParser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(OvernightParser.LB)
            self.state = 130
            self.match(OvernightParser.T__2)
            self.state = 131
            self.string()
            self.state = 132
            self.match(OvernightParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelNPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OvernightParser.RULE_relNP

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringRelNPContext(RelNPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.RelNPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def string(self):
            return self.getTypedRuleContext(OvernightParser.StringContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringRelNP" ):
                listener.enterStringRelNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringRelNP" ):
                listener.exitStringRelNP(self)


    class NumberRelNPContext(RelNPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.RelNPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def ensureNumericProperty(self):
            return self.getTypedRuleContext(OvernightParser.EnsureNumericPropertyContext,0)

        def relNP(self):
            return self.getTypedRuleContext(OvernightParser.RelNPContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberRelNP" ):
                listener.enterNumberRelNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberRelNP" ):
                listener.exitNumberRelNP(self)



    def relNP(self):

        localctx = OvernightParser.RelNPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relNP)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.StringRelNPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(OvernightParser.LB)
                self.state = 135
                self.match(OvernightParser.T__2)
                self.state = 136
                self.string()
                self.state = 137
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.NumberRelNPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 139
                self.match(OvernightParser.LB)
                self.state = 140
                self.ensureNumericProperty()
                self.state = 141
                self.relNP()
                self.state = 142
                self.match(OvernightParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReversePredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)

        def reverse(self):
            return self.getTypedRuleContext(OvernightParser.ReverseContext,0)


        def predicate(self):
            return self.getTypedRuleContext(OvernightParser.PredicateContext,0)


        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def relNP(self):
            return self.getTypedRuleContext(OvernightParser.RelNPContext,0)


        def getRuleIndex(self):
            return OvernightParser.RULE_reversePredicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReversePredicate" ):
                listener.enterReversePredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReversePredicate" ):
                listener.exitReversePredicate(self)




    def reversePredicate(self):

        localctx = OvernightParser.ReversePredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_reversePredicate)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(OvernightParser.LB)
                self.state = 147
                self.reverse()
                self.state = 148
                self.predicate()
                self.state = 149
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(OvernightParser.LB)
                self.state = 152
                self.reverse()
                self.state = 153
                self.relNP()
                self.state = 154
                self.match(OvernightParser.RB)
                pass


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


        def getRuleIndex(self):
            return OvernightParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DateNPContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def date(self):
            return self.getTypedRuleContext(OvernightParser.DateContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDateNP" ):
                listener.enterDateNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDateNP" ):
                listener.exitDateNP(self)


    class NumericEntityNPContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def ensureNumericEntity(self):
            return self.getTypedRuleContext(OvernightParser.EnsureNumericEntityContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericEntityNP" ):
                listener.enterNumericEntityNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericEntityNP" ):
                listener.exitNumericEntityNP(self)


    class TimeNPContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def time(self):
            return self.getTypedRuleContext(OvernightParser.TimeContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeNP" ):
                listener.enterTimeNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeNP" ):
                listener.exitTimeNP(self)


    class NumberNPContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def quantity(self):
            return self.getTypedRuleContext(OvernightParser.QuantityContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)
        def string(self):
            return self.getTypedRuleContext(OvernightParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberNP" ):
                listener.enterNumberNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberNP" ):
                listener.exitNumberNP(self)


    class ConcatValueNPContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def concat(self):
            return self.getTypedRuleContext(OvernightParser.ConcatContext,0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OvernightParser.ValueContext)
            else:
                return self.getTypedRuleContext(OvernightParser.ValueContext,i)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatValueNP" ):
                listener.enterConcatValueNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatValueNP" ):
                listener.exitConcatValueNP(self)


    class AttributeNPContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def getProperty(self):
            return self.getTypedRuleContext(OvernightParser.GetPropertyContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)

        def relNP(self):
            return self.getTypedRuleContext(OvernightParser.RelNPContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributeNP" ):
                listener.enterAttributeNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributeNP" ):
                listener.exitAttributeNP(self)



    def value(self):

        localctx = OvernightParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.ConcatValueNPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(OvernightParser.LB)
                self.state = 159
                self.concat()
                self.state = 160
                self.value()
                self.state = 161
                self.value()
                self.state = 162
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.AttributeNPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(OvernightParser.LB)
                self.state = 165
                self.getProperty()
                self.state = 166
                self.np()
                self.state = 167
                self.relNP()
                self.state = 168
                self.match(OvernightParser.RB)
                pass

            elif la_ == 3:
                localctx = OvernightParser.NumericEntityNPContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.match(OvernightParser.LB)
                self.state = 171
                self.ensureNumericEntity()
                self.state = 172
                self.np()
                self.state = 173
                self.match(OvernightParser.RB)
                pass

            elif la_ == 4:
                localctx = OvernightParser.NumberNPContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.match(OvernightParser.LB)
                self.state = 176
                self.match(OvernightParser.T__3)
                self.state = 177
                self.quantity()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OvernightParser.T__0) | (1 << OvernightParser.T__16) | (1 << OvernightParser.T__29) | (1 << OvernightParser.INTEGER) | (1 << OvernightParser.STRING_LITERAL))) != 0):
                    self.state = 179
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==OvernightParser.T__0:
                        self.state = 178
                        self.match(OvernightParser.T__0)


                    self.state = 181
                    self.string()


                self.state = 184
                self.match(OvernightParser.RB)
                pass

            elif la_ == 5:
                localctx = OvernightParser.DateNPContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 186
                self.match(OvernightParser.LB)
                self.state = 187
                self.date()
                self.state = 188
                self.match(OvernightParser.RB)
                pass

            elif la_ == 6:
                localctx = OvernightParser.TimeNPContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 190
                self.match(OvernightParser.LB)
                self.state = 191
                self.time()
                self.state = 192
                self.match(OvernightParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintNPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OvernightParser.RULE_constraintNP

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeConstraintNPContext(ConstraintNPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ConstraintNPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(OvernightParser.LB)
            else:
                return self.getToken(OvernightParser.LB, i)
        def getProperty(self):
            return self.getTypedRuleContext(OvernightParser.GetPropertyContext,0)

        def singleton(self):
            return self.getTypedRuleContext(OvernightParser.SingletonContext,0)

        def concept(self):
            return self.getTypedRuleContext(OvernightParser.ConceptContext,0)

        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(OvernightParser.RB)
            else:
                return self.getToken(OvernightParser.RB, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeConstraintNP" ):
                listener.enterTypeConstraintNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeConstraintNP" ):
                listener.exitTypeConstraintNP(self)


    class FilterConstraintNPContext(ConstraintNPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ConstraintNPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def filterCP(self):
            return self.getTypedRuleContext(OvernightParser.FilterCPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterConstraintNP" ):
                listener.enterFilterConstraintNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterConstraintNP" ):
                listener.exitFilterConstraintNP(self)


    class EventConstraintNPContext(ConstraintNPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ConstraintNPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def getProperty(self):
            return self.getTypedRuleContext(OvernightParser.GetPropertyContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)

        def reversePredicate(self):
            return self.getTypedRuleContext(OvernightParser.ReversePredicateContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventConstraintNP" ):
                listener.enterEventConstraintNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventConstraintNP" ):
                listener.exitEventConstraintNP(self)


    class VoidConstraintNPContext(ConstraintNPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ConstraintNPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def string(self):
            return self.getTypedRuleContext(OvernightParser.StringContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidConstraintNP" ):
                listener.enterVoidConstraintNP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidConstraintNP" ):
                listener.exitVoidConstraintNP(self)



    def constraintNP(self):

        localctx = OvernightParser.ConstraintNPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constraintNP)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.TypeConstraintNPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(OvernightParser.LB)
                self.state = 197
                self.getProperty()
                self.state = 198
                self.match(OvernightParser.LB)
                self.state = 199
                self.singleton()
                self.state = 200
                self.concept()
                self.state = 201
                self.match(OvernightParser.RB)
                self.state = 202
                self.match(OvernightParser.LB)
                self.state = 203
                self.match(OvernightParser.T__2)
                self.state = 204
                self.match(OvernightParser.T__4)
                self.state = 205
                self.match(OvernightParser.T__5)
                self.state = 206
                self.match(OvernightParser.RB)
                self.state = 207
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.FilterConstraintNPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.filterCP()
                pass

            elif la_ == 3:
                localctx = OvernightParser.EventConstraintNPContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.match(OvernightParser.LB)
                self.state = 211
                self.getProperty()
                self.state = 212
                self.np()
                self.state = 213
                self.reversePredicate()
                self.state = 214
                self.match(OvernightParser.RB)
                pass

            elif la_ == 4:
                localctx = OvernightParser.VoidConstraintNPContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 216
                self.match(OvernightParser.LB)
                self.state = 217
                self.match(OvernightParser.T__6)
                self.state = 218
                self.string()
                self.state = 219
                self.match(OvernightParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OvernightParser.RULE_cp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NestedCPContext(CpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.CpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def string(self):
            return self.getTypedRuleContext(OvernightParser.StringContext,0)

        def cp(self):
            return self.getTypedRuleContext(OvernightParser.CpContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedCP" ):
                listener.enterNestedCP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedCP" ):
                listener.exitNestedCP(self)


    class CPContext(CpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.CpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def filterCP(self):
            return self.getTypedRuleContext(OvernightParser.FilterCPContext,0)

        def superlativeCP(self):
            return self.getTypedRuleContext(OvernightParser.SuperlativeCPContext,0)

        def comparativeCP(self):
            return self.getTypedRuleContext(OvernightParser.ComparativeCPContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCP" ):
                listener.enterCP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCP" ):
                listener.exitCP(self)



    def cp(self):

        localctx = OvernightParser.CpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cp)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.NestedCPContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(OvernightParser.LB)
                self.state = 224
                self.match(OvernightParser.T__7)
                self.state = 225
                self.string()
                self.state = 226
                self.cp()
                self.state = 227
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.CPContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.filterCP()
                pass

            elif la_ == 3:
                localctx = OvernightParser.CPContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.superlativeCP()
                pass

            elif la_ == 4:
                localctx = OvernightParser.CPContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.comparativeCP()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterCPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OvernightParser.RULE_filterCP

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FilterByReversePredicateContext(FilterCPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.FilterCPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def filterFunc(self):
            return self.getTypedRuleContext(OvernightParser.FilterFuncContext,0)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)

        def reversePredicate(self):
            return self.getTypedRuleContext(OvernightParser.ReversePredicateContext,0)

        def op(self):
            return self.getTypedRuleContext(OvernightParser.OpContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterByReversePredicate" ):
                listener.enterFilterByReversePredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterByReversePredicate" ):
                listener.exitFilterByReversePredicate(self)


    class FilterByAttributeContext(FilterCPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.FilterCPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def filterFunc(self):
            return self.getTypedRuleContext(OvernightParser.FilterFuncContext,0)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)

        def relNP(self):
            return self.getTypedRuleContext(OvernightParser.RelNPContext,0)

        def op(self):
            return self.getTypedRuleContext(OvernightParser.OpContext,0)

        def value(self):
            return self.getTypedRuleContext(OvernightParser.ValueContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterByAttribute" ):
                listener.enterFilterByAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterByAttribute" ):
                listener.exitFilterByAttribute(self)


    class FilterByPredicateContext(FilterCPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.FilterCPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def filterFunc(self):
            return self.getTypedRuleContext(OvernightParser.FilterFuncContext,0)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)

        def predicate(self):
            return self.getTypedRuleContext(OvernightParser.PredicateContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)
        def op(self):
            return self.getTypedRuleContext(OvernightParser.OpContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterByPredicate" ):
                listener.enterFilterByPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterByPredicate" ):
                listener.exitFilterByPredicate(self)



    def filterCP(self):

        localctx = OvernightParser.FilterCPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_filterCP)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.FilterByPredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(OvernightParser.LB)
                self.state = 235
                self.filterFunc()
                self.state = 236
                self.constraintNP()
                self.state = 237
                self.predicate()
                self.state = 238
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.FilterByAttributeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(OvernightParser.LB)
                self.state = 241
                self.filterFunc()
                self.state = 242
                self.constraintNP()
                self.state = 243
                self.relNP()
                self.state = 244
                self.op()
                self.state = 245
                self.value()
                self.state = 246
                self.match(OvernightParser.RB)
                pass

            elif la_ == 3:
                localctx = OvernightParser.FilterByPredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(OvernightParser.LB)
                self.state = 249
                self.filterFunc()
                self.state = 250
                self.constraintNP()
                self.state = 251
                self.predicate()
                self.state = 252
                self.op()
                self.state = 253
                self.np()
                self.state = 254
                self.match(OvernightParser.RB)
                pass

            elif la_ == 4:
                localctx = OvernightParser.FilterByReversePredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.match(OvernightParser.LB)
                self.state = 257
                self.filterFunc()
                self.state = 258
                self.constraintNP()
                self.state = 259
                self.reversePredicate()
                self.state = 260
                self.op()
                self.state = 261
                self.np()
                self.state = 262
                self.match(OvernightParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperlativeCPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OvernightParser.RULE_superlativeCP

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SuperlativeByReversePredicateContext(SuperlativeCPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.SuperlativeCPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def countSuperlative(self):
            return self.getTypedRuleContext(OvernightParser.CountSuperlativeContext,0)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)

        def op(self):
            return self.getTypedRuleContext(OvernightParser.OpContext,0)

        def reversePredicate(self):
            return self.getTypedRuleContext(OvernightParser.ReversePredicateContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperlativeByReversePredicate" ):
                listener.enterSuperlativeByReversePredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperlativeByReversePredicate" ):
                listener.exitSuperlativeByReversePredicate(self)


    class SuperlativeByPredicateContext(SuperlativeCPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.SuperlativeCPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def countSuperlative(self):
            return self.getTypedRuleContext(OvernightParser.CountSuperlativeContext,0)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)

        def op(self):
            return self.getTypedRuleContext(OvernightParser.OpContext,0)

        def relNP(self):
            return self.getTypedRuleContext(OvernightParser.RelNPContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)
        def predicate(self):
            return self.getTypedRuleContext(OvernightParser.PredicateContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperlativeByPredicate" ):
                listener.enterSuperlativeByPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperlativeByPredicate" ):
                listener.exitSuperlativeByPredicate(self)


    class SuperlativeByAttributeContext(SuperlativeCPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.SuperlativeCPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def superlative(self):
            return self.getTypedRuleContext(OvernightParser.SuperlativeContext,0)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)

        def op(self):
            return self.getTypedRuleContext(OvernightParser.OpContext,0)

        def relNP(self):
            return self.getTypedRuleContext(OvernightParser.RelNPContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperlativeByAttribute" ):
                listener.enterSuperlativeByAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperlativeByAttribute" ):
                listener.exitSuperlativeByAttribute(self)



    def superlativeCP(self):

        localctx = OvernightParser.SuperlativeCPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_superlativeCP)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.SuperlativeByAttributeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.match(OvernightParser.LB)
                self.state = 267
                self.superlative()
                self.state = 268
                self.constraintNP()
                self.state = 269
                self.op()
                self.state = 270
                self.relNP()
                self.state = 271
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.SuperlativeByPredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(OvernightParser.LB)
                self.state = 274
                self.countSuperlative()
                self.state = 275
                self.constraintNP()
                self.state = 276
                self.op()
                self.state = 277
                self.relNP()
                self.state = 278
                self.match(OvernightParser.RB)
                pass

            elif la_ == 3:
                localctx = OvernightParser.SuperlativeByPredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.match(OvernightParser.LB)
                self.state = 281
                self.countSuperlative()
                self.state = 282
                self.constraintNP()
                self.state = 283
                self.op()
                self.state = 284
                self.predicate()
                self.state = 285
                self.np()
                self.state = 286
                self.match(OvernightParser.RB)
                pass

            elif la_ == 4:
                localctx = OvernightParser.SuperlativeByReversePredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 288
                self.match(OvernightParser.LB)
                self.state = 289
                self.countSuperlative()
                self.state = 290
                self.constraintNP()
                self.state = 291
                self.op()
                self.state = 292
                self.reversePredicate()
                self.state = 293
                self.np()
                self.state = 294
                self.match(OvernightParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparativeCPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OvernightParser.RULE_comparativeCP

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComparativeByReversePredicateContext(ComparativeCPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ComparativeCPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def countComparative(self):
            return self.getTypedRuleContext(OvernightParser.CountComparativeContext,0)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)

        def reversePredicate(self):
            return self.getTypedRuleContext(OvernightParser.ReversePredicateContext,0)

        def op(self):
            return self.getTypedRuleContext(OvernightParser.OpContext,0)

        def value(self):
            return self.getTypedRuleContext(OvernightParser.ValueContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparativeByReversePredicate" ):
                listener.enterComparativeByReversePredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparativeByReversePredicate" ):
                listener.exitComparativeByReversePredicate(self)


    class ComparativeByPredicateContext(ComparativeCPContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.ComparativeCPContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def countComparative(self):
            return self.getTypedRuleContext(OvernightParser.CountComparativeContext,0)

        def constraintNP(self):
            return self.getTypedRuleContext(OvernightParser.ConstraintNPContext,0)

        def relNP(self):
            return self.getTypedRuleContext(OvernightParser.RelNPContext,0)

        def op(self):
            return self.getTypedRuleContext(OvernightParser.OpContext,0)

        def value(self):
            return self.getTypedRuleContext(OvernightParser.ValueContext,0)

        def RB(self):
            return self.getToken(OvernightParser.RB, 0)
        def predicate(self):
            return self.getTypedRuleContext(OvernightParser.PredicateContext,0)

        def np(self):
            return self.getTypedRuleContext(OvernightParser.NpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparativeByPredicate" ):
                listener.enterComparativeByPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparativeByPredicate" ):
                listener.exitComparativeByPredicate(self)



    def comparativeCP(self):

        localctx = OvernightParser.ComparativeCPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparativeCP)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.ComparativeByPredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(OvernightParser.LB)
                self.state = 299
                self.countComparative()
                self.state = 300
                self.constraintNP()
                self.state = 301
                self.relNP()
                self.state = 302
                self.op()
                self.state = 303
                self.value()
                self.state = 304
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.ComparativeByPredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(OvernightParser.LB)
                self.state = 307
                self.countComparative()
                self.state = 308
                self.constraintNP()
                self.state = 309
                self.predicate()
                self.state = 310
                self.op()
                self.state = 311
                self.value()
                self.state = 312
                self.np()
                self.state = 313
                self.match(OvernightParser.RB)
                pass

            elif la_ == 3:
                localctx = OvernightParser.ComparativeByReversePredicateContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 315
                self.match(OvernightParser.LB)
                self.state = 316
                self.countComparative()
                self.state = 317
                self.constraintNP()
                self.state = 318
                self.reversePredicate()
                self.state = 319
                self.op()
                self.state = 320
                self.value()
                self.state = 321
                self.np()
                self.state = 322
                self.match(OvernightParser.RB)
                pass


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


        def getRuleIndex(self):
            return OvernightParser.RULE_op

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EqualContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqual" ):
                listener.enterEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqual" ):
                listener.exitEqual(self)


    class MinContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMin" ):
                listener.enterMin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMin" ):
                listener.exitMin(self)


    class MaxContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMax" ):
                listener.enterMax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMax" ):
                listener.exitMax(self)


    class LessThanContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThan" ):
                listener.enterLessThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThan" ):
                listener.exitLessThan(self)


    class LessThanOrEqualContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLessThanOrEqual" ):
                listener.enterLessThanOrEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLessThanOrEqual" ):
                listener.exitLessThanOrEqual(self)


    class NotEqualContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotEqual" ):
                listener.enterNotEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotEqual" ):
                listener.exitNotEqual(self)


    class GreaterThanContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThan" ):
                listener.enterGreaterThan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThan" ):
                listener.exitGreaterThan(self)


    class GreaterThanOrEqualContext(OpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.OpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGreaterThanOrEqual" ):
                listener.enterGreaterThanOrEqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGreaterThanOrEqual" ):
                listener.exitGreaterThanOrEqual(self)



    def op(self):

        localctx = OvernightParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_op)
        try:
            self.state = 361
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(OvernightParser.LB)
                self.state = 327
                self.match(OvernightParser.T__2)
                self.state = 328
                self.match(OvernightParser.T__8)
                self.state = 329
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.NotEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(OvernightParser.LB)
                self.state = 331
                self.match(OvernightParser.T__2)
                self.state = 332
                self.match(OvernightParser.T__4)
                self.state = 333
                self.match(OvernightParser.T__8)
                self.state = 334
                self.match(OvernightParser.RB)
                pass

            elif la_ == 3:
                localctx = OvernightParser.LessThanContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.match(OvernightParser.LB)
                self.state = 336
                self.match(OvernightParser.T__2)
                self.state = 337
                self.match(OvernightParser.T__9)
                self.state = 338
                self.match(OvernightParser.RB)
                pass

            elif la_ == 4:
                localctx = OvernightParser.GreaterThanContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 339
                self.match(OvernightParser.LB)
                self.state = 340
                self.match(OvernightParser.T__2)
                self.state = 341
                self.match(OvernightParser.T__10)
                self.state = 342
                self.match(OvernightParser.RB)
                pass

            elif la_ == 5:
                localctx = OvernightParser.LessThanOrEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 343
                self.match(OvernightParser.LB)
                self.state = 344
                self.match(OvernightParser.T__2)
                self.state = 345
                self.match(OvernightParser.T__9)
                self.state = 346
                self.match(OvernightParser.T__8)
                self.state = 347
                self.match(OvernightParser.RB)
                pass

            elif la_ == 6:
                localctx = OvernightParser.GreaterThanOrEqualContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 348
                self.match(OvernightParser.LB)
                self.state = 349
                self.match(OvernightParser.T__2)
                self.state = 350
                self.match(OvernightParser.T__10)
                self.state = 351
                self.match(OvernightParser.T__8)
                self.state = 352
                self.match(OvernightParser.RB)
                pass

            elif la_ == 7:
                localctx = OvernightParser.MinContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 353
                self.match(OvernightParser.LB)
                self.state = 354
                self.match(OvernightParser.T__2)
                self.state = 355
                self.match(OvernightParser.T__11)
                self.state = 356
                self.match(OvernightParser.RB)
                pass

            elif la_ == 8:
                localctx = OvernightParser.MaxContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 357
                self.match(OvernightParser.LB)
                self.state = 358
                self.match(OvernightParser.T__2)
                self.state = 359
                self.match(OvernightParser.T__12)
                self.state = 360
                self.match(OvernightParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OvernightParser.RULE_aggregateType

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AvgAggregateContext(AggregateTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.AggregateTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAvgAggregate" ):
                listener.enterAvgAggregate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAvgAggregate" ):
                listener.exitAvgAggregate(self)


    class SumAggregateContext(AggregateTypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OvernightParser.AggregateTypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(OvernightParser.LB, 0)
        def RB(self):
            return self.getToken(OvernightParser.RB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumAggregate" ):
                listener.enterSumAggregate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumAggregate" ):
                listener.exitSumAggregate(self)



    def aggregateType(self):

        localctx = OvernightParser.AggregateTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_aggregateType)
        try:
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = OvernightParser.SumAggregateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.match(OvernightParser.LB)
                self.state = 364
                self.match(OvernightParser.T__2)
                self.state = 365
                self.match(OvernightParser.T__13)
                self.state = 366
                self.match(OvernightParser.RB)
                pass

            elif la_ == 2:
                localctx = OvernightParser.AvgAggregateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(OvernightParser.LB)
                self.state = 368
                self.match(OvernightParser.T__2)
                self.state = 369
                self.match(OvernightParser.T__14)
                self.state = 370
                self.match(OvernightParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_listValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListValue" ):
                listener.enterListValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListValue" ):
                listener.exitListValue(self)




    def listValue(self):

        localctx = OvernightParser.ListValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(OvernightParser.PREFIX)
            self.state = 374
            self.match(OvernightParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize" ):
                listener.enterSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize" ):
                listener.exitSize(self)




    def size(self):

        localctx = OvernightParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(OvernightParser.PREFIX)
            self.state = 377
            self.match(OvernightParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DomainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_domain

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDomain" ):
                listener.enterDomain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDomain" ):
                listener.exitDomain(self)




    def domain(self):

        localctx = OvernightParser.DomainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_domain)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(OvernightParser.PREFIX)
            self.state = 380
            self.match(OvernightParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingletonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_singleton

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleton" ):
                listener.enterSingleton(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleton" ):
                listener.exitSingleton(self)




    def singleton(self):

        localctx = OvernightParser.SingletonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_singleton)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(OvernightParser.PREFIX)
            self.state = 383
            self.match(OvernightParser.T__18)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_filterFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterFunc" ):
                listener.enterFilterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterFunc" ):
                listener.exitFilterFunc(self)




    def filterFunc(self):

        localctx = OvernightParser.FilterFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_filterFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(OvernightParser.PREFIX)
            self.state = 386
            self.match(OvernightParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_getProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetProperty" ):
                listener.enterGetProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetProperty" ):
                listener.exitGetProperty(self)




    def getProperty(self):

        localctx = OvernightParser.GetPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_getProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(OvernightParser.PREFIX)
            self.state = 389
            self.match(OvernightParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperlativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_superlative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperlative" ):
                listener.enterSuperlative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperlative" ):
                listener.exitSuperlative(self)




    def superlative(self):

        localctx = OvernightParser.SuperlativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_superlative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(OvernightParser.PREFIX)
            self.state = 392
            self.match(OvernightParser.T__21)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountSuperlativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_countSuperlative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountSuperlative" ):
                listener.enterCountSuperlative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountSuperlative" ):
                listener.exitCountSuperlative(self)




    def countSuperlative(self):

        localctx = OvernightParser.CountSuperlativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_countSuperlative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(OvernightParser.PREFIX)
            self.state = 395
            self.match(OvernightParser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CountComparativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_countComparative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCountComparative" ):
                listener.enterCountComparative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCountComparative" ):
                listener.exitCountComparative(self)




    def countComparative(self):

        localctx = OvernightParser.CountComparativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_countComparative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(OvernightParser.PREFIX)
            self.state = 398
            self.match(OvernightParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_aggregate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate" ):
                listener.enterAggregate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate" ):
                listener.exitAggregate(self)




    def aggregate(self):

        localctx = OvernightParser.AggregateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_aggregate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(OvernightParser.PREFIX)
            self.state = 401
            self.match(OvernightParser.T__24)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_concat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcat" ):
                listener.enterConcat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcat" ):
                listener.exitConcat(self)




    def concat(self):

        localctx = OvernightParser.ConcatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_concat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(OvernightParser.PREFIX)
            self.state = 404
            self.match(OvernightParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReverseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_reverse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverse" ):
                listener.enterReverse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverse" ):
                listener.exitReverse(self)




    def reverse(self):

        localctx = OvernightParser.ReverseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_reverse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.match(OvernightParser.PREFIX)
            self.state = 407
            self.match(OvernightParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnsureNumericPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_ensureNumericProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnsureNumericProperty" ):
                listener.enterEnsureNumericProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnsureNumericProperty" ):
                listener.exitEnsureNumericProperty(self)




    def ensureNumericProperty(self):

        localctx = OvernightParser.EnsureNumericPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_ensureNumericProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(OvernightParser.PREFIX)
            self.state = 410
            self.match(OvernightParser.T__27)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnsureNumericEntityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREFIX(self):
            return self.getToken(OvernightParser.PREFIX, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_ensureNumericEntity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnsureNumericEntity" ):
                listener.enterEnsureNumericEntity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnsureNumericEntity" ):
                listener.exitEnsureNumericEntity(self)




    def ensureNumericEntity(self):

        localctx = OvernightParser.EnsureNumericEntityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ensureNumericEntity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(OvernightParser.PREFIX)
            self.state = 413
            self.match(OvernightParser.T__28)
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
                return self.getTokens(OvernightParser.STRING_LITERAL)
            else:
                return self.getToken(OvernightParser.STRING_LITERAL, i)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(OvernightParser.INTEGER)
            else:
                return self.getToken(OvernightParser.INTEGER, i)

        def getRuleIndex(self):
            return OvernightParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = OvernightParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 415
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OvernightParser.T__16) | (1 << OvernightParser.T__29) | (1 << OvernightParser.INTEGER) | (1 << OvernightParser.STRING_LITERAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 418 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OvernightParser.T__16) | (1 << OvernightParser.T__29) | (1 << OvernightParser.INTEGER) | (1 << OvernightParser.STRING_LITERAL))) != 0)):
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

        def DATE(self):
            return self.getToken(OvernightParser.DATE, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDate" ):
                listener.enterDate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDate" ):
                listener.exitDate(self)




    def date(self):

        localctx = OvernightParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(OvernightParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIME(self):
            return self.getToken(OvernightParser.TIME, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = OvernightParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(OvernightParser.TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(OvernightParser.INTEGER, 0)

        def getRuleIndex(self):
            return OvernightParser.RULE_quantity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantity" ):
                listener.enterQuantity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantity" ):
                listener.exitQuantity(self)




    def quantity(self):

        localctx = OvernightParser.QuantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_quantity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(OvernightParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





