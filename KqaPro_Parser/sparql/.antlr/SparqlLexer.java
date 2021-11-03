// Generated from /data1/nlx/KqaPro_Parser/sparql/Sparql.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SparqlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, T__44=45, 
		T__45=46, T__46=47, T__47=48, T__48=49, T__49=50, T__50=51, T__51=52, 
		T__52=53, T__53=54, T__54=55, T__55=56, T__56=57, T__57=58, IRI_REF=59, 
		PNAME_NS=60, PNAME_LN=61, BLANK_NODE_LABEL=62, VAR1=63, VAR2=64, LANGTAG=65, 
		INTEGER=66, DECIMAL=67, DOUBLE=68, INTEGER_POSITIVE=69, DECIMAL_POSITIVE=70, 
		DOUBLE_POSITIVE=71, INTEGER_NEGATIVE=72, DECIMAL_NEGATIVE=73, DOUBLE_NEGATIVE=74, 
		EXPONENT=75, STRING_LITERAL1=76, STRING_LITERAL2=77, STRING_LITERAL_LONG1=78, 
		STRING_LITERAL_LONG2=79, ECHAR=80, NIL=81, ANON=82, PN_CHARS_U=83, VARNAME=84, 
		PN_PREFIX=85, PN_LOCAL=86, WS=87;
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
			"T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
			"T__25", "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", "T__32", 
			"T__33", "T__34", "T__35", "T__36", "T__37", "T__38", "T__39", "T__40", 
			"T__41", "T__42", "T__43", "T__44", "T__45", "T__46", "T__47", "T__48", 
			"T__49", "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", "T__56", 
			"T__57", "IRI_REF", "PNAME_NS", "PNAME_LN", "BLANK_NODE_LABEL", "VAR1", 
			"VAR2", "LANGTAG", "INTEGER", "DECIMAL", "DOUBLE", "INTEGER_POSITIVE", 
			"DECIMAL_POSITIVE", "DOUBLE_POSITIVE", "INTEGER_NEGATIVE", "DECIMAL_NEGATIVE", 
			"DOUBLE_NEGATIVE", "EXPONENT", "STRING_LITERAL1", "STRING_LITERAL2", 
			"STRING_LITERAL_LONG1", "STRING_LITERAL_LONG2", "ECHAR", "NIL", "ANON", 
			"PN_CHARS_U", "VARNAME", "PN_CHARS", "PN_PREFIX", "PN_LOCAL", "PN_CHARS_BASE", 
			"DIGIT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'BASE'", "'PREFIX'", "'SELECT'", "'DISTINCT'", "'REDUCED'", "'*'", 
			"'CONSTRUCT'", "'DESCRIBE'", "'ASK'", "'FROM'", "'NAMED'", "'WHERE'", 
			"'ORDER'", "'BY'", "'ASC'", "'DESC'", "'LIMIT'", "'OFFSET'", "'{'", "'.'", 
			"'}'", "'OPTIONAL'", "'GRAPH'", "'UNION'", "'FILTER'", "'('", "','", 
			"')'", "';'", "'a'", "'['", "']'", "'||'", "'&&'", "'='", "'!='", "'<'", 
			"'>'", "'<='", "'>='", "'+'", "'-'", "'/'", "'!'", "'STR'", "'LANG'", 
			"'LANGMATCHES'", "'DATATYPE'", "'BOUND'", "'sameTerm'", "'isIRI'", "'isURI'", 
			"'isBLANK'", "'isLITERAL'", "'REGEX'", "'^^'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "IRI_REF", 
			"PNAME_NS", "PNAME_LN", "BLANK_NODE_LABEL", "VAR1", "VAR2", "LANGTAG", 
			"INTEGER", "DECIMAL", "DOUBLE", "INTEGER_POSITIVE", "DECIMAL_POSITIVE", 
			"DOUBLE_POSITIVE", "INTEGER_NEGATIVE", "DECIMAL_NEGATIVE", "DOUBLE_NEGATIVE", 
			"EXPONENT", "STRING_LITERAL1", "STRING_LITERAL2", "STRING_LITERAL_LONG1", 
			"STRING_LITERAL_LONG2", "ECHAR", "NIL", "ANON", "PN_CHARS_U", "VARNAME", 
			"PN_PREFIX", "PN_LOCAL", "WS"
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


	public SparqlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Sparql.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2Y\u02e1\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT"+
		"\4U\tU\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\3\2\3\2\3\2\3\2\3\2\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b"+
		"\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3"+
		"\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3"+
		"\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20"+
		"\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23"+
		"\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34"+
		"\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3"+
		"$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-"+
		"\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3"+
		"\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3"+
		"\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3"+
		"\64\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3"+
		"\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3"+
		"\67\3\67\38\38\38\38\38\38\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3"+
		"<\3<\3<\7<\u01d4\n<\f<\16<\u01d7\13<\3<\3<\3=\5=\u01dc\n=\3=\3=\3>\3>"+
		"\3>\3?\3?\3?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\6B\u01f0\nB\rB\16B\u01f1\3"+
		"B\3B\3B\3B\6B\u01f8\nB\rB\16B\u01f9\7B\u01fc\nB\fB\16B\u01ff\13B\3C\6"+
		"C\u0202\nC\rC\16C\u0203\3D\6D\u0207\nD\rD\16D\u0208\3D\3D\7D\u020d\nD"+
		"\fD\16D\u0210\13D\3D\3D\6D\u0214\nD\rD\16D\u0215\5D\u0218\nD\3E\6E\u021b"+
		"\nE\rE\16E\u021c\3E\3E\7E\u0221\nE\fE\16E\u0224\13E\3E\3E\3E\3E\6E\u022a"+
		"\nE\rE\16E\u022b\3E\3E\3E\6E\u0231\nE\rE\16E\u0232\3E\3E\5E\u0237\nE\3"+
		"F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\5L\u024d\n"+
		"L\3L\6L\u0250\nL\rL\16L\u0251\3M\3M\3M\7M\u0257\nM\fM\16M\u025a\13M\3"+
		"M\3M\3N\3N\3N\7N\u0261\nN\fN\16N\u0264\13N\3N\3N\3O\3O\3O\3O\3O\3O\3O"+
		"\5O\u026f\nO\3O\3O\5O\u0273\nO\7O\u0275\nO\fO\16O\u0278\13O\3O\3O\3O\3"+
		"O\3P\3P\3P\3P\3P\3P\3P\5P\u0285\nP\3P\3P\5P\u0289\nP\7P\u028b\nP\fP\16"+
		"P\u028e\13P\3P\3P\3P\3P\3Q\3Q\3Q\3R\3R\7R\u0299\nR\fR\16R\u029c\13R\3"+
		"R\3R\3S\3S\7S\u02a2\nS\fS\16S\u02a5\13S\3S\3S\3T\3T\5T\u02ab\nT\3U\3U"+
		"\5U\u02af\nU\3U\3U\3U\7U\u02b4\nU\fU\16U\u02b7\13U\3V\3V\3V\5V\u02bc\n"+
		"V\3W\3W\3W\7W\u02c1\nW\fW\16W\u02c4\13W\3W\5W\u02c7\nW\3X\3X\5X\u02cb"+
		"\nX\3X\3X\7X\u02cf\nX\fX\16X\u02d2\13X\3X\5X\u02d5\nX\3Y\3Y\3Z\3Z\3[\6"+
		"[\u02dc\n[\r[\16[\u02dd\3[\3[\2\2\\\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n"+
		"\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30"+
		"/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.["+
		"/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083"+
		"C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097"+
		"M\u0099N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00ab"+
		"\2\u00adW\u00afX\u00b1\2\u00b3\2\u00b5Y\3\2\f\t\2$$>>@@^^``bb}\177\4\2"+
		"GGgg\4\2--//\6\2\f\f\17\17))^^\6\2\f\f\17\17$$^^\4\2))^^\t\2$$))ddhhp"+
		"pttvv\5\2\u00b9\u00b9\u0302\u0371\u2041\u2042\17\2C\\c|\u00c2\u00d8\u00da"+
		"\u00f8\u00fa\u0301\u0372\u037f\u0381\u2001\u200e\u200f\u2072\u2191\u2c02"+
		"\u2ff1\u3003\ud801\uf902\ufdd1\ufdf2\uffff\5\2\13\f\17\17\"\"\2\u030d"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3"+
		"\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2"+
		"\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2"+
		"U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3"+
		"\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2"+
		"\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2"+
		"{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085"+
		"\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2"+
		"\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097"+
		"\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2"+
		"\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9"+
		"\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b5\3\2\2\2\3\u00b7\3\2\2"+
		"\2\5\u00bc\3\2\2\2\7\u00c3\3\2\2\2\t\u00ca\3\2\2\2\13\u00d3\3\2\2\2\r"+
		"\u00db\3\2\2\2\17\u00dd\3\2\2\2\21\u00e7\3\2\2\2\23\u00f0\3\2\2\2\25\u00f4"+
		"\3\2\2\2\27\u00f9\3\2\2\2\31\u00ff\3\2\2\2\33\u0105\3\2\2\2\35\u010b\3"+
		"\2\2\2\37\u010e\3\2\2\2!\u0112\3\2\2\2#\u0117\3\2\2\2%\u011d\3\2\2\2\'"+
		"\u0124\3\2\2\2)\u0126\3\2\2\2+\u0128\3\2\2\2-\u012a\3\2\2\2/\u0133\3\2"+
		"\2\2\61\u0139\3\2\2\2\63\u013f\3\2\2\2\65\u0146\3\2\2\2\67\u0148\3\2\2"+
		"\29\u014a\3\2\2\2;\u014c\3\2\2\2=\u014e\3\2\2\2?\u0150\3\2\2\2A\u0152"+
		"\3\2\2\2C\u0154\3\2\2\2E\u0157\3\2\2\2G\u015a\3\2\2\2I\u015c\3\2\2\2K"+
		"\u015f\3\2\2\2M\u0161\3\2\2\2O\u0163\3\2\2\2Q\u0166\3\2\2\2S\u0169\3\2"+
		"\2\2U\u016b\3\2\2\2W\u016d\3\2\2\2Y\u016f\3\2\2\2[\u0171\3\2\2\2]\u0175"+
		"\3\2\2\2_\u017a\3\2\2\2a\u0186\3\2\2\2c\u018f\3\2\2\2e\u0195\3\2\2\2g"+
		"\u019e\3\2\2\2i\u01a4\3\2\2\2k\u01aa\3\2\2\2m\u01b2\3\2\2\2o\u01bc\3\2"+
		"\2\2q\u01c2\3\2\2\2s\u01c5\3\2\2\2u\u01ca\3\2\2\2w\u01d0\3\2\2\2y\u01db"+
		"\3\2\2\2{\u01df\3\2\2\2}\u01e2\3\2\2\2\177\u01e7\3\2\2\2\u0081\u01ea\3"+
		"\2\2\2\u0083\u01ed\3\2\2\2\u0085\u0201\3\2\2\2\u0087\u0217\3\2\2\2\u0089"+
		"\u0236\3\2\2\2\u008b\u0238\3\2\2\2\u008d\u023b\3\2\2\2\u008f\u023e\3\2"+
		"\2\2\u0091\u0241\3\2\2\2\u0093\u0244\3\2\2\2\u0095\u0247\3\2\2\2\u0097"+
		"\u024a\3\2\2\2\u0099\u0253\3\2\2\2\u009b\u025d\3\2\2\2\u009d\u0267\3\2"+
		"\2\2\u009f\u027d\3\2\2\2\u00a1\u0293\3\2\2\2\u00a3\u0296\3\2\2\2\u00a5"+
		"\u029f\3\2\2\2\u00a7\u02aa\3\2\2\2\u00a9\u02ae\3\2\2\2\u00ab\u02bb\3\2"+
		"\2\2\u00ad\u02bd\3\2\2\2\u00af\u02ca\3\2\2\2\u00b1\u02d6\3\2\2\2\u00b3"+
		"\u02d8\3\2\2\2\u00b5\u02db\3\2\2\2\u00b7\u00b8\7D\2\2\u00b8\u00b9\7C\2"+
		"\2\u00b9\u00ba\7U\2\2\u00ba\u00bb\7G\2\2\u00bb\4\3\2\2\2\u00bc\u00bd\7"+
		"R\2\2\u00bd\u00be\7T\2\2\u00be\u00bf\7G\2\2\u00bf\u00c0\7H\2\2\u00c0\u00c1"+
		"\7K\2\2\u00c1\u00c2\7Z\2\2\u00c2\6\3\2\2\2\u00c3\u00c4\7U\2\2\u00c4\u00c5"+
		"\7G\2\2\u00c5\u00c6\7N\2\2\u00c6\u00c7\7G\2\2\u00c7\u00c8\7E\2\2\u00c8"+
		"\u00c9\7V\2\2\u00c9\b\3\2\2\2\u00ca\u00cb\7F\2\2\u00cb\u00cc\7K\2\2\u00cc"+
		"\u00cd\7U\2\2\u00cd\u00ce\7V\2\2\u00ce\u00cf\7K\2\2\u00cf\u00d0\7P\2\2"+
		"\u00d0\u00d1\7E\2\2\u00d1\u00d2\7V\2\2\u00d2\n\3\2\2\2\u00d3\u00d4\7T"+
		"\2\2\u00d4\u00d5\7G\2\2\u00d5\u00d6\7F\2\2\u00d6\u00d7\7W\2\2\u00d7\u00d8"+
		"\7E\2\2\u00d8\u00d9\7G\2\2\u00d9\u00da\7F\2\2\u00da\f\3\2\2\2\u00db\u00dc"+
		"\7,\2\2\u00dc\16\3\2\2\2\u00dd\u00de\7E\2\2\u00de\u00df\7Q\2\2\u00df\u00e0"+
		"\7P\2\2\u00e0\u00e1\7U\2\2\u00e1\u00e2\7V\2\2\u00e2\u00e3\7T\2\2\u00e3"+
		"\u00e4\7W\2\2\u00e4\u00e5\7E\2\2\u00e5\u00e6\7V\2\2\u00e6\20\3\2\2\2\u00e7"+
		"\u00e8\7F\2\2\u00e8\u00e9\7G\2\2\u00e9\u00ea\7U\2\2\u00ea\u00eb\7E\2\2"+
		"\u00eb\u00ec\7T\2\2\u00ec\u00ed\7K\2\2\u00ed\u00ee\7D\2\2\u00ee\u00ef"+
		"\7G\2\2\u00ef\22\3\2\2\2\u00f0\u00f1\7C\2\2\u00f1\u00f2\7U\2\2\u00f2\u00f3"+
		"\7M\2\2\u00f3\24\3\2\2\2\u00f4\u00f5\7H\2\2\u00f5\u00f6\7T\2\2\u00f6\u00f7"+
		"\7Q\2\2\u00f7\u00f8\7O\2\2\u00f8\26\3\2\2\2\u00f9\u00fa\7P\2\2\u00fa\u00fb"+
		"\7C\2\2\u00fb\u00fc\7O\2\2\u00fc\u00fd\7G\2\2\u00fd\u00fe\7F\2\2\u00fe"+
		"\30\3\2\2\2\u00ff\u0100\7Y\2\2\u0100\u0101\7J\2\2\u0101\u0102\7G\2\2\u0102"+
		"\u0103\7T\2\2\u0103\u0104\7G\2\2\u0104\32\3\2\2\2\u0105\u0106\7Q\2\2\u0106"+
		"\u0107\7T\2\2\u0107\u0108\7F\2\2\u0108\u0109\7G\2\2\u0109\u010a\7T\2\2"+
		"\u010a\34\3\2\2\2\u010b\u010c\7D\2\2\u010c\u010d\7[\2\2\u010d\36\3\2\2"+
		"\2\u010e\u010f\7C\2\2\u010f\u0110\7U\2\2\u0110\u0111\7E\2\2\u0111 \3\2"+
		"\2\2\u0112\u0113\7F\2\2\u0113\u0114\7G\2\2\u0114\u0115\7U\2\2\u0115\u0116"+
		"\7E\2\2\u0116\"\3\2\2\2\u0117\u0118\7N\2\2\u0118\u0119\7K\2\2\u0119\u011a"+
		"\7O\2\2\u011a\u011b\7K\2\2\u011b\u011c\7V\2\2\u011c$\3\2\2\2\u011d\u011e"+
		"\7Q\2\2\u011e\u011f\7H\2\2\u011f\u0120\7H\2\2\u0120\u0121\7U\2\2\u0121"+
		"\u0122\7G\2\2\u0122\u0123\7V\2\2\u0123&\3\2\2\2\u0124\u0125\7}\2\2\u0125"+
		"(\3\2\2\2\u0126\u0127\7\60\2\2\u0127*\3\2\2\2\u0128\u0129\7\177\2\2\u0129"+
		",\3\2\2\2\u012a\u012b\7Q\2\2\u012b\u012c\7R\2\2\u012c\u012d\7V\2\2\u012d"+
		"\u012e\7K\2\2\u012e\u012f\7Q\2\2\u012f\u0130\7P\2\2\u0130\u0131\7C\2\2"+
		"\u0131\u0132\7N\2\2\u0132.\3\2\2\2\u0133\u0134\7I\2\2\u0134\u0135\7T\2"+
		"\2\u0135\u0136\7C\2\2\u0136\u0137\7R\2\2\u0137\u0138\7J\2\2\u0138\60\3"+
		"\2\2\2\u0139\u013a\7W\2\2\u013a\u013b\7P\2\2\u013b\u013c\7K\2\2\u013c"+
		"\u013d\7Q\2\2\u013d\u013e\7P\2\2\u013e\62\3\2\2\2\u013f\u0140\7H\2\2\u0140"+
		"\u0141\7K\2\2\u0141\u0142\7N\2\2\u0142\u0143\7V\2\2\u0143\u0144\7G\2\2"+
		"\u0144\u0145\7T\2\2\u0145\64\3\2\2\2\u0146\u0147\7*\2\2\u0147\66\3\2\2"+
		"\2\u0148\u0149\7.\2\2\u01498\3\2\2\2\u014a\u014b\7+\2\2\u014b:\3\2\2\2"+
		"\u014c\u014d\7=\2\2\u014d<\3\2\2\2\u014e\u014f\7c\2\2\u014f>\3\2\2\2\u0150"+
		"\u0151\7]\2\2\u0151@\3\2\2\2\u0152\u0153\7_\2\2\u0153B\3\2\2\2\u0154\u0155"+
		"\7~\2\2\u0155\u0156\7~\2\2\u0156D\3\2\2\2\u0157\u0158\7(\2\2\u0158\u0159"+
		"\7(\2\2\u0159F\3\2\2\2\u015a\u015b\7?\2\2\u015bH\3\2\2\2\u015c\u015d\7"+
		"#\2\2\u015d\u015e\7?\2\2\u015eJ\3\2\2\2\u015f\u0160\7>\2\2\u0160L\3\2"+
		"\2\2\u0161\u0162\7@\2\2\u0162N\3\2\2\2\u0163\u0164\7>\2\2\u0164\u0165"+
		"\7?\2\2\u0165P\3\2\2\2\u0166\u0167\7@\2\2\u0167\u0168\7?\2\2\u0168R\3"+
		"\2\2\2\u0169\u016a\7-\2\2\u016aT\3\2\2\2\u016b\u016c\7/\2\2\u016cV\3\2"+
		"\2\2\u016d\u016e\7\61\2\2\u016eX\3\2\2\2\u016f\u0170\7#\2\2\u0170Z\3\2"+
		"\2\2\u0171\u0172\7U\2\2\u0172\u0173\7V\2\2\u0173\u0174\7T\2\2\u0174\\"+
		"\3\2\2\2\u0175\u0176\7N\2\2\u0176\u0177\7C\2\2\u0177\u0178\7P\2\2\u0178"+
		"\u0179\7I\2\2\u0179^\3\2\2\2\u017a\u017b\7N\2\2\u017b\u017c\7C\2\2\u017c"+
		"\u017d\7P\2\2\u017d\u017e\7I\2\2\u017e\u017f\7O\2\2\u017f\u0180\7C\2\2"+
		"\u0180\u0181\7V\2\2\u0181\u0182\7E\2\2\u0182\u0183\7J\2\2\u0183\u0184"+
		"\7G\2\2\u0184\u0185\7U\2\2\u0185`\3\2\2\2\u0186\u0187\7F\2\2\u0187\u0188"+
		"\7C\2\2\u0188\u0189\7V\2\2\u0189\u018a\7C\2\2\u018a\u018b\7V\2\2\u018b"+
		"\u018c\7[\2\2\u018c\u018d\7R\2\2\u018d\u018e\7G\2\2\u018eb\3\2\2\2\u018f"+
		"\u0190\7D\2\2\u0190\u0191\7Q\2\2\u0191\u0192\7W\2\2\u0192\u0193\7P\2\2"+
		"\u0193\u0194\7F\2\2\u0194d\3\2\2\2\u0195\u0196\7u\2\2\u0196\u0197\7c\2"+
		"\2\u0197\u0198\7o\2\2\u0198\u0199\7g\2\2\u0199\u019a\7V\2\2\u019a\u019b"+
		"\7g\2\2\u019b\u019c\7t\2\2\u019c\u019d\7o\2\2\u019df\3\2\2\2\u019e\u019f"+
		"\7k\2\2\u019f\u01a0\7u\2\2\u01a0\u01a1\7K\2\2\u01a1\u01a2\7T\2\2\u01a2"+
		"\u01a3\7K\2\2\u01a3h\3\2\2\2\u01a4\u01a5\7k\2\2\u01a5\u01a6\7u\2\2\u01a6"+
		"\u01a7\7W\2\2\u01a7\u01a8\7T\2\2\u01a8\u01a9\7K\2\2\u01a9j\3\2\2\2\u01aa"+
		"\u01ab\7k\2\2\u01ab\u01ac\7u\2\2\u01ac\u01ad\7D\2\2\u01ad\u01ae\7N\2\2"+
		"\u01ae\u01af\7C\2\2\u01af\u01b0\7P\2\2\u01b0\u01b1\7M\2\2\u01b1l\3\2\2"+
		"\2\u01b2\u01b3\7k\2\2\u01b3\u01b4\7u\2\2\u01b4\u01b5\7N\2\2\u01b5\u01b6"+
		"\7K\2\2\u01b6\u01b7\7V\2\2\u01b7\u01b8\7G\2\2\u01b8\u01b9\7T\2\2\u01b9"+
		"\u01ba\7C\2\2\u01ba\u01bb\7N\2\2\u01bbn\3\2\2\2\u01bc\u01bd\7T\2\2\u01bd"+
		"\u01be\7G\2\2\u01be\u01bf\7I\2\2\u01bf\u01c0\7G\2\2\u01c0\u01c1\7Z\2\2"+
		"\u01c1p\3\2\2\2\u01c2\u01c3\7`\2\2\u01c3\u01c4\7`\2\2\u01c4r\3\2\2\2\u01c5"+
		"\u01c6\7v\2\2\u01c6\u01c7\7t\2\2\u01c7\u01c8\7w\2\2\u01c8\u01c9\7g\2\2"+
		"\u01c9t\3\2\2\2\u01ca\u01cb\7h\2\2\u01cb\u01cc\7c\2\2\u01cc\u01cd\7n\2"+
		"\2\u01cd\u01ce\7u\2\2\u01ce\u01cf\7g\2\2\u01cfv\3\2\2\2\u01d0\u01d5\7"+
		">\2\2\u01d1\u01d4\n\2\2\2\u01d2\u01d4\5\u00abV\2\u01d3\u01d1\3\2\2\2\u01d3"+
		"\u01d2\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d6\3\2"+
		"\2\2\u01d6\u01d8\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01d9\7@\2\2\u01d9"+
		"x\3\2\2\2\u01da\u01dc\5\u00adW\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2\2"+
		"\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\7<\2\2\u01dez\3\2\2\2\u01df\u01e0\5"+
		"y=\2\u01e0\u01e1\5\u00afX\2\u01e1|\3\2\2\2\u01e2\u01e3\7a\2\2\u01e3\u01e4"+
		"\7<\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6\5\u00afX\2\u01e6~\3\2\2\2\u01e7"+
		"\u01e8\7A\2\2\u01e8\u01e9\5\u00a9U\2\u01e9\u0080\3\2\2\2\u01ea\u01eb\7"+
		"&\2\2\u01eb\u01ec\5\u00a9U\2\u01ec\u0082\3\2\2\2\u01ed\u01ef\7B\2\2\u01ee"+
		"\u01f0\5\u00b1Y\2\u01ef\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01ef"+
		"\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01fd\3\2\2\2\u01f3\u01f7\7/\2\2\u01f4"+
		"\u01f5\5\u00b1Y\2\u01f5\u01f6\5\u00b3Z\2\u01f6\u01f8\3\2\2\2\u01f7\u01f4"+
		"\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa"+
		"\u01fc\3\2\2\2\u01fb\u01f3\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fb\3\2"+
		"\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0084\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200"+
		"\u0202\5\u00b3Z\2\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0201"+
		"\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0086\3\2\2\2\u0205\u0207\5\u00b3Z"+
		"\2\u0206\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0209"+
		"\3\2\2\2\u0209\u020a\3\2\2\2\u020a\u020e\7\60\2\2\u020b\u020d\5\u00b3"+
		"Z\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e"+
		"\u020f\3\2\2\2\u020f\u0218\3\2\2\2\u0210\u020e\3\2\2\2\u0211\u0213\7\60"+
		"\2\2\u0212\u0214\5\u00b3Z\2\u0213\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215"+
		"\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0218\3\2\2\2\u0217\u0206\3\2"+
		"\2\2\u0217\u0211\3\2\2\2\u0218\u0088\3\2\2\2\u0219\u021b\5\u00b3Z\2\u021a"+
		"\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2"+
		"\2\2\u021d\u021e\3\2\2\2\u021e\u0222\7\60\2\2\u021f\u0221\5\u00b3Z\2\u0220"+
		"\u021f\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2"+
		"\2\2\u0223\u0225\3\2\2\2\u0224\u0222\3\2\2\2\u0225\u0226\5\u0097L\2\u0226"+
		"\u0237\3\2\2\2\u0227\u0229\7\60\2\2\u0228\u022a\5\u00b3Z\2\u0229\u0228"+
		"\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c"+
		"\u022d\3\2\2\2\u022d\u022e\5\u0097L\2\u022e\u0237\3\2\2\2\u022f\u0231"+
		"\5\u00b3Z\2\u0230\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0230\3\2\2"+
		"\2\u0232\u0233\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\5\u0097L\2\u0235"+
		"\u0237\3\2\2\2\u0236\u021a\3\2\2\2\u0236\u0227\3\2\2\2\u0236\u0230\3\2"+
		"\2\2\u0237\u008a\3\2\2\2\u0238\u0239\7-\2\2\u0239\u023a\5\u0085C\2\u023a"+
		"\u008c\3\2\2\2\u023b\u023c\7-\2\2\u023c\u023d\5\u0087D\2\u023d\u008e\3"+
		"\2\2\2\u023e\u023f\7-\2\2\u023f\u0240\5\u0089E\2\u0240\u0090\3\2\2\2\u0241"+
		"\u0242\7/\2\2\u0242\u0243\5\u0085C\2\u0243\u0092\3\2\2\2\u0244\u0245\7"+
		"/\2\2\u0245\u0246\5\u0087D\2\u0246\u0094\3\2\2\2\u0247\u0248\7/\2\2\u0248"+
		"\u0249\5\u0089E\2\u0249\u0096\3\2\2\2\u024a\u024c\t\3\2\2\u024b\u024d"+
		"\t\4\2\2\u024c\u024b\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024f\3\2\2\2\u024e"+
		"\u0250\5\u00b3Z\2\u024f\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251\u024f"+
		"\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0098\3\2\2\2\u0253\u0258\7)\2\2\u0254"+
		"\u0257\n\5\2\2\u0255\u0257\5\u00a1Q\2\u0256\u0254\3\2\2\2\u0256\u0255"+
		"\3\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259"+
		"\u025b\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c\7)\2\2\u025c\u009a\3\2"+
		"\2\2\u025d\u0262\7$\2\2\u025e\u0261\n\6\2\2\u025f\u0261\5\u00a1Q\2\u0260"+
		"\u025e\3\2\2\2\u0260\u025f\3\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2"+
		"\2\2\u0262\u0263\3\2\2\2\u0263\u0265\3\2\2\2\u0264\u0262\3\2\2\2\u0265"+
		"\u0266\7$\2\2\u0266\u009c\3\2\2\2\u0267\u0268\7)\2\2\u0268\u0269\7)\2"+
		"\2\u0269\u026a\7)\2\2\u026a\u0276\3\2\2\2\u026b\u026f\7)\2\2\u026c\u026d"+
		"\7)\2\2\u026d\u026f\7)\2\2\u026e\u026b\3\2\2\2\u026e\u026c\3\2\2\2\u026e"+
		"\u026f\3\2\2\2\u026f\u0272\3\2\2\2\u0270\u0273\n\7\2\2\u0271\u0273\5\u00a1"+
		"Q\2\u0272\u0270\3\2\2\2\u0272\u0271\3\2\2\2\u0273\u0275\3\2\2\2\u0274"+
		"\u026e\3\2\2\2\u0275\u0278\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2"+
		"\2\2\u0277\u0279\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u027a\7)\2\2\u027a"+
		"\u027b\7)\2\2\u027b\u027c\7)\2\2\u027c\u009e\3\2\2\2\u027d\u027e\7$\2"+
		"\2\u027e\u027f\7$\2\2\u027f\u0280\7$\2\2\u0280\u028c\3\2\2\2\u0281\u0285"+
		"\7$\2\2\u0282\u0283\7$\2\2\u0283\u0285\7$\2\2\u0284\u0281\3\2\2\2\u0284"+
		"\u0282\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0288\3\2\2\2\u0286\u0289\n\7"+
		"\2\2\u0287\u0289\5\u00a1Q\2\u0288\u0286\3\2\2\2\u0288\u0287\3\2\2\2\u0289"+
		"\u028b\3\2\2\2\u028a\u0284\3\2\2\2\u028b\u028e\3\2\2\2\u028c\u028a\3\2"+
		"\2\2\u028c\u028d\3\2\2\2\u028d\u028f\3\2\2\2\u028e\u028c\3\2\2\2\u028f"+
		"\u0290\7$\2\2\u0290\u0291\7$\2\2\u0291\u0292\7$\2\2\u0292\u00a0\3\2\2"+
		"\2\u0293\u0294\7^\2\2\u0294\u0295\t\b\2\2\u0295\u00a2\3\2\2\2\u0296\u029a"+
		"\7*\2\2\u0297\u0299\5\u00b5[\2\u0298\u0297\3\2\2\2\u0299\u029c\3\2\2\2"+
		"\u029a\u0298\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u029d\3\2\2\2\u029c\u029a"+
		"\3\2\2\2\u029d\u029e\7+\2\2\u029e\u00a4\3\2\2\2\u029f\u02a3\7]\2\2\u02a0"+
		"\u02a2\5\u00b5[\2\u02a1\u02a0\3\2\2\2\u02a2\u02a5\3\2\2\2\u02a3\u02a1"+
		"\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u02a6\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a6"+
		"\u02a7\7_\2\2\u02a7\u00a6\3\2\2\2\u02a8\u02ab\5\u00b1Y\2\u02a9\u02ab\7"+
		"a\2\2\u02aa\u02a8\3\2\2\2\u02aa\u02a9\3\2\2\2\u02ab\u00a8\3\2\2\2\u02ac"+
		"\u02af\5\u00a7T\2\u02ad\u02af\5\u00b3Z\2\u02ae\u02ac\3\2\2\2\u02ae\u02ad"+
		"\3\2\2\2\u02af\u02b5\3\2\2\2\u02b0\u02b4\5\u00a7T\2\u02b1\u02b4\5\u00b3"+
		"Z\2\u02b2\u02b4\t\t\2\2\u02b3\u02b0\3\2\2\2\u02b3\u02b1\3\2\2\2\u02b3"+
		"\u02b2\3\2\2\2\u02b4\u02b7\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b5\u02b6\3\2"+
		"\2\2\u02b6\u00aa\3\2\2\2\u02b7\u02b5\3\2\2\2\u02b8\u02bc\5\u00a7T\2\u02b9"+
		"\u02bc\7/\2\2\u02ba\u02bc\5\u00b3Z\2\u02bb\u02b8\3\2\2\2\u02bb\u02b9\3"+
		"\2\2\2\u02bb\u02ba\3\2\2\2\u02bc\u00ac\3\2\2\2\u02bd\u02c6\5\u00b1Y\2"+
		"\u02be\u02c1\5\u00abV\2\u02bf\u02c1\7\60\2\2\u02c0\u02be\3\2\2\2\u02c0"+
		"\u02bf\3\2\2\2\u02c1\u02c4\3\2\2\2\u02c2\u02c0\3\2\2\2\u02c2\u02c3\3\2"+
		"\2\2\u02c3\u02c5\3\2\2\2\u02c4\u02c2\3\2\2\2\u02c5\u02c7\5\u00abV\2\u02c6"+
		"\u02c2\3\2\2\2\u02c6\u02c7\3\2\2\2\u02c7\u00ae\3\2\2\2\u02c8\u02cb\5\u00a7"+
		"T\2\u02c9\u02cb\5\u00b3Z\2\u02ca\u02c8\3\2\2\2\u02ca\u02c9\3\2\2\2\u02cb"+
		"\u02d4\3\2\2\2\u02cc\u02cf\5\u00abV\2\u02cd\u02cf\7\60\2\2\u02ce\u02cc"+
		"\3\2\2\2\u02ce\u02cd\3\2\2\2\u02cf\u02d2\3\2\2\2\u02d0\u02ce\3\2\2\2\u02d0"+
		"\u02d1\3\2\2\2\u02d1\u02d3\3\2\2\2\u02d2\u02d0\3\2\2\2\u02d3\u02d5\5\u00ab"+
		"V\2\u02d4\u02d0\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5\u00b0\3\2\2\2\u02d6"+
		"\u02d7\t\n\2\2\u02d7\u00b2\3\2\2\2\u02d8\u02d9\4\62;\2\u02d9\u00b4\3\2"+
		"\2\2\u02da\u02dc\t\13\2\2\u02db\u02da\3\2\2\2\u02dc\u02dd\3\2\2\2\u02dd"+
		"\u02db\3\2\2\2\u02dd\u02de\3\2\2\2\u02de\u02df\3\2\2\2\u02df\u02e0\b["+
		"\2\2\u02e0\u00b6\3\2\2\2.\2\u01d3\u01d5\u01db\u01f1\u01f9\u01fd\u0203"+
		"\u0208\u020e\u0215\u0217\u021c\u0222\u022b\u0232\u0236\u024c\u0251\u0256"+
		"\u0258\u0260\u0262\u026e\u0272\u0276\u0284\u0288\u028c\u029a\u02a3\u02aa"+
		"\u02ae\u02b3\u02b5\u02bb\u02c0\u02c2\u02c6\u02ca\u02ce\u02d0\u02d4\u02dd"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}