import os
import re
from antlr4 import *

from .SparqlLexer import SparqlLexer
from .SparqlParser import SparqlParser
from .SparqlListener import SparqlListener


from ..utils import *
from ..ir.utils import *


class IREmitter(SparqlListener):

    def __init__(self):
        self.ir = ""

        self.query_var = ""
        self.queryType = ""

    def get_ir(self, ctx):
        return self.ir

    # Enter a parse tree produced by SparqlParser#query.
    def enterQuery(self, ctx: SparqlParser.QueryContext):
        self.ir = ""
        ctx.slots = strictDict({"entitySet": "", "relationEntitySet1": "", "relationEntitySet2": "", "attribute": ""})
        return super().enterQuery(ctx)

    # Exit a parse tree produced by SparqlParser#query.
    def exitQuery(self, ctx: SparqlParser.QueryContext):
        if self.queryType == "EntityQuery":
            self.ir = "what is {}".format(ctx.slots["entitySet"])
        return super().exitQuery(ctx)

        # Enter a parse tree produced by SparqlParser#prologue.
    def enterPrologue(self, ctx: SparqlParser.PrologueContext):
        pass

    # Exit a parse tree produced by SparqlParser#prologue.
    def exitPrologue(self, ctx: SparqlParser.PrologueContext):
        pass

    # Enter a parse tree produced by SparqlParser#baseDecl.
    def enterBaseDecl(self, ctx: SparqlParser.BaseDeclContext):
        pass

    # Exit a parse tree produced by SparqlParser#baseDecl.
    def exitBaseDecl(self, ctx: SparqlParser.BaseDeclContext):
        pass

    # Enter a parse tree produced by SparqlParser#prefixDecl.
    def enterPrefixDecl(self, ctx: SparqlParser.PrefixDeclContext):
        pass

    # Exit a parse tree produced by SparqlParser#prefixDecl.
    def exitPrefixDecl(self, ctx: SparqlParser.PrefixDeclContext):
        pass

    # Enter a parse tree produced by SparqlParser#selectQuery.
    def enterSelectQuery(self, ctx: SparqlParser.SelectQueryContext):
        ctx.slots = strictDict({"entitySet": "", "relationEntitySet1": "", "relationEntitySet2": "", "attribute": ""})
        return super().enterSelectQuery(ctx)

    # Exit a parse tree produced by SparqlParser#selectQuery.
    def exitSelectQuery(self, ctx: SparqlParser.SelectQueryContext):
        ctx.parentCtx.slots['entitySet'] = ctx.slots['entitySet']
        ctx.parentCtx.slots['relationEntitySet1'] = ctx.slots['relationEntitySet1']
        ctx.parentCtx.slots['relationEntitySet2'] = ctx.slots['relationEntitySet2']
        ctx.parentCtx.slots['attribute'] = ctx.slots['attribute']
        return super().exitSelectQuery(ctx)

    # Enter a parse tree produced by SparqlParser#entityQueryCondition.
    def enterEntityQueryCondition(self, ctx: SparqlParser.EntityQueryConditionContext):
        ctx.slots = strictDict({"var": "", "dtype": ""})
        return super().enterEntityQueryCondition(ctx)

    # Exit a parse tree produced by SparqlParser#entityQueryCondition.
    def exitEntityQueryCondition(self, ctx: SparqlParser.EntityQueryConditionContext):
        if ctx.slots["var"] == "?pv":
            self.queryType = "AttributeQuery"
        self.query_var = ctx.slots["var"]
        return super().exitEntityQueryCondition(ctx)

    # Enter a parse tree produced by SparqlParser#countQueryCondition.
    def enterCountQueryCondition(self, ctx: SparqlParser.CountQueryConditionContext):
        ctx.slots = strictDict({"var": "", "dtype": ""})
        return super().enterCountQueryCondition(ctx)

    # Exit a parse tree produced by SparqlParser#countQueryCondition.
    def exitCountQueryCondition(self, ctx: SparqlParser.CountQueryConditionContext):
        self.queryType = "CountQuery"
        return super().exitCountQueryCondition(ctx)

    # Enter a parse tree produced by SparqlParser#constructQuery.
    def enterConstructQuery(self, ctx: SparqlParser.ConstructQueryContext):
        pass

    # Exit a parse tree produced by SparqlParser#constructQuery.
    def exitConstructQuery(self, ctx: SparqlParser.ConstructQueryContext):
        pass

    # Enter a parse tree produced by SparqlParser#describeQuery.
    def enterDescribeQuery(self, ctx: SparqlParser.DescribeQueryContext):
        pass

    # Exit a parse tree produced by SparqlParser#describeQuery.
    def exitDescribeQuery(self, ctx: SparqlParser.DescribeQueryContext):
        pass

    # Enter a parse tree produced by SparqlParser#askQuery.
    def enterAskQuery(self, ctx: SparqlParser.AskQueryContext):
        pass

    # Exit a parse tree produced by SparqlParser#askQuery.
    def exitAskQuery(self, ctx: SparqlParser.AskQueryContext):
        pass

    # Enter a parse tree produced by SparqlParser#datasetClause.
    def enterDatasetClause(self, ctx: SparqlParser.DatasetClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#datasetClause.
    def exitDatasetClause(self, ctx: SparqlParser.DatasetClauseContext):
        pass

    # Enter a parse tree produced by SparqlParser#defaultGraphClause.
    def enterDefaultGraphClause(self, ctx: SparqlParser.DefaultGraphClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#defaultGraphClause.
    def exitDefaultGraphClause(self, ctx: SparqlParser.DefaultGraphClauseContext):
        pass

    # Enter a parse tree produced by SparqlParser#namedGraphClause.
    def enterNamedGraphClause(self, ctx: SparqlParser.NamedGraphClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#namedGraphClause.
    def exitNamedGraphClause(self, ctx: SparqlParser.NamedGraphClauseContext):
        pass

    # Enter a parse tree produced by SparqlParser#sourceSelector.
    def enterSourceSelector(self, ctx: SparqlParser.SourceSelectorContext):
        pass

    # Exit a parse tree produced by SparqlParser#sourceSelector.
    def exitSourceSelector(self, ctx: SparqlParser.SourceSelectorContext):
        pass

    # Enter a parse tree produced by SparqlParser#whereClause.
    def enterWhereClause(self, ctx: SparqlParser.WhereClauseContext):
        ctx.slots = strictDict({"entitySet": "", "relationEntitySet1": "", "relationEntitySet2": "", "attribute": ""})
        return super().enterWhereClause(ctx)

    # Exit a parse tree produced by SparqlParser#whereClause.
    def exitWhereClause(self, ctx: SparqlParser.WhereClauseContext):
        ctx.parentCtx.slots['entitySet'] = ctx.slots['entitySet']
        ctx.parentCtx.slots['relationEntitySet1'] = ctx.slots['relationEntitySet1']
        ctx.parentCtx.slots['relationEntitySet2'] = ctx.slots['relationEntitySet2']
        ctx.parentCtx.slots['attribute'] = ctx.slots['attribute']
        return super().exitWhereClause(ctx)

    # Enter a parse tree produced by SparqlParser#solutionModifier.
    def enterSolutionModifier(self, ctx: SparqlParser.SolutionModifierContext):
        pass

    # Exit a parse tree produced by SparqlParser#solutionModifier.
    def exitSolutionModifier(self, ctx: SparqlParser.SolutionModifierContext):
        pass

    # Enter a parse tree produced by SparqlParser#limitOffsetClauses.
    def enterLimitOffsetClauses(self, ctx: SparqlParser.LimitOffsetClausesContext):
        pass

    # Exit a parse tree produced by SparqlParser#limitOffsetClauses.
    def exitLimitOffsetClauses(self, ctx: SparqlParser.LimitOffsetClausesContext):
        pass

    # Enter a parse tree produced by SparqlParser#orderClause.
    def enterOrderClause(self, ctx: SparqlParser.OrderClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#orderClause.
    def exitOrderClause(self, ctx: SparqlParser.OrderClauseContext):
        pass

    # Enter a parse tree produced by SparqlParser#orderCondition.
    def enterOrderCondition(self, ctx: SparqlParser.OrderConditionContext):
        pass

    # Exit a parse tree produced by SparqlParser#orderCondition.
    def exitOrderCondition(self, ctx: SparqlParser.OrderConditionContext):
        pass

    # Enter a parse tree produced by SparqlParser#limitClause.
    def enterLimitClause(self, ctx: SparqlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#limitClause.
    def exitLimitClause(self, ctx: SparqlParser.LimitClauseContext):
        pass

    # Enter a parse tree produced by SparqlParser#offsetClause.
    def enterOffsetClause(self, ctx: SparqlParser.OffsetClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#offsetClause.
    def exitOffsetClause(self, ctx: SparqlParser.OffsetClauseContext):
        pass

    # Enter a parse tree produced by SparqlParser#groupGraphPattern.
    def enterGroupGraphPattern(self, ctx: SparqlParser.GroupGraphPatternContext):
        ctx.slots = strictDict({"triple_table": dict()})
        return super().enterGroupGraphPattern(ctx)

    # Exit a parse tree produced by SparqlParser#groupGraphPattern.
    def exitGroupGraphPattern(self, ctx: SparqlParser.GroupGraphPatternContext):
        if isinstance(ctx.parentCtx, SparqlParser.WhereClauseContext):
            if self.queryType == 'CountQuery' or self.queryType == 'EntityQuery':
                print(ctx.slots['triple_table'])

                entity = 'Ones'
                entitySets = []

                for triple in ctx.slots['triple_table'][self.query_var]:
                    if triple[2] == '?c':
                        entity = '<C> {} </C>'.format(get_class_label(ctx.slots['triple_table']))
                    if triple[1] == '<pred:name>':
                        entity = '<E> {} </E>'.format(get_class_label(triple[1]))

                for triple in ctx.slots['triple_table'][self.query_var]:
                    if triple[2].startswith('?pv'):
                        entity_set = '<ES> {} whose <A> {} </A> is text <V> {} </V>'
                        label, value = get_attribute(ctx.slots['triple_table'], triple[2])
                        entity_set = entity_set.format(entity, label, value)
                        entitySets.append(entity_set)

                ES = f"{entitySets.pop()}"
                while len(entitySets) != 0:
                    es = entitySets.pop()
                    ES = "<ES> {} and {} </ES>".format(ES, es)

                ctx.parentCtx.slots['entitySet'] = ES

        return super().exitGroupGraphPattern(ctx)

    # Enter a parse tree produced by SparqlParser#triplesBlock.
    def enterTriplesBlock(self, ctx: SparqlParser.TriplesBlockContext):
        ctx.slots = strictDict({"triple_table": dict()})
        return super().enterTriplesBlock(ctx)

    # Exit a parse tree produced by SparqlParser#triplesBlock.
    def exitTriplesBlock(self, ctx: SparqlParser.TriplesBlockContext):
        ctx.parentCtx.slots['triple_table'] = merge_dict(ctx.slots['triple_table'], ctx.parentCtx.slots['triple_table'])
        return super().exitTriplesBlock(ctx)

    # Enter a parse tree produced by SparqlParser#graphPatternNotTriples.
    def enterGraphPatternNotTriples(self, ctx: SparqlParser.GraphPatternNotTriplesContext):
        pass

    # Exit a parse tree produced by SparqlParser#graphPatternNotTriples.
    def exitGraphPatternNotTriples(self, ctx: SparqlParser.GraphPatternNotTriplesContext):
        pass

    # Enter a parse tree produced by SparqlParser#optionalGraphPattern.
    def enterOptionalGraphPattern(self, ctx: SparqlParser.OptionalGraphPatternContext):
        pass

    # Exit a parse tree produced by SparqlParser#optionalGraphPattern.
    def exitOptionalGraphPattern(self, ctx: SparqlParser.OptionalGraphPatternContext):
        pass

    # Enter a parse tree produced by SparqlParser#graphGraphPattern.
    def enterGraphGraphPattern(self, ctx: SparqlParser.GraphGraphPatternContext):
        pass

    # Exit a parse tree produced by SparqlParser#graphGraphPattern.
    def exitGraphGraphPattern(self, ctx: SparqlParser.GraphGraphPatternContext):
        pass

    # Enter a parse tree produced by SparqlParser#groupOrUnionGraphPattern.
    def enterGroupOrUnionGraphPattern(self, ctx: SparqlParser.GroupOrUnionGraphPatternContext):
        pass

    # Exit a parse tree produced by SparqlParser#groupOrUnionGraphPattern.
    def exitGroupOrUnionGraphPattern(self, ctx: SparqlParser.GroupOrUnionGraphPatternContext):
        pass

    # Enter a parse tree produced by SparqlParser#filter_.
    def enterFilter_(self, ctx: SparqlParser.Filter_Context):
        pass

    # Exit a parse tree produced by SparqlParser#filter_.
    def exitFilter_(self, ctx: SparqlParser.Filter_Context):
        pass

    # Enter a parse tree produced by SparqlParser#constraint.
    def enterConstraint(self, ctx: SparqlParser.ConstraintContext):
        pass

    # Exit a parse tree produced by SparqlParser#constraint.
    def exitConstraint(self, ctx: SparqlParser.ConstraintContext):
        pass

    # Enter a parse tree produced by SparqlParser#functionCall.
    def enterFunctionCall(self, ctx: SparqlParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SparqlParser#functionCall.
    def exitFunctionCall(self, ctx: SparqlParser.FunctionCallContext):
        pass

    # Enter a parse tree produced by SparqlParser#argList.
    def enterArgList(self, ctx: SparqlParser.ArgListContext):
        pass

    # Exit a parse tree produced by SparqlParser#argList.
    def exitArgList(self, ctx: SparqlParser.ArgListContext):
        pass

    # Enter a parse tree produced by SparqlParser#constructTemplate.
    def enterConstructTemplate(self, ctx: SparqlParser.ConstructTemplateContext):
        pass

    # Exit a parse tree produced by SparqlParser#constructTemplate.
    def exitConstructTemplate(self, ctx: SparqlParser.ConstructTemplateContext):
        pass

    # Enter a parse tree produced by SparqlParser#constructTriples.
    def enterConstructTriples(self, ctx: SparqlParser.ConstructTriplesContext):
        pass

    # Exit a parse tree produced by SparqlParser#constructTriples.
    def exitConstructTriples(self, ctx: SparqlParser.ConstructTriplesContext):
        pass

    # Enter a parse tree produced by SparqlParser#triplesSameSubject.
    def enterTriplesSameSubject(self, ctx: SparqlParser.TriplesSameSubjectContext):
        ctx.slots = strictDict({"head": "", "relation": "", "tail": "", "dtype": ""})
        return super().enterTriplesSameSubject(ctx)

    # Exit a parse tree produced by SparqlParser#triplesSameSubject.
    def exitTriplesSameSubject(self, ctx: SparqlParser.TriplesSameSubjectContext):
        if ctx.slots["head"] == self.query_var and not self.queryType:
            self.queryType = "EntityQuery"
        elif ctx.slots["relation"] == self.query_var and not self.queryType:
            self.queryType = "RelationQuery"
        elif ctx.slots["tail"] == self.query_var and not self.queryType:
            self.queryType = "EntityQuery"

        if ctx.slots['head'] not in ctx.parentCtx.slots['triple_table'].keys():
            ctx.parentCtx.slots['triple_table'][ctx.slots['head']] = []
        if ctx.slots['dtype'] == 'var' and ctx.slots['tail'] not in ctx.parentCtx.slots['triple_table'].keys():
            ctx.parentCtx.slots['triple_table'][ctx.slots['tail']] = []

        ctx.parentCtx.slots['triple_table'][ctx.slots['head']].append(
            (ctx.slots['head'], ctx.slots['relation'], ctx.slots['tail']))

        if ctx.slots['dtype'] == 'var':
            ctx.parentCtx.slots['triple_table'][ctx.slots['tail']].append(
                (ctx.slots['head'], ctx.slots['relation'], ctx.slots['tail']))
        return super().exitTriplesSameSubject(ctx)

    # Enter a parse tree produced by SparqlParser#propertyListNotEmpty.
    def enterPropertyListNotEmpty(self, ctx: SparqlParser.PropertyListNotEmptyContext):
        ctx.slots = strictDict({"relation": "", "tail": "", "dtype": ""})
        return super().enterPropertyListNotEmpty(ctx)

    # Exit a parse tree produced by SparqlParser#propertyListNotEmpty.
    def exitPropertyListNotEmpty(self, ctx: SparqlParser.PropertyListNotEmptyContext):
        ctx.parentCtx.slots["relation"] = ctx.slots["relation"]
        ctx.parentCtx.slots["tail"] = ctx.slots["tail"]
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        return super().exitPropertyListNotEmpty(ctx)

    # Enter a parse tree produced by SparqlParser#propertyList.
    def enterPropertyList(self, ctx: SparqlParser.PropertyListContext):
        pass

    # Exit a parse tree produced by SparqlParser#propertyList.
    def exitPropertyList(self, ctx: SparqlParser.PropertyListContext):
        pass

    # Enter a parse tree produced by SparqlParser#objectList.
    def enterObjectList(self, ctx: SparqlParser.ObjectListContext):
        ctx.slots = strictDict({"tail": "", "dtype": ""})
        return super().enterObjectList(ctx)

    # Exit a parse tree produced by SparqlParser#objectList.
    def exitObjectList(self, ctx: SparqlParser.ObjectListContext):
        ctx.parentCtx.slots["tail"] = ctx.slots["tail"]
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        return super().exitObjectList(ctx)

    # Enter a parse tree produced by SparqlParser#object_.
    def enterObject_(self, ctx: SparqlParser.Object_Context):
        ctx.slots = strictDict({"tail": "", "dtype": ""})
        return super().enterObjectList(ctx)

    # Exit a parse tree produced by SparqlParser#object_.
    def exitObject_(self, ctx: SparqlParser.Object_Context):
        ctx.parentCtx.slots["tail"] = ctx.slots["tail"]
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        return super().exitObjectList(ctx)

    # Enter a parse tree produced by SparqlParser#verb.
    def enterVerb(self, ctx: SparqlParser.VerbContext):
        ctx.slots = strictDict({"var": "", "predicate": "", "dtype": ""})
        return super().enterVerb(ctx)

    # Exit a parse tree produced by SparqlParser#verb.
    def exitVerb(self, ctx: SparqlParser.VerbContext):
        if ctx.slots["predicate"]:
            ctx.parentCtx.slots["relation"] = ctx.slots["predicate"]
        else:
            ctx.parentCtx.slots["relation"] = ctx.slots["var"]
        return super().exitVerb(ctx)

    # Enter a parse tree produced by SparqlParser#triplesNode.
    def enterTriplesNode(self, ctx: SparqlParser.TriplesNodeContext):
        pass

    # Exit a parse tree produced by SparqlParser#triplesNode.
    def exitTriplesNode(self, ctx: SparqlParser.TriplesNodeContext):
        pass

    # Enter a parse tree produced by SparqlParser#blankNodePropertyList.
    def enterBlankNodePropertyList(self, ctx: SparqlParser.BlankNodePropertyListContext):
        pass

    # Exit a parse tree produced by SparqlParser#blankNodePropertyList.
    def exitBlankNodePropertyList(self, ctx: SparqlParser.BlankNodePropertyListContext):
        pass

    # Enter a parse tree produced by SparqlParser#collection.
    def enterCollection(self, ctx: SparqlParser.CollectionContext):
        pass

    # Exit a parse tree produced by SparqlParser#collection.
    def exitCollection(self, ctx: SparqlParser.CollectionContext):
        pass

    # Enter a parse tree produced by SparqlParser#graphNode.
    def enterGraphNode(self, ctx: SparqlParser.GraphNodeContext):
        ctx.slots = strictDict({"head": "", "dtype": ""})
        return super().enterGraphNode(ctx)

    # Exit a parse tree produced by SparqlParser#graphNode.
    def exitGraphNode(self, ctx: SparqlParser.GraphNodeContext):
        ctx.parentCtx.slots["tail"] = ctx.slots["head"]
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        return super().exitGraphNode(ctx)

    # Enter a parse tree produced by SparqlParser#varOrTerm.
    def enterVarOrTerm(self, ctx: SparqlParser.VarOrTermContext):
        ctx.slots = strictDict({"var": "", "dtype": ""})
        return super().enterVarOrTerm(ctx)

    # Exit a parse tree produced by SparqlParser#varOrTerm.
    def exitVarOrTerm(self, ctx: SparqlParser.VarOrTermContext):
        ctx.parentCtx.slots["head"] = ctx.slots["var"]
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        return super().exitVarOrTerm(ctx)

    # Enter a parse tree produced by SparqlParser#varOrIRIref.
    def enterVarOrIRIref(self, ctx: SparqlParser.VarOrIRIrefContext):
        ctx.slots = strictDict({"predicate": "", "var": "", "dtype": ""})
        return super().enterVarOrIRIref(ctx)

    # Exit a parse tree produced by SparqlParser#varOrIRIref.
    def exitVarOrIRIref(self, ctx: SparqlParser.VarOrIRIrefContext):
        ctx.parentCtx.slots["predicate"] = ctx.slots["predicate"]
        ctx.parentCtx.slots["var"] = ctx.slots["var"]
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        return super().exitVarOrIRIref(ctx)

    # Enter a parse tree produced by SparqlParser#var_.
    def enterVar_(self, ctx: SparqlParser.Var_Context):
        assert ctx.getText() != "*"
        return super().enterVar_(ctx)

    # Exit a parse tree produced by SparqlParser#var_.
    def exitVar_(self, ctx: SparqlParser.Var_Context):
        ctx.parentCtx.slots["var"] = ctx.getText()
        ctx.parentCtx.slots["dtype"] = "var"
        return super().exitVar_(ctx)

    # Enter a parse tree produced by SparqlParser#graphTerm.
    def enterGraphTerm(self, ctx: SparqlParser.GraphTermContext):
        ctx.slots = strictDict({"value": "", "dtype": ""})
        return super().enterGraphTerm(ctx)

    # Exit a parse tree produced by SparqlParser#graphTerm.
    def exitGraphTerm(self, ctx: SparqlParser.GraphTermContext):
        ctx.parentCtx.slots["var"] = ctx.slots["value"]
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        return super().exitGraphTerm(ctx)

    # Enter a parse tree produced by SparqlParser#expression.
    def enterExpression(self, ctx: SparqlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#expression.
    def exitExpression(self, ctx: SparqlParser.ExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx: SparqlParser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx: SparqlParser.ConditionalOrExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx: SparqlParser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx: SparqlParser.ConditionalAndExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#valueLogical.
    def enterValueLogical(self, ctx: SparqlParser.ValueLogicalContext):
        pass

    # Exit a parse tree produced by SparqlParser#valueLogical.
    def exitValueLogical(self, ctx: SparqlParser.ValueLogicalContext):
        pass

    # Enter a parse tree produced by SparqlParser#relationalExpression.
    def enterRelationalExpression(self, ctx: SparqlParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#relationalExpression.
    def exitRelationalExpression(self, ctx: SparqlParser.RelationalExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#numericExpression.
    def enterNumericExpression(self, ctx: SparqlParser.NumericExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericExpression.
    def exitNumericExpression(self, ctx: SparqlParser.NumericExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#additiveExpression.
    def enterAdditiveExpression(self, ctx: SparqlParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#additiveExpression.
    def exitAdditiveExpression(self, ctx: SparqlParser.AdditiveExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx: SparqlParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx: SparqlParser.MultiplicativeExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#unaryExpression.
    def enterUnaryExpression(self, ctx: SparqlParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#unaryExpression.
    def exitUnaryExpression(self, ctx: SparqlParser.UnaryExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#primaryExpression.
    def enterPrimaryExpression(self, ctx: SparqlParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#primaryExpression.
    def exitPrimaryExpression(self, ctx: SparqlParser.PrimaryExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#brackettedExpression.
    def enterBrackettedExpression(self, ctx: SparqlParser.BrackettedExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#brackettedExpression.
    def exitBrackettedExpression(self, ctx: SparqlParser.BrackettedExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#builtInCall.
    def enterBuiltInCall(self, ctx: SparqlParser.BuiltInCallContext):
        pass

    # Exit a parse tree produced by SparqlParser#builtInCall.
    def exitBuiltInCall(self, ctx: SparqlParser.BuiltInCallContext):
        pass

    # Enter a parse tree produced by SparqlParser#regexExpression.
    def enterRegexExpression(self, ctx: SparqlParser.RegexExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#regexExpression.
    def exitRegexExpression(self, ctx: SparqlParser.RegexExpressionContext):
        pass

    # Enter a parse tree produced by SparqlParser#iriRefOrFunction.
    def enterIriRefOrFunction(self, ctx: SparqlParser.IriRefOrFunctionContext):
        pass

    # Exit a parse tree produced by SparqlParser#iriRefOrFunction.
    def exitIriRefOrFunction(self, ctx: SparqlParser.IriRefOrFunctionContext):
        pass

    # Enter a parse tree produced by SparqlParser#rdfLiteral.
    def enterRdfLiteral(self, ctx: SparqlParser.RdfLiteralContext):
        ctx.slots = strictDict({"value": "", "dtype": ""})
        return super().enterRdfLiteral(ctx)

    # Exit a parse tree produced by SparqlParser#rdfLiteral.
    def exitRdfLiteral(self, ctx: SparqlParser.RdfLiteralContext):
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        if not ctx.slots["dtype"]:
            ctx.slots["dtype"] = "string"
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        return super().exitRdfLiteral(ctx)
    # Enter a parse tree produced by SparqlParser#numericLiteral.
    def enterNumericLiteral(self, ctx: SparqlParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericLiteral.
    def exitNumericLiteral(self, ctx: SparqlParser.NumericLiteralContext):
        pass

    # Enter a parse tree produced by SparqlParser#numericLiteralUnsigned.
    def enterNumericLiteralUnsigned(self, ctx: SparqlParser.NumericLiteralUnsignedContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericLiteralUnsigned.
    def exitNumericLiteralUnsigned(self, ctx: SparqlParser.NumericLiteralUnsignedContext):
        pass

    # Enter a parse tree produced by SparqlParser#numericLiteralPositive.
    def enterNumericLiteralPositive(self, ctx: SparqlParser.NumericLiteralPositiveContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericLiteralPositive.
    def exitNumericLiteralPositive(self, ctx: SparqlParser.NumericLiteralPositiveContext):
        pass

    # Enter a parse tree produced by SparqlParser#numericLiteralNegative.
    def enterNumericLiteralNegative(self, ctx: SparqlParser.NumericLiteralNegativeContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericLiteralNegative.
    def exitNumericLiteralNegative(self, ctx: SparqlParser.NumericLiteralNegativeContext):
        pass

    # Enter a parse tree produced by SparqlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx: SparqlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SparqlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx: SparqlParser.BooleanLiteralContext):
        pass

    # Enter a parse tree produced by SparqlParser#string.
    def enterString(self, ctx: SparqlParser.StringContext):
        if not isinstance(ctx.parentCtx, SparqlParser.StringContext):
            ctx.parentCtx.slots["value"] = str(ctx.getText()).replace('"', '')

    # Exit a parse tree produced by SparqlParser#string.
    def exitString(self, ctx: SparqlParser.StringContext):
        pass

    # Enter a parse tree produced by SparqlParser#iriRef.
    def enterIriRef(self, ctx: SparqlParser.IriRefContext):
        return super().enterIriRef(ctx)

    # Exit a parse tree produced by SparqlParser#iriRef.
    def exitIriRef(self, ctx: SparqlParser.IriRefContext):
        ctx.parentCtx.slots["predicate"] = ctx.getText()
        return super().exitIriRef(ctx)

    # Enter a parse tree produced by SparqlParser#prefixedName.
    def enterPrefixedName(self, ctx: SparqlParser.PrefixedNameContext):
        pass

    # Exit a parse tree produced by SparqlParser#prefixedName.
    def exitPrefixedName(self, ctx: SparqlParser.PrefixedNameContext):
        pass

    # Enter a parse tree produced by SparqlParser#blankNode.
    def enterBlankNode(self, ctx: SparqlParser.BlankNodeContext):
        pass

    # Exit a parse tree produced by SparqlParser#blankNode.
    def exitBlankNode(self, ctx: SparqlParser.BlankNodeContext):
        pass


def merge_dict(d1: dict, d2: dict):
    new_dict = {}
    for key in d1.keys():
        if key not in new_dict.keys():
            new_dict[key] = []
        new_dict[key].extend(d1[key])

    for key in d2.keys():
        if key not in new_dict.keys():
            new_dict[key] = []
        new_dict[key].extend(d2[key])

    return new_dict


def get_class_label(table: dict):
    assert '?c' in table.keys()
    for triple in table['?c']:
        if triple[0] == '?c' and triple[1] == '<pred:name>':
            return triple[2]
    return ''

def get_attribute(table: dict, var):
    assert var in table.keys()
    label, value = '', ''
    for triple in table[var]:
        if triple[2] == var:
            label = triple[1].strip('"').replace('<', '').replace('>', '')
        if triple[0] == var and triple[1] == '<pred:value>':
            value = triple[2]

    return label, value




