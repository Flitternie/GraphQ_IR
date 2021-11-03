// Generated from /data1/nlx/KqaPro_Parser/template/Template.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TemplateParser extends Parser {
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
	public static final int
		RULE_query = 0, RULE_whatEntityQuery = 1, RULE_howManyEntityQuery = 2, 
		RULE_whatAttributeQuery = 3, RULE_whatRelationQuery = 4, RULE_selectAmongQuery = 5, 
		RULE_selectBetweenQuery = 6, RULE_attributeSatisfyQuery = 7, RULE_attributeVerify = 8, 
		RULE_attributeVerifyUnderQualifier = 9, RULE_whatAttributeQualifierQuery = 10, 
		RULE_whatRelationQualifierQuery = 11, RULE_entity = 12, RULE_entitySet = 13, 
		RULE_entityFilterByRelation = 14, RULE_relationFilter = 15, RULE_relationFilterUnderQualifier = 16, 
		RULE_qualifierFilter = 17, RULE_entityFilterByAttribute = 18, RULE_attributeFilter = 19, 
		RULE_attributeFilterUnderQualifier = 20, RULE_concept = 21, RULE_attribute = 22, 
		RULE_qualifierKey = 23, RULE_value = 24, RULE_qualifierValue = 25, RULE_predicate = 26, 
		RULE_entity_name = 27, RULE_concept_name = 28, RULE_key_name = 29, RULE_relation_name = 30, 
		RULE_value_name = 31, RULE_prefix = 32, RULE_op = 33, RULE_bool = 34;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "whatEntityQuery", "howManyEntityQuery", "whatAttributeQuery", 
			"whatRelationQuery", "selectAmongQuery", "selectBetweenQuery", "attributeSatisfyQuery", 
			"attributeVerify", "attributeVerifyUnderQualifier", "whatAttributeQualifierQuery", 
			"whatRelationQualifierQuery", "entity", "entitySet", "entityFilterByRelation", 
			"relationFilter", "relationFilterUnderQualifier", "qualifierFilter", 
			"entityFilterByAttribute", "attributeFilter", "attributeFilterUnderQualifier", 
			"concept", "attribute", "qualifierKey", "value", "qualifierValue", "predicate", 
			"entity_name", "concept_name", "key_name", "relation_name", "value_name", 
			"prefix", "op", "bool"
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

	@Override
	public String getGrammarFileName() { return "Template.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TemplateParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class QueryContext extends ParserRuleContext {
		public TerminalNode EOQ() { return getToken(TemplateParser.EOQ, 0); }
		public TerminalNode EOF() { return getToken(TemplateParser.EOF, 0); }
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
		public SelectAmongQueryContext selectAmongQuery() {
			return getRuleContext(SelectAmongQueryContext.class,0);
		}
		public SelectBetweenQueryContext selectBetweenQuery() {
			return getRuleContext(SelectBetweenQueryContext.class,0);
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
			setState(79);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(70);
				whatEntityQuery();
				}
				break;
			case 2:
				{
				setState(71);
				howManyEntityQuery();
				}
				break;
			case 3:
				{
				setState(72);
				whatAttributeQuery();
				}
				break;
			case 4:
				{
				setState(73);
				whatRelationQuery();
				}
				break;
			case 5:
				{
				setState(74);
				selectAmongQuery();
				}
				break;
			case 6:
				{
				setState(75);
				selectBetweenQuery();
				}
				break;
			case 7:
				{
				setState(76);
				attributeSatisfyQuery();
				}
				break;
			case 8:
				{
				setState(77);
				whatAttributeQualifierQuery();
				}
				break;
			case 9:
				{
				setState(78);
				whatRelationQualifierQuery();
				}
				break;
			}
			setState(81);
			match(EOQ);
			setState(82);
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
		public TerminalNode BOQ() { return getToken(TemplateParser.BOQ, 0); }
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
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
			setState(84);
			match(BOQ);
			setState(85);
			match(T__0);
			setState(86);
			entity();
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
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
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
			setState(88);
			match(T__1);
			setState(89);
			entity();
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
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
		}
		public PrefixContext prefix() {
			return getRuleContext(PrefixContext.class,0);
		}
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
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
			setState(91);
			match(T__2);
			setState(92);
			entity();
			setState(93);
			match(T__3);
			setState(94);
			match(T__4);
			setState(95);
			prefix();
			setState(96);
			attribute();
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
		public List<EntityContext> entity() {
			return getRuleContexts(EntityContext.class);
		}
		public EntityContext entity(int i) {
			return getRuleContext(EntityContext.class,i);
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
			setState(98);
			match(T__5);
			setState(99);
			entity();
			setState(100);
			match(T__6);
			setState(101);
			entity();
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

	public static class SelectAmongQueryContext extends ParserRuleContext {
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public SelectAmongQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectAmongQuery; }
	}

	public final SelectAmongQueryContext selectAmongQuery() throws RecognitionException {
		SelectAmongQueryContext _localctx = new SelectAmongQueryContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_selectAmongQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			match(T__7);
			setState(104);
			entity();
			setState(105);
			match(T__3);
			setState(106);
			match(T__8);
			setState(107);
			op();
			setState(108);
			attribute();
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

	public static class SelectBetweenQueryContext extends ParserRuleContext {
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public List<EntityContext> entity() {
			return getRuleContexts(EntityContext.class);
		}
		public EntityContext entity(int i) {
			return getRuleContext(EntityContext.class,i);
		}
		public SelectBetweenQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selectBetweenQuery; }
	}

	public final SelectBetweenQueryContext selectBetweenQuery() throws RecognitionException {
		SelectBetweenQueryContext _localctx = new SelectBetweenQueryContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_selectBetweenQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(110);
			match(T__9);
			setState(111);
			op();
			setState(112);
			attribute();
			setState(113);
			match(T__3);
			setState(114);
			entity();
			setState(115);
			match(T__10);
			setState(116);
			entity();
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
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
		}
		public AttributeVerifyUnderQualifierContext attributeVerifyUnderQualifier() {
			return getRuleContext(AttributeVerifyUnderQualifierContext.class,0);
		}
		public AttributeVerifyContext attributeVerify() {
			return getRuleContext(AttributeVerifyContext.class,0);
		}
		public AttributeSatisfyQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeSatisfyQuery; }
	}

	public final AttributeSatisfyQueryContext attributeSatisfyQuery() throws RecognitionException {
		AttributeSatisfyQueryContext _localctx = new AttributeSatisfyQueryContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_attributeSatisfyQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(T__2);
			setState(119);
			entity();
			setState(120);
			match(T__3);
			setState(121);
			match(T__0);
			setState(124);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(122);
				attributeVerifyUnderQualifier();
				}
				break;
			case 2:
				{
				setState(123);
				attributeVerify();
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

	public static class AttributeVerifyContext extends ParserRuleContext {
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public AttributeVerifyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeVerify; }
	}

	public final AttributeVerifyContext attributeVerify() throws RecognitionException {
		AttributeVerifyContext _localctx = new AttributeVerifyContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_attributeVerify);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			attribute();
			setState(127);
			op();
			setState(128);
			value();
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

	public static class AttributeVerifyUnderQualifierContext extends ParserRuleContext {
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public QualifierKeyContext qualifierKey() {
			return getRuleContext(QualifierKeyContext.class,0);
		}
		public QualifierValueContext qualifierValue() {
			return getRuleContext(QualifierValueContext.class,0);
		}
		public AttributeVerifyUnderQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeVerifyUnderQualifier; }
	}

	public final AttributeVerifyUnderQualifierContext attributeVerifyUnderQualifier() throws RecognitionException {
		AttributeVerifyUnderQualifierContext _localctx = new AttributeVerifyUnderQualifierContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_attributeVerifyUnderQualifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			attribute();
			setState(131);
			op();
			setState(132);
			value();
			setState(133);
			match(T__11);
			setState(134);
			qualifierKey();
			setState(135);
			match(T__0);
			setState(136);
			qualifierValue();
			setState(137);
			match(T__12);
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
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
		}
		public PrefixContext prefix() {
			return getRuleContext(PrefixContext.class,0);
		}
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode BOQ() { return getToken(TemplateParser.BOQ, 0); }
		public QualifierKeyContext qualifierKey() {
			return getRuleContext(QualifierKeyContext.class,0);
		}
		public WhatAttributeQualifierQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whatAttributeQualifierQuery; }
	}

	public final WhatAttributeQualifierQueryContext whatAttributeQualifierQuery() throws RecognitionException {
		WhatAttributeQualifierQueryContext _localctx = new WhatAttributeQualifierQueryContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_whatAttributeQualifierQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			match(T__2);
			setState(140);
			entity();
			setState(141);
			match(T__3);
			setState(142);
			prefix();
			setState(143);
			attribute();
			setState(144);
			match(T__0);
			setState(145);
			value();
			setState(146);
			match(T__3);
			setState(147);
			match(BOQ);
			setState(148);
			match(T__13);
			setState(149);
			qualifierKey();
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
		public List<EntityContext> entity() {
			return getRuleContexts(EntityContext.class);
		}
		public EntityContext entity(int i) {
			return getRuleContext(EntityContext.class,i);
		}
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public TerminalNode BOQ() { return getToken(TemplateParser.BOQ, 0); }
		public QualifierKeyContext qualifierKey() {
			return getRuleContext(QualifierKeyContext.class,0);
		}
		public WhatRelationQualifierQueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whatRelationQualifierQuery; }
	}

	public final WhatRelationQualifierQueryContext whatRelationQualifierQuery() throws RecognitionException {
		WhatRelationQualifierQueryContext _localctx = new WhatRelationQualifierQueryContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_whatRelationQualifierQuery);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			entity();
			setState(152);
			predicate();
			setState(153);
			entity();
			setState(154);
			match(T__3);
			setState(155);
			match(BOQ);
			setState(156);
			match(T__13);
			setState(157);
			qualifierKey();
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
		public EntitySetContext entitySet() {
			return getRuleContext(EntitySetContext.class,0);
		}
		public EntityFilterByRelationContext entityFilterByRelation() {
			return getRuleContext(EntityFilterByRelationContext.class,0);
		}
		public EntityFilterByAttributeContext entityFilterByAttribute() {
			return getRuleContext(EntityFilterByAttributeContext.class,0);
		}
		public Entity_nameContext entity_name() {
			return getRuleContext(Entity_nameContext.class,0);
		}
		public EntityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity; }
	}

	public final EntityContext entity() throws RecognitionException {
		EntityContext _localctx = new EntityContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_entity);
		try {
			setState(163);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(159);
				entitySet();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(160);
				entityFilterByRelation();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(161);
				entityFilterByAttribute();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(162);
				entity_name();
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

	public static class EntitySetContext extends ParserRuleContext {
		public BoolContext bool() {
			return getRuleContext(BoolContext.class,0);
		}
		public List<EntityFilterByRelationContext> entityFilterByRelation() {
			return getRuleContexts(EntityFilterByRelationContext.class);
		}
		public EntityFilterByRelationContext entityFilterByRelation(int i) {
			return getRuleContext(EntityFilterByRelationContext.class,i);
		}
		public List<EntityFilterByAttributeContext> entityFilterByAttribute() {
			return getRuleContexts(EntityFilterByAttributeContext.class);
		}
		public EntityFilterByAttributeContext entityFilterByAttribute(int i) {
			return getRuleContext(EntityFilterByAttributeContext.class,i);
		}
		public List<Entity_nameContext> entity_name() {
			return getRuleContexts(Entity_nameContext.class);
		}
		public Entity_nameContext entity_name(int i) {
			return getRuleContext(Entity_nameContext.class,i);
		}
		public EntitySetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entitySet; }
	}

	public final EntitySetContext entitySet() throws RecognitionException {
		EntitySetContext _localctx = new EntitySetContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_entitySet);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(165);
				entityFilterByRelation();
				}
				break;
			case 2:
				{
				setState(166);
				entityFilterByAttribute();
				}
				break;
			case 3:
				{
				setState(167);
				entity_name();
				}
				break;
			}
			setState(170);
			bool();
			setState(174);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(171);
				entityFilterByRelation();
				}
				break;
			case 2:
				{
				setState(172);
				entityFilterByAttribute();
				}
				break;
			case 3:
				{
				setState(173);
				entity_name();
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

	public static class EntityFilterByRelationContext extends ParserRuleContext {
		public ConceptContext concept() {
			return getRuleContext(ConceptContext.class,0);
		}
		public RelationFilterUnderQualifierContext relationFilterUnderQualifier() {
			return getRuleContext(RelationFilterUnderQualifierContext.class,0);
		}
		public RelationFilterContext relationFilter() {
			return getRuleContext(RelationFilterContext.class,0);
		}
		public EntityFilterByRelationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityFilterByRelation; }
	}

	public final EntityFilterByRelationContext entityFilterByRelation() throws RecognitionException {
		EntityFilterByRelationContext _localctx = new EntityFilterByRelationContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_entityFilterByRelation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(T__14);
			setState(179);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING:
				{
				setState(177);
				concept();
				}
				break;
			case T__15:
				{
				setState(178);
				match(T__15);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(181);
			match(T__16);
			setState(184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(182);
				relationFilterUnderQualifier();
				}
				break;
			case 2:
				{
				setState(183);
				relationFilter();
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

	public static class RelationFilterContext extends ParserRuleContext {
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
		}
		public RelationFilterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationFilter; }
	}

	public final RelationFilterContext relationFilter() throws RecognitionException {
		RelationFilterContext _localctx = new RelationFilterContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_relationFilter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(186);
			predicate();
			setState(187);
			entity();
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

	public static class RelationFilterUnderQualifierContext extends ParserRuleContext {
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public EntityContext entity() {
			return getRuleContext(EntityContext.class,0);
		}
		public QualifierFilterContext qualifierFilter() {
			return getRuleContext(QualifierFilterContext.class,0);
		}
		public RelationFilterUnderQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationFilterUnderQualifier; }
	}

	public final RelationFilterUnderQualifierContext relationFilterUnderQualifier() throws RecognitionException {
		RelationFilterUnderQualifierContext _localctx = new RelationFilterUnderQualifierContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_relationFilterUnderQualifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			predicate();
			setState(190);
			entity();
			setState(191);
			qualifierFilter();
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

	public static class QualifierFilterContext extends ParserRuleContext {
		public QualifierKeyContext qualifierKey() {
			return getRuleContext(QualifierKeyContext.class,0);
		}
		public QualifierValueContext qualifierValue() {
			return getRuleContext(QualifierValueContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public QualifierFilterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifierFilter; }
	}

	public final QualifierFilterContext qualifierFilter() throws RecognitionException {
		QualifierFilterContext _localctx = new QualifierFilterContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_qualifierFilter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			match(T__11);
			setState(194);
			qualifierKey();
			setState(195);
			match(T__0);
			setState(197);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << COMPARATIVE) | (1L << SUPERLATIVE) | (1L << OPERATOR))) != 0)) {
				{
				setState(196);
				op();
				}
			}

			setState(199);
			qualifierValue();
			setState(200);
			match(T__12);
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
		public ConceptContext concept() {
			return getRuleContext(ConceptContext.class,0);
		}
		public AttributeFilterUnderQualifierContext attributeFilterUnderQualifier() {
			return getRuleContext(AttributeFilterUnderQualifierContext.class,0);
		}
		public AttributeFilterContext attributeFilter() {
			return getRuleContext(AttributeFilterContext.class,0);
		}
		public EntityFilterByAttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityFilterByAttribute; }
	}

	public final EntityFilterByAttributeContext entityFilterByAttribute() throws RecognitionException {
		EntityFilterByAttributeContext _localctx = new EntityFilterByAttributeContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_entityFilterByAttribute);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(T__14);
			setState(205);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRING:
				{
				setState(203);
				concept();
				}
				break;
			case T__15:
				{
				setState(204);
				match(T__15);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(207);
			match(T__17);
			setState(210);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(208);
				attributeFilterUnderQualifier();
				}
				break;
			case 2:
				{
				setState(209);
				attributeFilter();
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

	public static class AttributeFilterContext extends ParserRuleContext {
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public AttributeFilterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeFilter; }
	}

	public final AttributeFilterContext attributeFilter() throws RecognitionException {
		AttributeFilterContext _localctx = new AttributeFilterContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_attributeFilter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			attribute();
			setState(213);
			match(T__0);
			setState(215);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << COMPARATIVE) | (1L << SUPERLATIVE) | (1L << OPERATOR))) != 0)) {
				{
				setState(214);
				op();
				}
			}

			setState(217);
			value();
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

	public static class AttributeFilterUnderQualifierContext extends ParserRuleContext {
		public AttributeContext attribute() {
			return getRuleContext(AttributeContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public QualifierFilterContext qualifierFilter() {
			return getRuleContext(QualifierFilterContext.class,0);
		}
		public OpContext op() {
			return getRuleContext(OpContext.class,0);
		}
		public AttributeFilterUnderQualifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attributeFilterUnderQualifier; }
	}

	public final AttributeFilterUnderQualifierContext attributeFilterUnderQualifier() throws RecognitionException {
		AttributeFilterUnderQualifierContext _localctx = new AttributeFilterUnderQualifierContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_attributeFilterUnderQualifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			attribute();
			setState(220);
			match(T__0);
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << COMPARATIVE) | (1L << SUPERLATIVE) | (1L << OPERATOR))) != 0)) {
				{
				setState(221);
				op();
				}
			}

			setState(224);
			value();
			setState(225);
			qualifierFilter();
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
		public Concept_nameContext concept_name() {
			return getRuleContext(Concept_nameContext.class,0);
		}
		public ConceptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concept; }
	}

	public final ConceptContext concept() throws RecognitionException {
		ConceptContext _localctx = new ConceptContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_concept);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			concept_name();
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

	public static class AttributeContext extends ParserRuleContext {
		public Key_nameContext key_name() {
			return getRuleContext(Key_nameContext.class,0);
		}
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_attribute);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			key_name();
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

	public static class QualifierKeyContext extends ParserRuleContext {
		public Key_nameContext key_name() {
			return getRuleContext(Key_nameContext.class,0);
		}
		public QualifierKeyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifierKey; }
	}

	public final QualifierKeyContext qualifierKey() throws RecognitionException {
		QualifierKeyContext _localctx = new QualifierKeyContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_qualifierKey);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			key_name();
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
		public Value_nameContext value_name() {
			return getRuleContext(Value_nameContext.class,0);
		}
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_value);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			value_name();
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

	public static class QualifierValueContext extends ParserRuleContext {
		public Value_nameContext value_name() {
			return getRuleContext(Value_nameContext.class,0);
		}
		public QualifierValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_qualifierValue; }
	}

	public final QualifierValueContext qualifierValue() throws RecognitionException {
		QualifierValueContext _localctx = new QualifierValueContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_qualifierValue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(235);
			value_name();
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
		public Relation_nameContext relation_name() {
			return getRuleContext(Relation_nameContext.class,0);
		}
		public PredicateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicate; }
	}

	public final PredicateContext predicate() throws RecognitionException {
		PredicateContext _localctx = new PredicateContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_predicate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			relation_name();
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

	public static class Entity_nameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(TemplateParser.STRING, 0); }
		public Entity_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entity_name; }
	}

	public final Entity_nameContext entity_name() throws RecognitionException {
		Entity_nameContext _localctx = new Entity_nameContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_entity_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			match(STRING);
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

	public static class Concept_nameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(TemplateParser.STRING, 0); }
		public Concept_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_concept_name; }
	}

	public final Concept_nameContext concept_name() throws RecognitionException {
		Concept_nameContext _localctx = new Concept_nameContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_concept_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(241);
			match(STRING);
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

	public static class Key_nameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(TemplateParser.STRING, 0); }
		public Key_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_key_name; }
	}

	public final Key_nameContext key_name() throws RecognitionException {
		Key_nameContext _localctx = new Key_nameContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_key_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(243);
			match(STRING);
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

	public static class Relation_nameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(TemplateParser.STRING, 0); }
		public Relation_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relation_name; }
	}

	public final Relation_nameContext relation_name() throws RecognitionException {
		Relation_nameContext _localctx = new Relation_nameContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_relation_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			match(STRING);
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

	public static class Value_nameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(TemplateParser.STRING, 0); }
		public TerminalNode DECIMAL() { return getToken(TemplateParser.DECIMAL, 0); }
		public TerminalNode INTEGER() { return getToken(TemplateParser.INTEGER, 0); }
		public Value_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value_name; }
	}

	public final Value_nameContext value_name() throws RecognitionException {
		Value_nameContext _localctx = new Value_nameContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_value_name);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << STRING) | (1L << INTEGER) | (1L << DECIMAL))) != 0)) ) {
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

	public static class PrefixContext extends ParserRuleContext {
		public PrefixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prefix; }
	}

	public final PrefixContext prefix() throws RecognitionException {
		PrefixContext _localctx = new PrefixContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_prefix);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			_la = _input.LA(1);
			if ( !(_la==T__18 || _la==T__19) ) {
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

	public static class OpContext extends ParserRuleContext {
		public TerminalNode COMPARATIVE() { return getToken(TemplateParser.COMPARATIVE, 0); }
		public TerminalNode SUPERLATIVE() { return getToken(TemplateParser.SUPERLATIVE, 0); }
		public TerminalNode OPERATOR() { return getToken(TemplateParser.OPERATOR, 0); }
		public OpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_op; }
	}

	public final OpContext op() throws RecognitionException {
		OpContext _localctx = new OpContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(251);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << COMPARATIVE) | (1L << SUPERLATIVE) | (1L << OPERATOR))) != 0)) ) {
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

	public static class BoolContext extends ParserRuleContext {
		public BoolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bool; }
	}

	public final BoolContext bool() throws RecognitionException {
		BoolContext _localctx = new BoolContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_bool);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			_la = _input.LA(1);
			if ( !(_la==T__10 || _la==T__20) ) {
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3-\u0102\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2R\n\2\3"+
		"\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6"+
		"\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\177\n\t\3\n\3\n\3\n\3\n\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16"+
		"\u00a6\n\16\3\17\3\17\3\17\5\17\u00ab\n\17\3\17\3\17\3\17\3\17\5\17\u00b1"+
		"\n\17\3\20\3\20\3\20\5\20\u00b6\n\20\3\20\3\20\3\20\5\20\u00bb\n\20\3"+
		"\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00c8\n\23"+
		"\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00d0\n\24\3\24\3\24\3\24\5\24\u00d5"+
		"\n\24\3\25\3\25\3\25\5\25\u00da\n\25\3\25\3\25\3\26\3\26\3\26\5\26\u00e1"+
		"\n\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33"+
		"\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$"+
		"\3$\3$\2\2%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66"+
		"8:<>@BDF\2\6\4\2\37\37!\"\3\2\25\26\3\2\30\32\4\2\r\r\27\27\2\u00f5\2"+
		"Q\3\2\2\2\4V\3\2\2\2\6Z\3\2\2\2\b]\3\2\2\2\nd\3\2\2\2\fi\3\2\2\2\16p\3"+
		"\2\2\2\20x\3\2\2\2\22\u0080\3\2\2\2\24\u0084\3\2\2\2\26\u008d\3\2\2\2"+
		"\30\u0099\3\2\2\2\32\u00a5\3\2\2\2\34\u00aa\3\2\2\2\36\u00b2\3\2\2\2 "+
		"\u00bc\3\2\2\2\"\u00bf\3\2\2\2$\u00c3\3\2\2\2&\u00cc\3\2\2\2(\u00d6\3"+
		"\2\2\2*\u00dd\3\2\2\2,\u00e5\3\2\2\2.\u00e7\3\2\2\2\60\u00e9\3\2\2\2\62"+
		"\u00eb\3\2\2\2\64\u00ed\3\2\2\2\66\u00ef\3\2\2\28\u00f1\3\2\2\2:\u00f3"+
		"\3\2\2\2<\u00f5\3\2\2\2>\u00f7\3\2\2\2@\u00f9\3\2\2\2B\u00fb\3\2\2\2D"+
		"\u00fd\3\2\2\2F\u00ff\3\2\2\2HR\5\4\3\2IR\5\6\4\2JR\5\b\5\2KR\5\n\6\2"+
		"LR\5\f\7\2MR\5\16\b\2NR\5\20\t\2OR\5\26\f\2PR\5\30\r\2QH\3\2\2\2QI\3\2"+
		"\2\2QJ\3\2\2\2QK\3\2\2\2QL\3\2\2\2QM\3\2\2\2QN\3\2\2\2QO\3\2\2\2QP\3\2"+
		"\2\2RS\3\2\2\2ST\7,\2\2TU\7\2\2\3U\3\3\2\2\2VW\7+\2\2WX\7\3\2\2XY\5\32"+
		"\16\2Y\5\3\2\2\2Z[\7\4\2\2[\\\5\32\16\2\\\7\3\2\2\2]^\7\5\2\2^_\5\32\16"+
		"\2_`\7\6\2\2`a\7\7\2\2ab\5B\"\2bc\5.\30\2c\t\3\2\2\2de\7\b\2\2ef\5\32"+
		"\16\2fg\7\t\2\2gh\5\32\16\2h\13\3\2\2\2ij\7\n\2\2jk\5\32\16\2kl\7\6\2"+
		"\2lm\7\13\2\2mn\5D#\2no\5.\30\2o\r\3\2\2\2pq\7\f\2\2qr\5D#\2rs\5.\30\2"+
		"st\7\6\2\2tu\5\32\16\2uv\7\r\2\2vw\5\32\16\2w\17\3\2\2\2xy\7\5\2\2yz\5"+
		"\32\16\2z{\7\6\2\2{~\7\3\2\2|\177\5\24\13\2}\177\5\22\n\2~|\3\2\2\2~}"+
		"\3\2\2\2\177\21\3\2\2\2\u0080\u0081\5.\30\2\u0081\u0082\5D#\2\u0082\u0083"+
		"\5\62\32\2\u0083\23\3\2\2\2\u0084\u0085\5.\30\2\u0085\u0086\5D#\2\u0086"+
		"\u0087\5\62\32\2\u0087\u0088\7\16\2\2\u0088\u0089\5\60\31\2\u0089\u008a"+
		"\7\3\2\2\u008a\u008b\5\64\33\2\u008b\u008c\7\17\2\2\u008c\25\3\2\2\2\u008d"+
		"\u008e\7\5\2\2\u008e\u008f\5\32\16\2\u008f\u0090\7\6\2\2\u0090\u0091\5"+
		"B\"\2\u0091\u0092\5.\30\2\u0092\u0093\7\3\2\2\u0093\u0094\5\62\32\2\u0094"+
		"\u0095\7\6\2\2\u0095\u0096\7+\2\2\u0096\u0097\7\20\2\2\u0097\u0098\5\60"+
		"\31\2\u0098\27\3\2\2\2\u0099\u009a\5\32\16\2\u009a\u009b\5\66\34\2\u009b"+
		"\u009c\5\32\16\2\u009c\u009d\7\6\2\2\u009d\u009e\7+\2\2\u009e\u009f\7"+
		"\20\2\2\u009f\u00a0\5\60\31\2\u00a0\31\3\2\2\2\u00a1\u00a6\5\34\17\2\u00a2"+
		"\u00a6\5\36\20\2\u00a3\u00a6\5&\24\2\u00a4\u00a6\58\35\2\u00a5\u00a1\3"+
		"\2\2\2\u00a5\u00a2\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6"+
		"\33\3\2\2\2\u00a7\u00ab\5\36\20\2\u00a8\u00ab\5&\24\2\u00a9\u00ab\58\35"+
		"\2\u00aa\u00a7\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac"+
		"\3\2\2\2\u00ac\u00b0\5F$\2\u00ad\u00b1\5\36\20\2\u00ae\u00b1\5&\24\2\u00af"+
		"\u00b1\58\35\2\u00b0\u00ad\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2"+
		"\2\2\u00b1\35\3\2\2\2\u00b2\u00b5\7\21\2\2\u00b3\u00b6\5,\27\2\u00b4\u00b6"+
		"\7\22\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2"+
		"\u00b7\u00ba\7\23\2\2\u00b8\u00bb\5\"\22\2\u00b9\u00bb\5 \21\2\u00ba\u00b8"+
		"\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\37\3\2\2\2\u00bc\u00bd\5\66\34\2\u00bd"+
		"\u00be\5\32\16\2\u00be!\3\2\2\2\u00bf\u00c0\5\66\34\2\u00c0\u00c1\5\32"+
		"\16\2\u00c1\u00c2\5$\23\2\u00c2#\3\2\2\2\u00c3\u00c4\7\16\2\2\u00c4\u00c5"+
		"\5\60\31\2\u00c5\u00c7\7\3\2\2\u00c6\u00c8\5D#\2\u00c7\u00c6\3\2\2\2\u00c7"+
		"\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\5\64\33\2\u00ca\u00cb\7"+
		"\17\2\2\u00cb%\3\2\2\2\u00cc\u00cf\7\21\2\2\u00cd\u00d0\5,\27\2\u00ce"+
		"\u00d0\7\22\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\u00d1\3"+
		"\2\2\2\u00d1\u00d4\7\24\2\2\u00d2\u00d5\5*\26\2\u00d3\u00d5\5(\25\2\u00d4"+
		"\u00d2\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\'\3\2\2\2\u00d6\u00d7\5.\30\2"+
		"\u00d7\u00d9\7\3\2\2\u00d8\u00da\5D#\2\u00d9\u00d8\3\2\2\2\u00d9\u00da"+
		"\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\5\62\32\2\u00dc)\3\2\2\2\u00dd"+
		"\u00de\5.\30\2\u00de\u00e0\7\3\2\2\u00df\u00e1\5D#\2\u00e0\u00df\3\2\2"+
		"\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\5\62\32\2\u00e3"+
		"\u00e4\5$\23\2\u00e4+\3\2\2\2\u00e5\u00e6\5:\36\2\u00e6-\3\2\2\2\u00e7"+
		"\u00e8\5<\37\2\u00e8/\3\2\2\2\u00e9\u00ea\5<\37\2\u00ea\61\3\2\2\2\u00eb"+
		"\u00ec\5@!\2\u00ec\63\3\2\2\2\u00ed\u00ee\5@!\2\u00ee\65\3\2\2\2\u00ef"+
		"\u00f0\5> \2\u00f0\67\3\2\2\2\u00f1\u00f2\7\37\2\2\u00f29\3\2\2\2\u00f3"+
		"\u00f4\7\37\2\2\u00f4;\3\2\2\2\u00f5\u00f6\7\37\2\2\u00f6=\3\2\2\2\u00f7"+
		"\u00f8\7\37\2\2\u00f8?\3\2\2\2\u00f9\u00fa\t\2\2\2\u00faA\3\2\2\2\u00fb"+
		"\u00fc\t\3\2\2\u00fcC\3\2\2\2\u00fd\u00fe\t\4\2\2\u00feE\3\2\2\2\u00ff"+
		"\u0100\t\5\2\2\u0100G\3\2\2\2\16Q~\u00a5\u00aa\u00b0\u00b5\u00ba\u00c7"+
		"\u00cf\u00d4\u00d9\u00e0";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}