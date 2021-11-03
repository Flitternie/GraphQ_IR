// Generated from /data1/nlx/KqaPro_Parser/template/Template.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TemplateLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, COMPARATIVE=22, SUPERLATIVE=23, 
		OPERATOR=24, STRING_OP=25, QUANTITY_OP=26, DATE_OP=27, YEAR_OP=28, STRING=29, 
		STRING_LITERAL=30, INTEGER=31, DECIMAL=32, DOUBLE=33, INTEGER_POSITIVE=34, 
		DECIMAL_POSITIVE=35, DOUBLE_POSITIVE=36, INTEGER_NEGATIVE=37, DECIMAL_NEGATIVE=38, 
		DOUBLE_NEGATIVE=39, EXPONENT=40, BOQ=41, EOQ=42, WS=43;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "T__19", "T__20", "COMPARATIVE", "SUPERLATIVE", "OPERATOR", 
			"STRING_OP", "QUANTITY_OP", "DATE_OP", "YEAR_OP", "STRING", "STRING_LITERAL", 
			"INTEGER", "DECIMAL", "DOUBLE", "INTEGER_POSITIVE", "DECIMAL_POSITIVE", 
			"DOUBLE_POSITIVE", "INTEGER_NEGATIVE", "DECIMAL_NEGATIVE", "DOUBLE_NEGATIVE", 
			"EXPONENT", "PN_CHARS_BASE", "DIGIT", "BOQ", "EOQ", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'is'", "'How many'", "'For'", "','", "'what is'", "'What is the relation from'", 
			"'to'", "'Among'", "'which one has the'", "'Which one has the'", "'or'", 
			"'('", "')'", "'is the'", "'the'", "'one'", "'that'", "'whose'", "'his/her'", 
			"'its'", "'and'", null, null, null, "'equal to'", null, "'on'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, "COMPARATIVE", 
			"SUPERLATIVE", "OPERATOR", "STRING_OP", "QUANTITY_OP", "DATE_OP", "YEAR_OP", 
			"STRING", "STRING_LITERAL", "INTEGER", "DECIMAL", "DOUBLE", "INTEGER_POSITIVE", 
			"DECIMAL_POSITIVE", "DOUBLE_POSITIVE", "INTEGER_NEGATIVE", "DECIMAL_NEGATIVE", 
			"DOUBLE_NEGATIVE", "EXPONENT", "BOQ", "EOQ", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public TemplateLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Template.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2-\u01db\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3"+
		"\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3"+
		"\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3"+
		"\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3"+
		"\27\3\27\3\27\3\27\5\27\u00fb\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u010c\n\30\3\31\3\31\3\31"+
		"\3\31\5\31\u0112\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0146"+
		"\n\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u015e\n\35\3\36\6\36"+
		"\u0161\n\36\r\36\16\36\u0162\3\37\3\37\6\37\u0167\n\37\r\37\16\37\u0168"+
		"\3 \6 \u016c\n \r \16 \u016d\3!\6!\u0171\n!\r!\16!\u0172\3!\3!\7!\u0177"+
		"\n!\f!\16!\u017a\13!\3!\3!\6!\u017e\n!\r!\16!\u017f\5!\u0182\n!\3\"\6"+
		"\"\u0185\n\"\r\"\16\"\u0186\3\"\3\"\7\"\u018b\n\"\f\"\16\"\u018e\13\""+
		"\3\"\3\"\3\"\3\"\6\"\u0194\n\"\r\"\16\"\u0195\3\"\3\"\3\"\6\"\u019b\n"+
		"\"\r\"\16\"\u019c\3\"\3\"\5\"\u01a1\n\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&"+
		"\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\5)\u01b7\n)\3)\6)\u01ba\n)\r)\16)\u01bb"+
		"\3*\3*\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u01d0\n,\3-"+
		"\5-\u01d3\n-\3.\6.\u01d6\n.\r.\16.\u01d7\3.\3.\3\u0162\2/\3\3\5\4\7\5"+
		"\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23"+
		"%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G"+
		"%I&K\'M(O)Q*S\2U\2W+Y,[-\3\2\6\4\2GGgg\4\2--//\4\2C\\c|\5\2\13\f\17\17"+
		"\"\"\2\u01f8\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2"+
		"\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2"+
		"\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2"+
		"\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2"+
		"\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3"+
		"\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2"+
		"\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2"+
		"W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\3]\3\2\2\2\5`\3\2\2\2\7i\3\2\2\2\tm\3"+
		"\2\2\2\13o\3\2\2\2\rw\3\2\2\2\17\u0091\3\2\2\2\21\u0094\3\2\2\2\23\u009a"+
		"\3\2\2\2\25\u00ac\3\2\2\2\27\u00be\3\2\2\2\31\u00c1\3\2\2\2\33\u00c3\3"+
		"\2\2\2\35\u00c5\3\2\2\2\37\u00cc\3\2\2\2!\u00d0\3\2\2\2#\u00d4\3\2\2\2"+
		"%\u00d9\3\2\2\2\'\u00df\3\2\2\2)\u00e7\3\2\2\2+\u00eb\3\2\2\2-\u00fa\3"+
		"\2\2\2/\u010b\3\2\2\2\61\u0111\3\2\2\2\63\u0113\3\2\2\2\65\u0145\3\2\2"+
		"\2\67\u0147\3\2\2\29\u015d\3\2\2\2;\u0160\3\2\2\2=\u0166\3\2\2\2?\u016b"+
		"\3\2\2\2A\u0181\3\2\2\2C\u01a0\3\2\2\2E\u01a2\3\2\2\2G\u01a5\3\2\2\2I"+
		"\u01a8\3\2\2\2K\u01ab\3\2\2\2M\u01ae\3\2\2\2O\u01b1\3\2\2\2Q\u01b4\3\2"+
		"\2\2S\u01bd\3\2\2\2U\u01bf\3\2\2\2W\u01cf\3\2\2\2Y\u01d2\3\2\2\2[\u01d5"+
		"\3\2\2\2]^\7k\2\2^_\7u\2\2_\4\3\2\2\2`a\7J\2\2ab\7q\2\2bc\7y\2\2cd\7\""+
		"\2\2de\7o\2\2ef\7c\2\2fg\7p\2\2gh\7{\2\2h\6\3\2\2\2ij\7H\2\2jk\7q\2\2"+
		"kl\7t\2\2l\b\3\2\2\2mn\7.\2\2n\n\3\2\2\2op\7y\2\2pq\7j\2\2qr\7c\2\2rs"+
		"\7v\2\2st\7\"\2\2tu\7k\2\2uv\7u\2\2v\f\3\2\2\2wx\7Y\2\2xy\7j\2\2yz\7c"+
		"\2\2z{\7v\2\2{|\7\"\2\2|}\7k\2\2}~\7u\2\2~\177\7\"\2\2\177\u0080\7v\2"+
		"\2\u0080\u0081\7j\2\2\u0081\u0082\7g\2\2\u0082\u0083\7\"\2\2\u0083\u0084"+
		"\7t\2\2\u0084\u0085\7g\2\2\u0085\u0086\7n\2\2\u0086\u0087\7c\2\2\u0087"+
		"\u0088\7v\2\2\u0088\u0089\7k\2\2\u0089\u008a\7q\2\2\u008a\u008b\7p\2\2"+
		"\u008b\u008c\7\"\2\2\u008c\u008d\7h\2\2\u008d\u008e\7t\2\2\u008e\u008f"+
		"\7q\2\2\u008f\u0090\7o\2\2\u0090\16\3\2\2\2\u0091\u0092\7v\2\2\u0092\u0093"+
		"\7q\2\2\u0093\20\3\2\2\2\u0094\u0095\7C\2\2\u0095\u0096\7o\2\2\u0096\u0097"+
		"\7q\2\2\u0097\u0098\7p\2\2\u0098\u0099\7i\2\2\u0099\22\3\2\2\2\u009a\u009b"+
		"\7y\2\2\u009b\u009c\7j\2\2\u009c\u009d\7k\2\2\u009d\u009e\7e\2\2\u009e"+
		"\u009f\7j\2\2\u009f\u00a0\7\"\2\2\u00a0\u00a1\7q\2\2\u00a1\u00a2\7p\2"+
		"\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7\"\2\2\u00a4\u00a5\7j\2\2\u00a5\u00a6"+
		"\7c\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7\"\2\2\u00a8\u00a9\7v\2\2\u00a9"+
		"\u00aa\7j\2\2\u00aa\u00ab\7g\2\2\u00ab\24\3\2\2\2\u00ac\u00ad\7Y\2\2\u00ad"+
		"\u00ae\7j\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1\7j\2\2"+
		"\u00b1\u00b2\7\"\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5"+
		"\7g\2\2\u00b5\u00b6\7\"\2\2\u00b6\u00b7\7j\2\2\u00b7\u00b8\7c\2\2\u00b8"+
		"\u00b9\7u\2\2\u00b9\u00ba\7\"\2\2\u00ba\u00bb\7v\2\2\u00bb\u00bc\7j\2"+
		"\2\u00bc\u00bd\7g\2\2\u00bd\26\3\2\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0"+
		"\7t\2\2\u00c0\30\3\2\2\2\u00c1\u00c2\7*\2\2\u00c2\32\3\2\2\2\u00c3\u00c4"+
		"\7+\2\2\u00c4\34\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8"+
		"\7\"\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7j\2\2\u00ca\u00cb\7g\2\2\u00cb"+
		"\36\3\2\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7j\2\2\u00ce\u00cf\7g\2\2\u00cf"+
		" \3\2\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7g\2\2\u00d3"+
		"\"\3\2\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6\7j\2\2\u00d6\u00d7\7c\2\2\u00d7"+
		"\u00d8\7v\2\2\u00d8$\3\2\2\2\u00d9\u00da\7y\2\2\u00da\u00db\7j\2\2\u00db"+
		"\u00dc\7q\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7g\2\2\u00de&\3\2\2\2\u00df"+
		"\u00e0\7j\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3\7\61\2"+
		"\2\u00e3\u00e4\7j\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7t\2\2\u00e6(\3\2"+
		"\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7u\2\2\u00ea*\3"+
		"\2\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7f\2\2\u00ee"+
		",\3\2\2\2\u00ef\u00f0\7i\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7g\2\2\u00f2"+
		"\u00f3\7c\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5\7g\2\2\u00f5\u00fb\7t\2\2"+
		"\u00f6\u00f7\7n\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7u\2\2\u00f9\u00fb"+
		"\7u\2\2\u00fa\u00ef\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fb.\3\2\2\2\u00fc\u00fd"+
		"\7n\2\2\u00fd\u00fe\7c\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7i\2\2\u0100"+
		"\u0101\7g\2\2\u0101\u0102\7u\2\2\u0102\u010c\7v\2\2\u0103\u0104\7u\2\2"+
		"\u0104\u0105\7o\2\2\u0105\u0106\7c\2\2\u0106\u0107\7n\2\2\u0107\u0108"+
		"\7n\2\2\u0108\u0109\7g\2\2\u0109\u010a\7u\2\2\u010a\u010c\7v\2\2\u010b"+
		"\u00fc\3\2\2\2\u010b\u0103\3\2\2\2\u010c\60\3\2\2\2\u010d\u0112\5\63\32"+
		"\2\u010e\u0112\5\65\33\2\u010f\u0112\5\67\34\2\u0110\u0112\59\35\2\u0111"+
		"\u010d\3\2\2\2\u0111\u010e\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0110\3\2"+
		"\2\2\u0112\62\3\2\2\2\u0113\u0114\7g\2\2\u0114\u0115\7s\2\2\u0115\u0116"+
		"\7w\2\2\u0116\u0117\7c\2\2\u0117\u0118\7n\2\2\u0118\u0119\7\"\2\2\u0119"+
		"\u011a\7v\2\2\u011a\u011b\7q\2\2\u011b\64\3\2\2\2\u011c\u011d\7n\2\2\u011d"+
		"\u011e\7g\2\2\u011e\u011f\7u\2\2\u011f\u0120\7u\2\2\u0120\u0121\7\"\2"+
		"\2\u0121\u0122\7v\2\2\u0122\u0123\7j\2\2\u0123\u0124\7c\2\2\u0124\u0146"+
		"\7p\2\2\u0125\u0126\7i\2\2\u0126\u0127\7t\2\2\u0127\u0128\7g\2\2\u0128"+
		"\u0129\7c\2\2\u0129\u012a\7v\2\2\u012a\u012b\7g\2\2\u012b\u012c\7t\2\2"+
		"\u012c\u012d\7\"\2\2\u012d\u012e\7v\2\2\u012e\u012f\7j\2\2\u012f\u0130"+
		"\7c\2\2\u0130\u0146\7p\2\2\u0131\u0132\7g\2\2\u0132\u0133\7s\2\2\u0133"+
		"\u0134\7w\2\2\u0134\u0135\7c\2\2\u0135\u0136\7n\2\2\u0136\u0137\7\"\2"+
		"\2\u0137\u0138\7v\2\2\u0138\u0146\7q\2\2\u0139\u013a\7p\2\2\u013a\u013b"+
		"\7q\2\2\u013b\u013c\7v\2\2\u013c\u013d\7\"\2\2\u013d\u013e\7g\2\2\u013e"+
		"\u013f\7s\2\2\u013f\u0140\7w\2\2\u0140\u0141\7c\2\2\u0141\u0142\7n\2\2"+
		"\u0142\u0143\7\"\2\2\u0143\u0144\7v\2\2\u0144\u0146\7q\2\2\u0145\u011c"+
		"\3\2\2\2\u0145\u0125\3\2\2\2\u0145\u0131\3\2\2\2\u0145\u0139\3\2\2\2\u0146"+
		"\66\3\2\2\2\u0147\u0148\7q\2\2\u0148\u0149\7p\2\2\u01498\3\2\2\2\u014a"+
		"\u014b\7d\2\2\u014b\u014c\7g\2\2\u014c\u014d\7h\2\2\u014d\u014e\7q\2\2"+
		"\u014e\u014f\7t\2\2\u014f\u015e\7g\2\2\u0150\u0151\7c\2\2\u0151\u0152"+
		"\7h\2\2\u0152\u0153\7v\2\2\u0153\u0154\7g\2\2\u0154\u015e\7t\2\2\u0155"+
		"\u0156\7k\2\2\u0156\u015e\7p\2\2\u0157\u0158\7p\2\2\u0158\u0159\7q\2\2"+
		"\u0159\u015a\7v\2\2\u015a\u015b\7\"\2\2\u015b\u015c\7k\2\2\u015c\u015e"+
		"\7p\2\2\u015d\u014a\3\2\2\2\u015d\u0150\3\2\2\2\u015d\u0155\3\2\2\2\u015d"+
		"\u0157\3\2\2\2\u015e:\3\2\2\2\u015f\u0161\5=\37\2\u0160\u015f\3\2\2\2"+
		"\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2\2\u0162\u0160\3\2\2\2\u0163<\3"+
		"\2\2\2\u0164\u0167\5S*\2\u0165\u0167\5U+\2\u0166\u0164\3\2\2\2\u0166\u0165"+
		"\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169"+
		">\3\2\2\2\u016a\u016c\5U+\2\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d"+
		"\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e@\3\2\2\2\u016f\u0171\5U+\2\u0170"+
		"\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2"+
		"\2\2\u0173\u0174\3\2\2\2\u0174\u0178\7\60\2\2\u0175\u0177\5U+\2\u0176"+
		"\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2"+
		"\2\2\u0179\u0182\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u017d\7\60\2\2\u017c"+
		"\u017e\5U+\2\u017d\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u017d\3\2\2"+
		"\2\u017f\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0170\3\2\2\2\u0181\u017b"+
		"\3\2\2\2\u0182B\3\2\2\2\u0183\u0185\5U+\2\u0184\u0183\3\2\2\2\u0185\u0186"+
		"\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188"+
		"\u018c\7\60\2\2\u0189\u018b\5U+\2\u018a\u0189\3\2\2\2\u018b\u018e\3\2"+
		"\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2\u018e"+
		"\u018c\3\2\2\2\u018f\u0190\5Q)\2\u0190\u01a1\3\2\2\2\u0191\u0193\7\60"+
		"\2\2\u0192\u0194\5U+\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0193"+
		"\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\5Q)\2\u0198"+
		"\u01a1\3\2\2\2\u0199\u019b\5U+\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2"+
		"\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f"+
		"\5Q)\2\u019f\u01a1\3\2\2\2\u01a0\u0184\3\2\2\2\u01a0\u0191\3\2\2\2\u01a0"+
		"\u019a\3\2\2\2\u01a1D\3\2\2\2\u01a2\u01a3\7-\2\2\u01a3\u01a4\5? \2\u01a4"+
		"F\3\2\2\2\u01a5\u01a6\7-\2\2\u01a6\u01a7\5A!\2\u01a7H\3\2\2\2\u01a8\u01a9"+
		"\7-\2\2\u01a9\u01aa\5C\"\2\u01aaJ\3\2\2\2\u01ab\u01ac\7/\2\2\u01ac\u01ad"+
		"\5? \2\u01adL\3\2\2\2\u01ae\u01af\7/\2\2\u01af\u01b0\5A!\2\u01b0N\3\2"+
		"\2\2\u01b1\u01b2\7/\2\2\u01b2\u01b3\5C\"\2\u01b3P\3\2\2\2\u01b4\u01b6"+
		"\t\2\2\2\u01b5\u01b7\t\3\2\2\u01b6\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7"+
		"\u01b9\3\2\2\2\u01b8\u01ba\5U+\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2"+
		"\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bcR\3\2\2\2\u01bd\u01be"+
		"\t\4\2\2\u01beT\3\2\2\2\u01bf\u01c0\4\62;\2\u01c0V\3\2\2\2\u01c1\u01c2"+
		"\7Y\2\2\u01c2\u01c3\7j\2\2\u01c3\u01c4\7c\2\2\u01c4\u01d0\7v\2\2\u01c5"+
		"\u01c6\7y\2\2\u01c6\u01c7\7j\2\2\u01c7\u01c8\7c\2\2\u01c8\u01d0\7v\2\2"+
		"\u01c9\u01ca\7Y\2\2\u01ca\u01cb\7j\2\2\u01cb\u01d0\7q\2\2\u01cc\u01cd"+
		"\7y\2\2\u01cd\u01ce\7j\2\2\u01ce\u01d0\7q\2\2\u01cf\u01c1\3\2\2\2\u01cf"+
		"\u01c5\3\2\2\2\u01cf\u01c9\3\2\2\2\u01cf\u01cc\3\2\2\2\u01d0X\3\2\2\2"+
		"\u01d1\u01d3\7A\2\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3Z\3\2"+
		"\2\2\u01d4\u01d6\t\5\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7"+
		"\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01da\b."+
		"\2\2\u01da\\\3\2\2\2\32\2\u00fa\u010b\u0111\u0145\u015d\u0162\u0166\u0168"+
		"\u016d\u0172\u0178\u017f\u0181\u0186\u018c\u0195\u019c\u01a0\u01b6\u01bb"+
		"\u01cf\u01d2\u01d7\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}