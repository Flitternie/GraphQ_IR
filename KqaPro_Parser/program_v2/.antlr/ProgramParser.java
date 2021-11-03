// Generated from /home/lynie/proj/KqaPro_IR/KqaPro_Parser/program_v2/Program.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ProgramParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, WS=38, STRING_LITERAL=39, 
		INTEGER=40, DECIMAL=41, DOUBLE=42, EXPONENT=43, DIGIT=44, FUNC_SEP=45, 
		IN_FUNC_SEP=46;
	public static final int
		RULE_query = 0, RULE_whatEntityQuery = 1, RULE_howManyEntityQuery = 2, 
		RULE_whatAttributeQuery = 3, RULE_whatRelationQuery = 4, RULE_attributeSatisfyQuery = 5, 
		RULE_whatAttributeQualifierQuery = 6, RULE_whatRelationQualifierQuery = 7, 
		RULE_entitySetGroup = 8, RULE_entitySet = 9, RULE_entityFilterByRelation = 10, 
		RULE_entityFilterByAttribute = 11, RULE_entityFilterByConcept = 12, RULE_queryName = 13, 
		RULE_count = 14, RULE_findAll = 15, RULE_setOP = 16, RULE_intersect = 17, 
		RULE_union = 18, RULE_filterAttr = 19, RULE_filterStr = 20, RULE_filterNum = 21, 
		RULE_filterYear = 22, RULE_filterDate = 23, RULE_queryRelation = 24, RULE_select = 25, 
		RULE_queryAttributeUnderCondition = 26, RULE_queryAttribute = 27, RULE_verify = 28, 
		RULE_verifyStr = 29, RULE_verifyNum = 30, RULE_verifyYear = 31, RULE_verifyDate = 32, 
		RULE_queryAttrQualifier = 33, RULE_queryRelationQualifier = 34, RULE_relate = 35, 
		RULE_filterQualifier = 36, RULE_filterStrQualifier = 37, RULE_filterNumQualifier = 38, 
		RULE_filterYearQualifier = 39, RULE_filterDateQualifier = 40, RULE_filterConcept = 41, 
		RULE_entity = 42, RULE_concept = 43, RULE_predicate = 44, RULE_key = 45, 
		RULE_value = 46, RULE_qkey = 47, RULE_qvalue = 48, RULE_topk = 49, RULE_start = 50, 
		RULE_op = 51, RULE_symbolOP = 52, RULE_stringOP = 53, RULE_direction = 54, 
		RULE_string = 55, RULE_date = 56, RULE_year = 57, RULE_number = 58;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "whatEntityQuery", "howManyEntityQuery", "whatAttributeQuery", 
			"whatRelationQuery", "attributeSatisfyQuery", "whatAttributeQualifierQuery", 
			"whatRelationQualifierQuery", "entitySetGroup", "entitySet", "entityFilterByRelation", 
			"entityFilterByAttribute", "entityFilterByConcept", "queryName", "count", 
			"findAll", "setOP", "intersect", "union", "filterAttr", "filterStr", 
			"filterNum", "filterYear", "filterDate", "queryRelation", "select", "queryAttributeUnderCondition", 
			"queryAttribute", "verify", "verifyStr", "verifyNum", "verifyYear", "verifyDate", 
			"queryAttrQualifier", "queryRelationQualifier", "relate", "filterQualifier", 
			"filterStrQualifier", "filterNumQualifier", "filterYearQualifier", "filterDateQualifier", 
			"filterConcept", "entity", "concept", "predicate", "key", "value", "qkey", 
			"qvalue", "topk", "start", "op", "symbolOP", "stringOP", "direction", 
			"string", "date", "year", "number"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'What()'", "'Count()'", "'FindAll()'", "'And()'", "'Or()'", "'FilterStr('", 
			"')'", "'FilterNum('", "'FilterYear('", "'FilterDate('", "'QueryRelation()'", 
			"'Select('", "'QueryAttrUnderCondition('", "'QueryAttr('", "'VerifyStr('", 
			"'VerifyNum('", "'VerifyYear('", "'VerifyDate('", "'QueryAttrQualifier('", 
			"'QueryRelationQualifier('", "'Relate('", "'QFilterStr('", "'QFilterNum('", 
			"'QFilterYear('", "'QFilterDate('", "'FilterConcept('", "'Find('", "'='", 
			"'<'", "'>'", "'!='", "'largest'", "'smallest'", "'forward'", "'backward'", 
			"'('", "'-'", null, null, null, null, null, null, null, "'<b>'", "'<c>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "WS", "STRING_LITERAL", "INTEGER", "DECIMAL", "DOUBLE", "EXPONENT", 
			"DIGIT", "FUNC_SEP", "IN_FUNC_SEP"
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

	@Override
	public String getGrammarFileName() { return "Program.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ProgramParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class QueryContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ProgramParser.EOF, 0); }
		public WhatEntityQueryContext whatEntityQuery() {
			return getRuleContext(WhatEntityQueryContext.class,0);
		}
		public HowManyEntityQueryContext howManyEntityQuery() {
			return getRuleContext(HowManyEntityQueryContext.class,0);
		}
		public WhatAttributeQueryContext whatAttributeQuery() {
			return getRuleContext(WhatAttributeQueryContext.class,0);
		}
		public WhatRelationQueryContext whatRelationQuery() {
			return getRuleContext(WhatRelationQueryContext.class,0);
		}
		public AttributeSatisfyQueryContext attributeSatisfyQuery() {
			return getRuleContext(AttributeSatisfyQueryContext.class,0);
		}
		public WhatAttributeQualifierQueryContext whatAttributeQualifierQuery() {
			return getRuleContext(WhatAttributeQualifierQueryContext.class,0);
		}
		public WhatRelationQualifierQueryContext whatRelationQualifierQuery() {
			return getRuleContext(WhatRelationQualifierQueryContext.class,0);
		}
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(118);
				whatEntityQuery();
				}
				break;
			case 2:
				{
				setState(119);
				howManyEntityQuery();
				}
				break;
			case 3:
				{
				setState(120);
				whatAttributeQuery();
				}
				break;
			case 4:
				{
				setState(121);
				whatRelationQuery();
				}
				break;
			case 5:
				{
				setState(122);
				attributeSatisfyQuery();
				}
				break;
			case 6:
				{
				setState(123);
				whatAttributeQualifierQuery();
				}
				break;
			case 7:
				{
				setState(124);
				whatRelationQualifierQuery();
				}
				break;
			}
			setState(127);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhatEntityQueryContext extends ParserRuleContext {
		public EntitySetContext entitySet() {
			return getRuleContext(EntitySetContext.class,0);
		}
		public QueryNameContext queryName() {
			return getRuleContext(QueryNameContext.class,0);
		}
		public WhatEntityQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whatEntityQuery; }
	}

	public final WhatEntityQueryContext whatEntityQuery() throws RecognitionException {
		WhatEntityQueryContext _localctx = new WhatEntityQueryContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_whatEntityQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			entitySet(0);
			setState(130);
			queryName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class HowManyEntityQueryContext extends ParserRuleContext {
		public EntitySetContext entitySet() {
			return getRuleContext(EntitySetContext.class,0);
		}
		public CountContext count() {
			return getRuleContext(CountContext.class,0);
		}
		public HowManyEntityQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_howManyEntityQuery; }
	}

	public final HowManyEntityQueryContext howManyEntityQuery() throws RecognitionException {
		HowManyEntityQueryContext _localctx = new HowManyEntityQueryContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_howManyEntityQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			entitySet(0);
			setState(133);
			count();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhatAttributeQueryContext extends ParserRuleContext {
		public EntitySetContext entitySet() {
			return getRuleContext(EntitySetContext.class,0);
		}
		public QueryAttributeContext queryAttribute() {
			return getRuleContext(QueryAttributeContext.class,0);
		}
		public WhatAttributeQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whatAttributeQuery; }
	}

	public final WhatAttributeQueryContext whatAttributeQuery() throws RecognitionException {
		WhatAttributeQueryContext _localctx = new WhatAttributeQueryContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_whatAttributeQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			entitySet(0);
			setState(136);
			queryAttribute();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhatRelationQueryContext extends ParserRuleContext {
		public EntitySetGroupContext entitySetGroup() {
			return getRuleContext(EntitySetGroupContext.class,0);
		}
		public QueryRelationContext queryRelation() {
			return getRuleContext(QueryRelationContext.class,0);
		}
		public WhatRelationQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whatRelationQuery; }
	}

	public final WhatRelationQueryContext whatRelationQuery() throws RecognitionException {
		WhatRelationQueryContext _localctx = new WhatRelationQueryContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_whatRelationQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			entitySetGroup();
			setState(139);
			queryRelation();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AttributeSatisfyQueryContext extends ParserRuleContext {
		public EntitySetContext entitySet() {
			return getRuleContext(EntitySetContext.class,0);
		}
		public VerifyContext verify() {
			return getRuleContext(VerifyContext.class,0);
		}
		public QueryAttributeUnderConditionContext queryAttributeUnderCondition() {
			return getRuleContext(QueryAttributeUnderConditionContext.class,0);
		}
		public QueryAttributeContext queryAttribute() {
			return getRuleContext(QueryAttributeContext.class,0);
		}
		public AttributeSatisfyQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeSatisfyQuery; }
	}

	public final AttributeSatisfyQueryContext attributeSatisfyQuery() throws RecognitionException {
		AttributeSatisfyQueryContext _localctx = new AttributeSatisfyQueryContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attributeSatisfyQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			entitySet(0);
			setState(144);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__12:
				{
				setState(142);
				queryAttributeUnderCondition();
				}
				break;
			case T__13:
				{
				setState(143);
				queryAttribute();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(146);
			verify();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhatAttributeQualifierQueryContext extends ParserRuleContext {
		public EntitySetContext entitySet() {
			return getRuleContext(EntitySetContext.class,0);
		}
		public QueryAttrQualifierContext queryAttrQualifier() {
			return getRuleContext(QueryAttrQualifierContext.class,0);
		}
		public WhatAttributeQualifierQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whatAttributeQualifierQuery; }
	}

	public final WhatAttributeQualifierQueryContext whatAttributeQualifierQuery() throws RecognitionException {
		WhatAttributeQualifierQueryContext _localctx = new WhatAttributeQualifierQueryContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_whatAttributeQualifierQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			entitySet(0);
			setState(149);
			queryAttrQualifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhatRelationQualifierQueryContext extends ParserRuleContext {
		public EntitySetGroupContext entitySetGroup() {
			return getRuleContext(EntitySetGroupContext.class,0);
		}
		public QueryRelationQualifierContext queryRelationQualifier() {
			return getRuleContext(QueryRelationQualifierContext.class,0);
		}
		public WhatRelationQualifierQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whatRelationQualifierQuery; }
	}

	public final WhatRelationQualifierQueryContext whatRelationQualifierQuery() throws RecognitionException {
		WhatRelationQualifierQueryContext _localctx = new WhatRelationQualifierQueryContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_whatRelationQualifierQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			entitySetGroup();
			setState(152);
			queryRelationQualifier();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EntitySetGroupContext extends ParserRuleContext {
		public List<EntitySetContext> entitySet() {
			return getRuleContexts(EntitySetContext.class);
		}
		public EntitySetContext entitySet(int i) {
			return getRuleContext(EntitySetContext.class,i);
		}
		public EntitySetGroupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entitySetGroup; }
	}

	public final EntitySetGroupContext entitySetGroup() throws RecognitionException {
		EntitySetGroupContext _localctx = new EntitySetGroupContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_entitySetGroup);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			entitySet(0);
			setState(155);
			entitySet(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EntitySetContext extends ParserRuleContext {
		public EntitySetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entitySet; }
	 
		public EntitySetContext() { }
		public void copyFrom(EntitySetContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class EntitySetByFilterContext extends EntitySetContext {
		public FindAllContext findAll() {
			return getRuleContext(FindAllContext.class,0);
		}
		public EntityFilterByAttributeContext entityFilterByAttribute() {
			return getRuleContext(EntityFilterByAttributeContext.class,0);
		}
		public EntityFilterByConceptContext entityFilterByConcept() {
			return getRuleContext(EntityFilterByConceptContext.class,0);
		}
		public EntitySetByFilterContext(EntitySetContext ctx) { copyFrom(ctx); }
	}
	public static class EntitySetAtomContext extends EntitySetContext {
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
		}
		public EntitySetAtomContext(EntitySetContext ctx) { copyFrom(ctx); }
	}
	public static class EntitySetByRankContext extends EntitySetContext {
		public EntitySetContext entitySet() {
			return getRuleContext(EntitySetContext.class,0);
		}
		public SelectContext select() {
			return getRuleContext(SelectContext.class,0);
		}
		public EntitySetByRankContext(EntitySetContext ctx) { copyFrom(ctx); }
	}
	public static class EntitySetByOPContext extends EntitySetContext {
		public List<EntitySetContext> entitySet() {
			return getRuleContexts(EntitySetContext.class);
		}
		public EntitySetContext entitySet(int i) {
			return getRuleContext(EntitySetContext.class,i);
		}
		public SetOPContext setOP() {
			return getRuleContext(SetOPContext.class,0);
		}
		public EntitySetByOPContext(EntitySetContext ctx) { copyFrom(ctx); }
	}
	public static class EntitySetNestedContext extends EntitySetContext {
		public EntitySetContext entitySet() {
			return getRuleContext(EntitySetContext.class,0);
		}
		public EntityFilterByRelationContext entityFilterByRelation() {
			return getRuleContext(EntityFilterByRelationContext.class,0);
		}
		public EntityFilterByAttributeContext entityFilterByAttribute() {
			return getRuleContext(EntityFilterByAttributeContext.class,0);
		}
		public EntitySetNestedContext(EntitySetContext ctx) { copyFrom(ctx); }
	}

	public final EntitySetContext entitySet() throws RecognitionException {
		return entitySet(0);
	}

	private EntitySetContext entitySet(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		EntitySetContext _localctx = new EntitySetContext(_ctx, _parentState);
		EntitySetContext _prevctx = _localctx;
		int _startState = 18;
		enterRecursionRule(_localctx, 18, RULE_entitySet, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__2:
				{
				_localctx = new EntitySetByFilterContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(158);
				findAll();
				setState(161);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__5:
				case T__7:
				case T__8:
				case T__9:
					{
					setState(159);
					entityFilterByAttribute();
					}
					break;
				case T__25:
					{
					setState(160);
					entityFilterByConcept();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				break;
			case T__26:
				{
				_localctx = new EntitySetAtomContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(163);
				entity();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(179);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(177);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new EntitySetByOPContext(new EntitySetContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_entitySet);
						setState(166);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(167);
						entitySet(0);
						setState(168);
						setOP();
						}
						break;
					case 2:
						{
						_localctx = new EntitySetByRankContext(new EntitySetContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_entitySet);
						setState(170);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(171);
						select();
						}
						break;
					case 3:
						{
						_localctx = new EntitySetNestedContext(new EntitySetContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_entitySet);
						setState(172);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(175);
						_errHandler.sync(this);
						switch (_input.LA(1)) {
						case T__20:
							{
							setState(173);
							entityFilterByRelation();
							}
							break;
						case T__5:
						case T__7:
						case T__8:
						case T__9:
							{
							setState(174);
							entityFilterByAttribute();
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						}
						break;
					}
					} 
				}
				setState(181);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class EntityFilterByRelationContext extends ParserRuleContext {
		public RelateContext relate() {
			return getRuleContext(RelateContext.class,0);
		}
		public FilterQualifierContext filterQualifier() {
			return getRuleContext(FilterQualifierContext.class,0);
		}
		public FilterConceptContext filterConcept() {
			return getRuleContext(FilterConceptContext.class,0);
		}
		public EntityFilterByRelationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityFilterByRelation; }
	}

	public final EntityFilterByRelationContext entityFilterByRelation() throws RecognitionException {
		EntityFilterByRelationContext _localctx = new EntityFilterByRelationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_entityFilterByRelation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			relate();
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				setState(183);
				filterQualifier();
				}
				break;
			}
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(186);
				filterConcept();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EntityFilterByAttributeContext extends ParserRuleContext {
		public FilterAttrContext filterAttr() {
			return getRuleContext(FilterAttrContext.class,0);
		}
		public FilterQualifierContext filterQualifier() {
			return getRuleContext(FilterQualifierContext.class,0);
		}
		public FilterConceptContext filterConcept() {
			return getRuleContext(FilterConceptContext.class,0);
		}
		public EntityFilterByAttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityFilterByAttribute; }
	}

	public final EntityFilterByAttributeContext entityFilterByAttribute() throws RecognitionException {
		EntityFilterByAttributeContext _localctx = new EntityFilterByAttributeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_entityFilterByAttribute);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			filterAttr();
			setState(191);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(190);
				filterQualifier();
				}
				break;
			}
			setState(194);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(193);
				filterConcept();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EntityFilterByConceptContext extends ParserRuleContext {
		public FilterConceptContext filterConcept() {
			return getRuleContext(FilterConceptContext.class,0);
		}
		public EntityFilterByConceptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityFilterByConcept; }
	}

	public final EntityFilterByConceptContext entityFilterByConcept() throws RecognitionException {
		EntityFilterByConceptContext _localctx = new EntityFilterByConceptContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_entityFilterByConcept);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			filterConcept();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QueryNameContext extends ParserRuleContext {
		public QueryNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryName; }
	}

	public final QueryNameContext queryName() throws RecognitionException {
		QueryNameContext _localctx = new QueryNameContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_queryName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(198);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CountContext extends ParserRuleContext {
		public CountContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_count; }
	}

	public final CountContext count() throws RecognitionException {
		CountContext _localctx = new CountContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_count);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FindAllContext extends ParserRuleContext {
		public FindAllContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findAll; }
	}

	public final FindAllContext findAll() throws RecognitionException {
		FindAllContext _localctx = new FindAllContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_findAll);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SetOPContext extends ParserRuleContext {
		public IntersectContext intersect() {
			return getRuleContext(IntersectContext.class,0);
		}
		public UnionContext union() {
			return getRuleContext(UnionContext.class,0);
		}
		public SetOPContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setOP; }
	}

	public final SetOPContext setOP() throws RecognitionException {
		SetOPContext _localctx = new SetOPContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_setOP);
		try {
			setState(206);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(204);
				intersect();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(205);
				union();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IntersectContext extends ParserRuleContext {
		public IntersectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intersect; }
	 
		public IntersectContext() { }
		public void copyFrom(IntersectContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AndContext extends IntersectContext {
		public AndContext(IntersectContext ctx) { copyFrom(ctx); }
	}

	public final IntersectContext intersect() throws RecognitionException {
		IntersectContext _localctx = new IntersectContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_intersect);
		try {
			_localctx = new AndContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnionContext extends ParserRuleContext {
		public UnionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_union; }
	 
		public UnionContext() { }
		public void copyFrom(UnionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class OrContext extends UnionContext {
		public OrContext(UnionContext ctx) { copyFrom(ctx); }
	}

	public final UnionContext union() throws RecognitionException {
		UnionContext _localctx = new UnionContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_union);
		try {
			_localctx = new OrContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(210);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterAttrContext extends ParserRuleContext {
		public FilterStrContext filterStr() {
			return getRuleContext(FilterStrContext.class,0);
		}
		public FilterNumContext filterNum() {
			return getRuleContext(FilterNumContext.class,0);
		}
		public FilterYearContext filterYear() {
			return getRuleContext(FilterYearContext.class,0);
		}
		public FilterDateContext filterDate() {
			return getRuleContext(FilterDateContext.class,0);
		}
		public FilterAttrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterAttr; }
	}

	public final FilterAttrContext filterAttr() throws RecognitionException {
		FilterAttrContext _localctx = new FilterAttrContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_filterAttr);
		try {
			setState(216);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
				enterOuterAlt(_localctx, 1);
				{
				setState(212);
				filterStr();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 2);
				{
				setState(213);
				filterNum();
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 3);
				{
				setState(214);
				filterYear();
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 4);
				{
				setState(215);
				filterDate();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterStrContext extends ParserRuleContext {
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public TerminalNode IN_FUNC_SEP() { return getToken(ProgramParser.IN_FUNC_SEP, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public FilterStrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterStr; }
	}

	public final FilterStrContext filterStr() throws RecognitionException {
		FilterStrContext _localctx = new FilterStrContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_filterStr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			match(T__5);
			setState(219);
			key();
			setState(220);
			match(IN_FUNC_SEP);
			setState(221);
			value();
			setState(222);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterNumContext extends ParserRuleContext {
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public FilterNumContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterNum; }
	}

	public final FilterNumContext filterNum() throws RecognitionException {
		FilterNumContext _localctx = new FilterNumContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_filterNum);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(T__7);
			setState(225);
			key();
			setState(226);
			match(IN_FUNC_SEP);
			setState(227);
			value();
			setState(228);
			match(IN_FUNC_SEP);
			setState(229);
			op();
			setState(230);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterYearContext extends ParserRuleContext {
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public FilterYearContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterYear; }
	}

	public final FilterYearContext filterYear() throws RecognitionException {
		FilterYearContext _localctx = new FilterYearContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_filterYear);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(T__8);
			setState(233);
			key();
			setState(234);
			match(IN_FUNC_SEP);
			setState(235);
			value();
			setState(236);
			match(IN_FUNC_SEP);
			setState(237);
			op();
			setState(238);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterDateContext extends ParserRuleContext {
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public FilterDateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterDate; }
	}

	public final FilterDateContext filterDate() throws RecognitionException {
		FilterDateContext _localctx = new FilterDateContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_filterDate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			match(T__9);
			setState(241);
			key();
			setState(242);
			match(IN_FUNC_SEP);
			setState(243);
			value();
			setState(244);
			match(IN_FUNC_SEP);
			setState(245);
			op();
			setState(246);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QueryRelationContext extends ParserRuleContext {
		public QueryRelationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryRelation; }
	}

	public final QueryRelationContext queryRelation() throws RecognitionException {
		QueryRelationContext _localctx = new QueryRelationContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_queryRelation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			match(T__10);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SelectContext extends ParserRuleContext {
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public TopkContext topk() {
			return getRuleContext(TopkContext.class,0);
		}
		public StartContext start() {
			return getRuleContext(StartContext.class,0);
		}
		public SelectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_select; }
	}

	public final SelectContext select() throws RecognitionException {
		SelectContext _localctx = new SelectContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_select);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(T__11);
			setState(251);
			key();
			setState(252);
			match(IN_FUNC_SEP);
			setState(253);
			op();
			setState(254);
			match(IN_FUNC_SEP);
			setState(255);
			topk();
			setState(256);
			match(IN_FUNC_SEP);
			setState(257);
			start();
			setState(258);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QueryAttributeUnderConditionContext extends ParserRuleContext {
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public QkeyContext qkey() {
			return getRuleContext(QkeyContext.class,0);
		}
		public QvalueContext qvalue() {
			return getRuleContext(QvalueContext.class,0);
		}
		public QueryAttributeUnderConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryAttributeUnderCondition; }
	}

	public final QueryAttributeUnderConditionContext queryAttributeUnderCondition() throws RecognitionException {
		QueryAttributeUnderConditionContext _localctx = new QueryAttributeUnderConditionContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_queryAttributeUnderCondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			match(T__12);
			setState(261);
			key();
			setState(262);
			match(IN_FUNC_SEP);
			setState(263);
			qkey();
			setState(264);
			match(IN_FUNC_SEP);
			setState(265);
			qvalue();
			setState(266);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QueryAttributeContext extends ParserRuleContext {
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public QueryAttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryAttribute; }
	}

	public final QueryAttributeContext queryAttribute() throws RecognitionException {
		QueryAttributeContext _localctx = new QueryAttributeContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_queryAttribute);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(268);
			match(T__13);
			setState(269);
			key();
			setState(270);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VerifyContext extends ParserRuleContext {
		public VerifyStrContext verifyStr() {
			return getRuleContext(VerifyStrContext.class,0);
		}
		public VerifyNumContext verifyNum() {
			return getRuleContext(VerifyNumContext.class,0);
		}
		public VerifyYearContext verifyYear() {
			return getRuleContext(VerifyYearContext.class,0);
		}
		public VerifyDateContext verifyDate() {
			return getRuleContext(VerifyDateContext.class,0);
		}
		public VerifyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verify; }
	}

	public final VerifyContext verify() throws RecognitionException {
		VerifyContext _localctx = new VerifyContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_verify);
		try {
			setState(276);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__14:
				enterOuterAlt(_localctx, 1);
				{
				setState(272);
				verifyStr();
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 2);
				{
				setState(273);
				verifyNum();
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 3);
				{
				setState(274);
				verifyYear();
				}
				break;
			case T__17:
				enterOuterAlt(_localctx, 4);
				{
				setState(275);
				verifyDate();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VerifyStrContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public VerifyStrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verifyStr; }
	}

	public final VerifyStrContext verifyStr() throws RecognitionException {
		VerifyStrContext _localctx = new VerifyStrContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_verifyStr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			match(T__14);
			setState(279);
			value();
			setState(280);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VerifyNumContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode IN_FUNC_SEP() { return getToken(ProgramParser.IN_FUNC_SEP, 0); }
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public VerifyNumContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verifyNum; }
	}

	public final VerifyNumContext verifyNum() throws RecognitionException {
		VerifyNumContext _localctx = new VerifyNumContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_verifyNum);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
			match(T__15);
			setState(283);
			value();
			setState(284);
			match(IN_FUNC_SEP);
			setState(285);
			op();
			setState(286);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VerifyYearContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode IN_FUNC_SEP() { return getToken(ProgramParser.IN_FUNC_SEP, 0); }
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public VerifyYearContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verifyYear; }
	}

	public final VerifyYearContext verifyYear() throws RecognitionException {
		VerifyYearContext _localctx = new VerifyYearContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_verifyYear);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			match(T__16);
			setState(289);
			value();
			setState(290);
			match(IN_FUNC_SEP);
			setState(291);
			op();
			setState(292);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VerifyDateContext extends ParserRuleContext {
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode IN_FUNC_SEP() { return getToken(ProgramParser.IN_FUNC_SEP, 0); }
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public VerifyDateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_verifyDate; }
	}

	public final VerifyDateContext verifyDate() throws RecognitionException {
		VerifyDateContext _localctx = new VerifyDateContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_verifyDate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(294);
			match(T__17);
			setState(295);
			value();
			setState(296);
			match(IN_FUNC_SEP);
			setState(297);
			op();
			setState(298);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QueryAttrQualifierContext extends ParserRuleContext {
		public KeyContext key() {
			return getRuleContext(KeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public QkeyContext qkey() {
			return getRuleContext(QkeyContext.class,0);
		}
		public QueryAttrQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryAttrQualifier; }
	}

	public final QueryAttrQualifierContext queryAttrQualifier() throws RecognitionException {
		QueryAttrQualifierContext _localctx = new QueryAttrQualifierContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_queryAttrQualifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			match(T__18);
			setState(301);
			key();
			setState(302);
			match(IN_FUNC_SEP);
			setState(303);
			value();
			setState(304);
			match(IN_FUNC_SEP);
			setState(305);
			qkey();
			setState(306);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QueryRelationQualifierContext extends ParserRuleContext {
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public TerminalNode IN_FUNC_SEP() { return getToken(ProgramParser.IN_FUNC_SEP, 0); }
		public QkeyContext qkey() {
			return getRuleContext(QkeyContext.class,0);
		}
		public QueryRelationQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryRelationQualifier; }
	}

	public final QueryRelationQualifierContext queryRelationQualifier() throws RecognitionException {
		QueryRelationQualifierContext _localctx = new QueryRelationQualifierContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_queryRelationQualifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(308);
			match(T__19);
			setState(309);
			predicate();
			setState(310);
			match(IN_FUNC_SEP);
			setState(311);
			qkey();
			setState(312);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RelateContext extends ParserRuleContext {
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public TerminalNode IN_FUNC_SEP() { return getToken(ProgramParser.IN_FUNC_SEP, 0); }
		public DirectionContext direction() {
			return getRuleContext(DirectionContext.class,0);
		}
		public RelateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relate; }
	}

	public final RelateContext relate() throws RecognitionException {
		RelateContext _localctx = new RelateContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_relate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			match(T__20);
			setState(315);
			predicate();
			setState(316);
			match(IN_FUNC_SEP);
			setState(317);
			direction();
			setState(318);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterQualifierContext extends ParserRuleContext {
		public FilterStrQualifierContext filterStrQualifier() {
			return getRuleContext(FilterStrQualifierContext.class,0);
		}
		public FilterNumQualifierContext filterNumQualifier() {
			return getRuleContext(FilterNumQualifierContext.class,0);
		}
		public FilterYearQualifierContext filterYearQualifier() {
			return getRuleContext(FilterYearQualifierContext.class,0);
		}
		public FilterDateQualifierContext filterDateQualifier() {
			return getRuleContext(FilterDateQualifierContext.class,0);
		}
		public FilterQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterQualifier; }
	}

	public final FilterQualifierContext filterQualifier() throws RecognitionException {
		FilterQualifierContext _localctx = new FilterQualifierContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_filterQualifier);
		try {
			setState(324);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__21:
				enterOuterAlt(_localctx, 1);
				{
				setState(320);
				filterStrQualifier();
				}
				break;
			case T__22:
				enterOuterAlt(_localctx, 2);
				{
				setState(321);
				filterNumQualifier();
				}
				break;
			case T__23:
				enterOuterAlt(_localctx, 3);
				{
				setState(322);
				filterYearQualifier();
				}
				break;
			case T__24:
				enterOuterAlt(_localctx, 4);
				{
				setState(323);
				filterDateQualifier();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterStrQualifierContext extends ParserRuleContext {
		public QkeyContext qkey() {
			return getRuleContext(QkeyContext.class,0);
		}
		public TerminalNode IN_FUNC_SEP() { return getToken(ProgramParser.IN_FUNC_SEP, 0); }
		public QvalueContext qvalue() {
			return getRuleContext(QvalueContext.class,0);
		}
		public FilterStrQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterStrQualifier; }
	}

	public final FilterStrQualifierContext filterStrQualifier() throws RecognitionException {
		FilterStrQualifierContext _localctx = new FilterStrQualifierContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_filterStrQualifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			match(T__21);
			setState(327);
			qkey();
			setState(328);
			match(IN_FUNC_SEP);
			setState(329);
			qvalue();
			setState(330);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterNumQualifierContext extends ParserRuleContext {
		public QkeyContext qkey() {
			return getRuleContext(QkeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public QvalueContext qvalue() {
			return getRuleContext(QvalueContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public FilterNumQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterNumQualifier; }
	}

	public final FilterNumQualifierContext filterNumQualifier() throws RecognitionException {
		FilterNumQualifierContext _localctx = new FilterNumQualifierContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_filterNumQualifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(332);
			match(T__22);
			setState(333);
			qkey();
			setState(334);
			match(IN_FUNC_SEP);
			setState(335);
			qvalue();
			setState(336);
			match(IN_FUNC_SEP);
			setState(337);
			op();
			setState(338);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterYearQualifierContext extends ParserRuleContext {
		public QkeyContext qkey() {
			return getRuleContext(QkeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public QvalueContext qvalue() {
			return getRuleContext(QvalueContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public FilterYearQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterYearQualifier; }
	}

	public final FilterYearQualifierContext filterYearQualifier() throws RecognitionException {
		FilterYearQualifierContext _localctx = new FilterYearQualifierContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_filterYearQualifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(340);
			match(T__23);
			setState(341);
			qkey();
			setState(342);
			match(IN_FUNC_SEP);
			setState(343);
			qvalue();
			setState(344);
			match(IN_FUNC_SEP);
			setState(345);
			op();
			setState(346);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterDateQualifierContext extends ParserRuleContext {
		public QkeyContext qkey() {
			return getRuleContext(QkeyContext.class,0);
		}
		public List<TerminalNode> IN_FUNC_SEP() { return getTokens(ProgramParser.IN_FUNC_SEP); }
		public TerminalNode IN_FUNC_SEP(int i) {
			return getToken(ProgramParser.IN_FUNC_SEP, i);
		}
		public QvalueContext qvalue() {
			return getRuleContext(QvalueContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public FilterDateQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterDateQualifier; }
	}

	public final FilterDateQualifierContext filterDateQualifier() throws RecognitionException {
		FilterDateQualifierContext _localctx = new FilterDateQualifierContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_filterDateQualifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(348);
			match(T__24);
			setState(349);
			qkey();
			setState(350);
			match(IN_FUNC_SEP);
			setState(351);
			qvalue();
			setState(352);
			match(IN_FUNC_SEP);
			setState(353);
			op();
			setState(354);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FilterConceptContext extends ParserRuleContext {
		public ConceptContext concept() {
			return getRuleContext(ConceptContext.class,0);
		}
		public FilterConceptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_filterConcept; }
	}

	public final FilterConceptContext filterConcept() throws RecognitionException {
		FilterConceptContext _localctx = new FilterConceptContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_filterConcept);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(356);
			match(T__25);
			setState(357);
			concept();
			setState(358);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class EntityContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public EntityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity; }
	}

	public final EntityContext entity() throws RecognitionException {
		EntityContext _localctx = new EntityContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_entity);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(360);
			match(T__26);
			setState(361);
			string();
			setState(362);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConceptContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public ConceptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concept; }
	}

	public final ConceptContext concept() throws RecognitionException {
		ConceptContext _localctx = new ConceptContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_concept);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(364);
			string();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PredicateContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public PredicateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicate; }
	}

	public final PredicateContext predicate() throws RecognitionException {
		PredicateContext _localctx = new PredicateContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_predicate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366);
			string();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class KeyContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public KeyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_key; }
	}

	public final KeyContext key() throws RecognitionException {
		KeyContext _localctx = new KeyContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_key);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(368);
			string();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ValueContext extends ParserRuleContext {
		public DateContext date() {
			return getRuleContext(DateContext.class,0);
		}
		public YearContext year() {
			return getRuleContext(YearContext.class,0);
		}
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_value);
		try {
			setState(374);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(370);
				date();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(371);
				year();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(372);
				number();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(373);
				string();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QkeyContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public QkeyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qkey; }
	}

	public final QkeyContext qkey() throws RecognitionException {
		QkeyContext _localctx = new QkeyContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_qkey);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			string();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class QvalueContext extends ParserRuleContext {
		public DateContext date() {
			return getRuleContext(DateContext.class,0);
		}
		public YearContext year() {
			return getRuleContext(YearContext.class,0);
		}
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public QvalueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qvalue; }
	}

	public final QvalueContext qvalue() throws RecognitionException {
		QvalueContext _localctx = new QvalueContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_qvalue);
		try {
			setState(382);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(378);
				date();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(379);
				year();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(380);
				number();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(381);
				string();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TopkContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public TopkContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topk; }
	}

	public final TopkContext topk() throws RecognitionException {
		TopkContext _localctx = new TopkContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_topk);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			string();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StartContext extends ParserRuleContext {
		public StringContext string() {
			return getRuleContext(StringContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(386);
			string();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OpContext extends ParserRuleContext {
		public SymbolOPContext symbolOP() {
			return getRuleContext(SymbolOPContext.class,0);
		}
		public StringOPContext stringOP() {
			return getRuleContext(StringOPContext.class,0);
		}
		public OpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op; }
	}

	public final OpContext op() throws RecognitionException {
		OpContext _localctx = new OpContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_op);
		try {
			setState(390);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__27:
			case T__28:
			case T__29:
			case T__30:
				enterOuterAlt(_localctx, 1);
				{
				setState(388);
				symbolOP();
				}
				break;
			case T__31:
			case T__32:
				enterOuterAlt(_localctx, 2);
				{
				setState(389);
				stringOP();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SymbolOPContext extends ParserRuleContext {
		public SymbolOPContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_symbolOP; }
	}

	public final SymbolOPContext symbolOP() throws RecognitionException {
		SymbolOPContext _localctx = new SymbolOPContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_symbolOP);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(392);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__27) | (1L << T__28) | (1L << T__29) | (1L << T__30))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StringOPContext extends ParserRuleContext {
		public StringOPContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringOP; }
	}

	public final StringOPContext stringOP() throws RecognitionException {
		StringOPContext _localctx = new StringOPContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_stringOP);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(394);
			_la = _input.LA(1);
			if ( !(_la==T__31 || _la==T__32) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DirectionContext extends ParserRuleContext {
		public DirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_direction; }
	}

	public final DirectionContext direction() throws RecognitionException {
		DirectionContext _localctx = new DirectionContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_direction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(396);
			_la = _input.LA(1);
			if ( !(_la==T__33 || _la==T__34) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StringContext extends ParserRuleContext {
		public List<TerminalNode> STRING_LITERAL() { return getTokens(ProgramParser.STRING_LITERAL); }
		public TerminalNode STRING_LITERAL(int i) {
			return getToken(ProgramParser.STRING_LITERAL, i);
		}
		public List<StringContext> string() {
			return getRuleContexts(StringContext.class);
		}
		public StringContext string(int i) {
			return getRuleContext(StringContext.class,i);
		}
		public List<DirectionContext> direction() {
			return getRuleContexts(DirectionContext.class);
		}
		public DirectionContext direction(int i) {
			return getRuleContext(DirectionContext.class,i);
		}
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_string);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(404); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(404);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case STRING_LITERAL:
					{
					setState(398);
					match(STRING_LITERAL);
					}
					break;
				case T__35:
					{
					setState(399);
					match(T__35);
					setState(400);
					string();
					setState(401);
					match(T__6);
					}
					break;
				case T__33:
				case T__34:
					{
					setState(403);
					direction();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(406); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__33) | (1L << T__34) | (1L << T__35) | (1L << STRING_LITERAL))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DateContext extends ParserRuleContext {
		public List<TerminalNode> DIGIT() { return getTokens(ProgramParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(ProgramParser.DIGIT, i);
		}
		public DateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_date; }
	}

	public final DateContext date() throws RecognitionException {
		DateContext _localctx = new DateContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_date);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(409); 
			_errHandler.sync(this);
			_alt = 1+1;
			do {
				switch (_alt) {
				case 1+1:
					{
					{
					setState(408);
					match(DIGIT);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(411); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			} while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(413);
			match(T__36);
			setState(415); 
			_errHandler.sync(this);
			_alt = 1+1;
			do {
				switch (_alt) {
				case 1+1:
					{
					{
					setState(414);
					match(DIGIT);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(417); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			} while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(419);
			match(T__36);
			setState(421); 
			_errHandler.sync(this);
			_alt = 1+1;
			do {
				switch (_alt) {
				case 1+1:
					{
					{
					setState(420);
					match(DIGIT);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(423); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			} while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class YearContext extends ParserRuleContext {
		public List<TerminalNode> DIGIT() { return getTokens(ProgramParser.DIGIT); }
		public TerminalNode DIGIT(int i) {
			return getToken(ProgramParser.DIGIT, i);
		}
		public YearContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_year; }
	}

	public final YearContext year() throws RecognitionException {
		YearContext _localctx = new YearContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_year);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(425);
			match(DIGIT);
			setState(426);
			match(DIGIT);
			setState(427);
			match(DIGIT);
			setState(428);
			match(DIGIT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public TerminalNode INTEGER() { return getToken(ProgramParser.INTEGER, 0); }
		public TerminalNode DECIMAL() { return getToken(ProgramParser.DECIMAL, 0); }
		public TerminalNode DOUBLE() { return getToken(ProgramParser.DOUBLE, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_number);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(430);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTEGER) | (1L << DECIMAL) | (1L << DOUBLE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 9:
			return entitySet_sempred((EntitySetContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean entitySet_sempred(EntitySetContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		case 2:
			return precpred(_ctx, 3);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60\u01b3\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\5\2\u0080\n\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3"+
		"\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\5\7\u0093\n\7\3\7\3\7\3\b\3\b\3\b\3"+
		"\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00a4\n\13\3\13\5\13\u00a7"+
		"\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00b2\n\13\7\13"+
		"\u00b4\n\13\f\13\16\13\u00b7\13\13\3\f\3\f\5\f\u00bb\n\f\3\f\5\f\u00be"+
		"\n\f\3\r\3\r\5\r\u00c2\n\r\3\r\5\r\u00c5\n\r\3\16\3\16\3\17\3\17\3\20"+
		"\3\20\3\21\3\21\3\22\3\22\5\22\u00d1\n\22\3\23\3\23\3\24\3\24\3\25\3\25"+
		"\3\25\3\25\5\25\u00db\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35"+
		"\3\35\3\35\3\35\3\36\3\36\3\36\3\36\5\36\u0117\n\36\3\37\3\37\3\37\3\37"+
		"\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#"+
		"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\5&\u0147"+
		"\n&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)"+
		"\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3.\3.\3/"+
		"\3/\3\60\3\60\3\60\3\60\5\60\u0179\n\60\3\61\3\61\3\62\3\62\3\62\3\62"+
		"\5\62\u0181\n\62\3\63\3\63\3\64\3\64\3\65\3\65\5\65\u0189\n\65\3\66\3"+
		"\66\3\67\3\67\38\38\39\39\39\39\39\39\69\u0197\n9\r9\169\u0198\3:\6:\u019c"+
		"\n:\r:\16:\u019d\3:\3:\6:\u01a2\n:\r:\16:\u01a3\3:\3:\6:\u01a8\n:\r:\16"+
		":\u01a9\3;\3;\3;\3;\3;\3<\3<\3<\5\u019d\u01a3\u01a9\3\24=\2\4\6\b\n\f"+
		"\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^"+
		"`bdfhjlnprtv\2\6\3\2\36!\3\2\"#\3\2$%\3\2*,\2\u019f\2\177\3\2\2\2\4\u0083"+
		"\3\2\2\2\6\u0086\3\2\2\2\b\u0089\3\2\2\2\n\u008c\3\2\2\2\f\u008f\3\2\2"+
		"\2\16\u0096\3\2\2\2\20\u0099\3\2\2\2\22\u009c\3\2\2\2\24\u00a6\3\2\2\2"+
		"\26\u00b8\3\2\2\2\30\u00bf\3\2\2\2\32\u00c6\3\2\2\2\34\u00c8\3\2\2\2\36"+
		"\u00ca\3\2\2\2 \u00cc\3\2\2\2\"\u00d0\3\2\2\2$\u00d2\3\2\2\2&\u00d4\3"+
		"\2\2\2(\u00da\3\2\2\2*\u00dc\3\2\2\2,\u00e2\3\2\2\2.\u00ea\3\2\2\2\60"+
		"\u00f2\3\2\2\2\62\u00fa\3\2\2\2\64\u00fc\3\2\2\2\66\u0106\3\2\2\28\u010e"+
		"\3\2\2\2:\u0116\3\2\2\2<\u0118\3\2\2\2>\u011c\3\2\2\2@\u0122\3\2\2\2B"+
		"\u0128\3\2\2\2D\u012e\3\2\2\2F\u0136\3\2\2\2H\u013c\3\2\2\2J\u0146\3\2"+
		"\2\2L\u0148\3\2\2\2N\u014e\3\2\2\2P\u0156\3\2\2\2R\u015e\3\2\2\2T\u0166"+
		"\3\2\2\2V\u016a\3\2\2\2X\u016e\3\2\2\2Z\u0170\3\2\2\2\\\u0172\3\2\2\2"+
		"^\u0178\3\2\2\2`\u017a\3\2\2\2b\u0180\3\2\2\2d\u0182\3\2\2\2f\u0184\3"+
		"\2\2\2h\u0188\3\2\2\2j\u018a\3\2\2\2l\u018c\3\2\2\2n\u018e\3\2\2\2p\u0196"+
		"\3\2\2\2r\u019b\3\2\2\2t\u01ab\3\2\2\2v\u01b0\3\2\2\2x\u0080\5\4\3\2y"+
		"\u0080\5\6\4\2z\u0080\5\b\5\2{\u0080\5\n\6\2|\u0080\5\f\7\2}\u0080\5\16"+
		"\b\2~\u0080\5\20\t\2\177x\3\2\2\2\177y\3\2\2\2\177z\3\2\2\2\177{\3\2\2"+
		"\2\177|\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082"+
		"\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084\5\24\13\2\u0084\u0085\5\34\17\2\u0085"+
		"\5\3\2\2\2\u0086\u0087\5\24\13\2\u0087\u0088\5\36\20\2\u0088\7\3\2\2\2"+
		"\u0089\u008a\5\24\13\2\u008a\u008b\58\35\2\u008b\t\3\2\2\2\u008c\u008d"+
		"\5\22\n\2\u008d\u008e\5\62\32\2\u008e\13\3\2\2\2\u008f\u0092\5\24\13\2"+
		"\u0090\u0093\5\66\34\2\u0091\u0093\58\35\2\u0092\u0090\3\2\2\2\u0092\u0091"+
		"\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\5:\36\2\u0095\r\3\2\2\2\u0096"+
		"\u0097\5\24\13\2\u0097\u0098\5D#\2\u0098\17\3\2\2\2\u0099\u009a\5\22\n"+
		"\2\u009a\u009b\5F$\2\u009b\21\3\2\2\2\u009c\u009d\5\24\13\2\u009d\u009e"+
		"\5\24\13\2\u009e\23\3\2\2\2\u009f\u00a0\b\13\1\2\u00a0\u00a3\5 \21\2\u00a1"+
		"\u00a4\5\30\r\2\u00a2\u00a4\5\32\16\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2"+
		"\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a7\5V,\2\u00a6\u009f\3\2\2\2\u00a6"+
		"\u00a5\3\2\2\2\u00a7\u00b5\3\2\2\2\u00a8\u00a9\f\7\2\2\u00a9\u00aa\5\24"+
		"\13\2\u00aa\u00ab\5\"\22\2\u00ab\u00b4\3\2\2\2\u00ac\u00ad\f\6\2\2\u00ad"+
		"\u00b4\5\64\33\2\u00ae\u00b1\f\5\2\2\u00af\u00b2\5\26\f\2\u00b0\u00b2"+
		"\5\30\r\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b4\3\2\2\2"+
		"\u00b3\u00a8\3\2\2\2\u00b3\u00ac\3\2\2\2\u00b3\u00ae\3\2\2\2\u00b4\u00b7"+
		"\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\25\3\2\2\2\u00b7"+
		"\u00b5\3\2\2\2\u00b8\u00ba\5H%\2\u00b9\u00bb\5J&\2\u00ba\u00b9\3\2\2\2"+
		"\u00ba\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00be\5T+\2\u00bd\u00bc"+
		"\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\27\3\2\2\2\u00bf\u00c1\5(\25\2\u00c0"+
		"\u00c2\5J&\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c4\3\2\2"+
		"\2\u00c3\u00c5\5T+\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\31"+
		"\3\2\2\2\u00c6\u00c7\5T+\2\u00c7\33\3\2\2\2\u00c8\u00c9\7\3\2\2\u00c9"+
		"\35\3\2\2\2\u00ca\u00cb\7\4\2\2\u00cb\37\3\2\2\2\u00cc\u00cd\7\5\2\2\u00cd"+
		"!\3\2\2\2\u00ce\u00d1\5$\23\2\u00cf\u00d1\5&\24\2\u00d0\u00ce\3\2\2\2"+
		"\u00d0\u00cf\3\2\2\2\u00d1#\3\2\2\2\u00d2\u00d3\7\6\2\2\u00d3%\3\2\2\2"+
		"\u00d4\u00d5\7\7\2\2\u00d5\'\3\2\2\2\u00d6\u00db\5*\26\2\u00d7\u00db\5"+
		",\27\2\u00d8\u00db\5.\30\2\u00d9\u00db\5\60\31\2\u00da\u00d6\3\2\2\2\u00da"+
		"\u00d7\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db)\3\2\2\2"+
		"\u00dc\u00dd\7\b\2\2\u00dd\u00de\5\\/\2\u00de\u00df\7\60\2\2\u00df\u00e0"+
		"\5^\60\2\u00e0\u00e1\7\t\2\2\u00e1+\3\2\2\2\u00e2\u00e3\7\n\2\2\u00e3"+
		"\u00e4\5\\/\2\u00e4\u00e5\7\60\2\2\u00e5\u00e6\5^\60\2\u00e6\u00e7\7\60"+
		"\2\2\u00e7\u00e8\5h\65\2\u00e8\u00e9\7\t\2\2\u00e9-\3\2\2\2\u00ea\u00eb"+
		"\7\13\2\2\u00eb\u00ec\5\\/\2\u00ec\u00ed\7\60\2\2\u00ed\u00ee\5^\60\2"+
		"\u00ee\u00ef\7\60\2\2\u00ef\u00f0\5h\65\2\u00f0\u00f1\7\t\2\2\u00f1/\3"+
		"\2\2\2\u00f2\u00f3\7\f\2\2\u00f3\u00f4\5\\/\2\u00f4\u00f5\7\60\2\2\u00f5"+
		"\u00f6\5^\60\2\u00f6\u00f7\7\60\2\2\u00f7\u00f8\5h\65\2\u00f8\u00f9\7"+
		"\t\2\2\u00f9\61\3\2\2\2\u00fa\u00fb\7\r\2\2\u00fb\63\3\2\2\2\u00fc\u00fd"+
		"\7\16\2\2\u00fd\u00fe\5\\/\2\u00fe\u00ff\7\60\2\2\u00ff\u0100\5h\65\2"+
		"\u0100\u0101\7\60\2\2\u0101\u0102\5d\63\2\u0102\u0103\7\60\2\2\u0103\u0104"+
		"\5f\64\2\u0104\u0105\7\t\2\2\u0105\65\3\2\2\2\u0106\u0107\7\17\2\2\u0107"+
		"\u0108\5\\/\2\u0108\u0109\7\60\2\2\u0109\u010a\5`\61\2\u010a\u010b\7\60"+
		"\2\2\u010b\u010c\5b\62\2\u010c\u010d\7\t\2\2\u010d\67\3\2\2\2\u010e\u010f"+
		"\7\20\2\2\u010f\u0110\5\\/\2\u0110\u0111\7\t\2\2\u01119\3\2\2\2\u0112"+
		"\u0117\5<\37\2\u0113\u0117\5> \2\u0114\u0117\5@!\2\u0115\u0117\5B\"\2"+
		"\u0116\u0112\3\2\2\2\u0116\u0113\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115"+
		"\3\2\2\2\u0117;\3\2\2\2\u0118\u0119\7\21\2\2\u0119\u011a\5^\60\2\u011a"+
		"\u011b\7\t\2\2\u011b=\3\2\2\2\u011c\u011d\7\22\2\2\u011d\u011e\5^\60\2"+
		"\u011e\u011f\7\60\2\2\u011f\u0120\5h\65\2\u0120\u0121\7\t\2\2\u0121?\3"+
		"\2\2\2\u0122\u0123\7\23\2\2\u0123\u0124\5^\60\2\u0124\u0125\7\60\2\2\u0125"+
		"\u0126\5h\65\2\u0126\u0127\7\t\2\2\u0127A\3\2\2\2\u0128\u0129\7\24\2\2"+
		"\u0129\u012a\5^\60\2\u012a\u012b\7\60\2\2\u012b\u012c\5h\65\2\u012c\u012d"+
		"\7\t\2\2\u012dC\3\2\2\2\u012e\u012f\7\25\2\2\u012f\u0130\5\\/\2\u0130"+
		"\u0131\7\60\2\2\u0131\u0132\5^\60\2\u0132\u0133\7\60\2\2\u0133\u0134\5"+
		"`\61\2\u0134\u0135\7\t\2\2\u0135E\3\2\2\2\u0136\u0137\7\26\2\2\u0137\u0138"+
		"\5Z.\2\u0138\u0139\7\60\2\2\u0139\u013a\5`\61\2\u013a\u013b\7\t\2\2\u013b"+
		"G\3\2\2\2\u013c\u013d\7\27\2\2\u013d\u013e\5Z.\2\u013e\u013f\7\60\2\2"+
		"\u013f\u0140\5n8\2\u0140\u0141\7\t\2\2\u0141I\3\2\2\2\u0142\u0147\5L\'"+
		"\2\u0143\u0147\5N(\2\u0144\u0147\5P)\2\u0145\u0147\5R*\2\u0146\u0142\3"+
		"\2\2\2\u0146\u0143\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147"+
		"K\3\2\2\2\u0148\u0149\7\30\2\2\u0149\u014a\5`\61\2\u014a\u014b\7\60\2"+
		"\2\u014b\u014c\5b\62\2\u014c\u014d\7\t\2\2\u014dM\3\2\2\2\u014e\u014f"+
		"\7\31\2\2\u014f\u0150\5`\61\2\u0150\u0151\7\60\2\2\u0151\u0152\5b\62\2"+
		"\u0152\u0153\7\60\2\2\u0153\u0154\5h\65\2\u0154\u0155\7\t\2\2\u0155O\3"+
		"\2\2\2\u0156\u0157\7\32\2\2\u0157\u0158\5`\61\2\u0158\u0159\7\60\2\2\u0159"+
		"\u015a\5b\62\2\u015a\u015b\7\60\2\2\u015b\u015c\5h\65\2\u015c\u015d\7"+
		"\t\2\2\u015dQ\3\2\2\2\u015e\u015f\7\33\2\2\u015f\u0160\5`\61\2\u0160\u0161"+
		"\7\60\2\2\u0161\u0162\5b\62\2\u0162\u0163\7\60\2\2\u0163\u0164\5h\65\2"+
		"\u0164\u0165\7\t\2\2\u0165S\3\2\2\2\u0166\u0167\7\34\2\2\u0167\u0168\5"+
		"X-\2\u0168\u0169\7\t\2\2\u0169U\3\2\2\2\u016a\u016b\7\35\2\2\u016b\u016c"+
		"\5p9\2\u016c\u016d\7\t\2\2\u016dW\3\2\2\2\u016e\u016f\5p9\2\u016fY\3\2"+
		"\2\2\u0170\u0171\5p9\2\u0171[\3\2\2\2\u0172\u0173\5p9\2\u0173]\3\2\2\2"+
		"\u0174\u0179\5r:\2\u0175\u0179\5t;\2\u0176\u0179\5v<\2\u0177\u0179\5p"+
		"9\2\u0178\u0174\3\2\2\2\u0178\u0175\3\2\2\2\u0178\u0176\3\2\2\2\u0178"+
		"\u0177\3\2\2\2\u0179_\3\2\2\2\u017a\u017b\5p9\2\u017ba\3\2\2\2\u017c\u0181"+
		"\5r:\2\u017d\u0181\5t;\2\u017e\u0181\5v<\2\u017f\u0181\5p9\2\u0180\u017c"+
		"\3\2\2\2\u0180\u017d\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181"+
		"c\3\2\2\2\u0182\u0183\5p9\2\u0183e\3\2\2\2\u0184\u0185\5p9\2\u0185g\3"+
		"\2\2\2\u0186\u0189\5j\66\2\u0187\u0189\5l\67\2\u0188\u0186\3\2\2\2\u0188"+
		"\u0187\3\2\2\2\u0189i\3\2\2\2\u018a\u018b\t\2\2\2\u018bk\3\2\2\2\u018c"+
		"\u018d\t\3\2\2\u018dm\3\2\2\2\u018e\u018f\t\4\2\2\u018fo\3\2\2\2\u0190"+
		"\u0197\7)\2\2\u0191\u0192\7&\2\2\u0192\u0193\5p9\2\u0193\u0194\7\t\2\2"+
		"\u0194\u0197\3\2\2\2\u0195\u0197\5n8\2\u0196\u0190\3\2\2\2\u0196\u0191"+
		"\3\2\2\2\u0196\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0196\3\2\2\2\u0198"+
		"\u0199\3\2\2\2\u0199q\3\2\2\2\u019a\u019c\7.\2\2\u019b\u019a\3\2\2\2\u019c"+
		"\u019d\3\2\2\2\u019d\u019e\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u019f\3\2"+
		"\2\2\u019f\u01a1\7\'\2\2\u01a0\u01a2\7.\2\2\u01a1\u01a0\3\2\2\2\u01a2"+
		"\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\3\2"+
		"\2\2\u01a5\u01a7\7\'\2\2\u01a6\u01a8\7.\2\2\u01a7\u01a6\3\2\2\2\u01a8"+
		"\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aas\3\2\2\2"+
		"\u01ab\u01ac\7.\2\2\u01ac\u01ad\7.\2\2\u01ad\u01ae\7.\2\2\u01ae\u01af"+
		"\7.\2\2\u01afu\3\2\2\2\u01b0\u01b1\t\5\2\2\u01b1w\3\2\2\2\31\177\u0092"+
		"\u00a3\u00a6\u00b1\u00b3\u00b5\u00ba\u00bd\u00c1\u00c4\u00d0\u00da\u0116"+
		"\u0146\u0178\u0180\u0188\u0196\u0198\u019d\u01a3\u01a9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}