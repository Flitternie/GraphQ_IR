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
        self.SOP = {
            "<": "smaller than",
            ">": "larger than",
            '=': 'is',
            '!=': 'is not'
        }
        self.VTYPE = {
            "xsd:double": 'number'
        }
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
        if self.queryType == "CountQuery":
            self.ir = "how many {}".format(ctx.slots["entitySet"])
        if self.queryType == 'AttributeQuery':
            self.ir = "what is the attribute {} Of {}".format(ctx.slots["attribute"], ctx.slots["entitySet"])
        if self.queryType == "PredicateQuery":
            self.ir = "what is the relation from {} to {}".format(ctx.slots["relationEntitySet1"], ctx.slots["relationEntitySet2"])
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
        ctx.slots = strictDict({"triple_table": dict(), "filter_table": dict()})
        return super().enterGroupGraphPattern(ctx)

    # Exit a parse tree produced by SparqlParser#groupGraphPattern.
    def exitGroupGraphPattern(self, ctx: SparqlParser.GroupGraphPatternContext):
        if isinstance(ctx.parentCtx, SparqlParser.WhereClauseContext):
            if self.queryType == 'CountQuery' or self.queryType == 'EntityQuery':
                print(ctx.slots['triple_table'])
                print(ctx.slots['filter_table'])
                ctx.parentCtx.slots['entitySet'] = scout_entity_set(
                    ctx.slots['triple_table'], ctx.slots['filter_table'], self.query_var
                )

            if self.queryType == 'AttributeQuery':
                print(ctx.slots['triple_table'])
                print(ctx.slots['filter_table'])
                attribute = ''
                es_var = ''

                for triple in ctx.slots['triple_table'][self.query_var]:
                    if triple[2] == self.query_var:
                        attribute = '<A> {} </A>'.format(re.sub(r'[<>]', '', triple[1]).replace('_', ' '))
                        es_var = triple[0]
                        break

                es = scout_entity_set(
                    ctx.slots['triple_table'], ctx.slots['filter_table'], es_var, excluding=[self.query_var]
                )
                ctx.parentCtx.slots['entitySet'] = es
                ctx.parentCtx.slots['attribute'] = attribute
            if self.queryType == 'PredicateQuery':
                print(ctx.slots['triple_table'])
                print(ctx.slots['filter_table'])
                es_var1, es_var2 = '', ''
                for triple in ctx.slots['triple_table'][self.query_var]:
                    if triple[1] == self.query_var:
                        es_var1 = triple[0]
                        es_var2 = triple[2]

                es1 = scout_entity_set(
                    ctx.slots['triple_table'], ctx.slots['filter_table'], es_var1, excluding=[self.query_var]
                )
                es2 = scout_entity_set(
                    ctx.slots['triple_table'], ctx.slots['filter_table'], es_var2, excluding=[self.query_var]
                )
                ctx.parentCtx.slots['relationEntitySet1'] = es1
                ctx.parentCtx.slots['relationEntitySet2'] = es2

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
        ctx.slots = strictDict({'var': "", "sop": "", "vtype": "", "value": ""})
        return super().enterFilter_(ctx)

    # Exit a parse tree produced by SparqlParser#filter_.
    def exitFilter_(self, ctx: SparqlParser.Filter_Context):
        if ctx.slots['var'] not in ctx.parentCtx.slots['filter_table'].keys():
            ctx.parentCtx.slots['filter_table'][ctx.slots['var']] = []

        ctx.parentCtx.slots['filter_table'][ctx.slots['var']].append(
            (ctx.slots['sop'], ctx.slots['vtype'], ctx.slots['value'])
        )
        return super().exitFilter_(ctx)

    # Enter a parse tree produced by SparqlParser#constraint.
    def enterConstraint(self, ctx: SparqlParser.ConstraintContext):
        ctx.slots = strictDict({'var': "", "sop": "", "vtype": "", "value": ""})
        return super().enterConstraint(ctx)

    # Exit a parse tree produced by SparqlParser#constraint.
    def exitConstraint(self, ctx: SparqlParser.ConstraintContext):
        ctx.parentCtx.slots['var'] = ctx.slots['var']
        ctx.parentCtx.slots['sop'] = ctx.slots['sop']
        ctx.parentCtx.slots['vtype'] = ctx.slots['vtype']
        ctx.parentCtx.slots['value'] = ctx.slots['value']
        return super().exitConstraint(ctx)

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
            self.queryType = "PredicateQuery"
        elif ctx.slots["tail"] == self.query_var and not self.queryType:
            self.queryType = "EntityQuery"

        if ctx.slots['head'] not in ctx.parentCtx.slots['triple_table'].keys():
            ctx.parentCtx.slots['triple_table'][ctx.slots['head']] = []
        if ctx.slots['relation'] not in ctx.parentCtx.slots['triple_table'].keys() and\
                ctx.slots['relation'].startswith('?'):
            ctx.parentCtx.slots['triple_table'][ctx.slots['relation']] = []
        if ctx.slots['dtype'] == 'var' and ctx.slots['tail'] not in ctx.parentCtx.slots['triple_table'].keys():
            ctx.parentCtx.slots['triple_table'][ctx.slots['tail']] = []

        ctx.parentCtx.slots['triple_table'][ctx.slots['head']].append(
            (ctx.slots['head'], ctx.slots['relation'], ctx.slots['tail']))

        if ctx.slots['relation'].startswith('?'):
            ctx.parentCtx.slots['triple_table'][ctx.slots['relation']].append(
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
        ctx.slots = strictDict({'var': "", "sop": "", "vtype": "", "value": ""})
        return super().enterExpression(ctx)

    # Exit a parse tree produced by SparqlParser#expression.
    def exitExpression(self, ctx: SparqlParser.ExpressionContext):
        ctx.parentCtx.slots['var'] = ctx.slots['var']
        ctx.parentCtx.slots['sop'] = ctx.slots['sop']
        ctx.parentCtx.slots['vtype'] = ctx.slots['vtype']
        ctx.parentCtx.slots['value'] = ctx.slots['value']
        return super().exitExpression(ctx)

    # Enter a parse tree produced by SparqlParser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx: SparqlParser.ConditionalOrExpressionContext):
        ctx.slots = strictDict({'var': "", "sop": "", "vtype": "", "value": ""})
        return super().enterConditionalOrExpression(ctx)

    # Exit a parse tree produced by SparqlParser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx: SparqlParser.ConditionalOrExpressionContext):
        ctx.parentCtx.slots['var'] = ctx.slots['var']
        ctx.parentCtx.slots['sop'] = ctx.slots['sop']
        ctx.parentCtx.slots['vtype'] = ctx.slots['vtype']
        ctx.parentCtx.slots['value'] = ctx.slots['value']
        return super().exitConditionalOrExpression(ctx)

    # Enter a parse tree produced by SparqlParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx: SparqlParser.ConditionalAndExpressionContext):
        ctx.slots = strictDict({'var': "", "sop": "", "vtype": "", "value": ""})
        return super().enterConditionalAndExpression(ctx)

    # Exit a parse tree produced by SparqlParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx: SparqlParser.ConditionalAndExpressionContext):
        ctx.parentCtx.slots['var'] = ctx.slots['var']
        ctx.parentCtx.slots['sop'] = ctx.slots['sop']
        ctx.parentCtx.slots['vtype'] = ctx.slots['vtype']
        ctx.parentCtx.slots['value'] = ctx.slots['value']
        return super().exitConditionalAndExpression(ctx)

    # Enter a parse tree produced by SparqlParser#valueLogical.
    def enterValueLogical(self, ctx: SparqlParser.ValueLogicalContext):
        ctx.slots = strictDict({'var': "", "sop": "", "vtype": "", "value": ""})
        return super().enterValueLogical(ctx)

    # Exit a parse tree produced by SparqlParser#valueLogical.
    def exitValueLogical(self, ctx: SparqlParser.ValueLogicalContext):
        ctx.parentCtx.slots['var'] = ctx.slots['var']
        ctx.parentCtx.slots['sop'] = ctx.slots['sop']
        ctx.parentCtx.slots['vtype'] = ctx.slots['vtype']
        ctx.parentCtx.slots['value'] = ctx.slots['value']
        return super().exitValueLogical(ctx)

    # Enter a parse tree produced by SparqlParser#relationalExpression.
    def enterRelationalExpression(self, ctx: SparqlParser.RelationalExpressionContext):
        return super().enterNumericExpression(ctx)

    # Exit a parse tree produced by SparqlParser#relationalExpression.
    def exitRelationalExpression(self, ctx: SparqlParser.RelationalExpressionContext):
        left, op, right = ctx.getChildren()
        if left.slots['dtype'] == 'var' and right.slots['dtype'] != 'var':
            ctx.parentCtx.slots['var'] = left.slots['var']
            ctx.parentCtx.slots['sop'] = self.SOP[op.getText()]
            ctx.parentCtx.slots['vtype'] = self.VTYPE[right.slots['dtype']]
            ctx.parentCtx.slots['value'] = right.slots['value']

        return super().exitRelationalExpression(ctx)

    # Enter a parse tree produced by SparqlParser#numericExpression.
    def enterNumericExpression(self, ctx: SparqlParser.NumericExpressionContext):
        ctx.slots = strictDict({"var": "", "dtype": "", "value": ""})
        return super().enterNumericExpression(ctx)

    # Exit a parse tree produced by SparqlParser#numericExpression.
    def exitNumericExpression(self, ctx: SparqlParser.NumericExpressionContext):
        return super().exitNumericExpression(ctx)

    # Enter a parse tree produced by SparqlParser#additiveExpression.
    def enterAdditiveExpression(self, ctx: SparqlParser.AdditiveExpressionContext):
        ctx.slots = strictDict({"var": "", "dtype": "", "value": ""})
        return super().enterAdditiveExpression(ctx)

    # Exit a parse tree produced by SparqlParser#additiveExpression.
    def exitAdditiveExpression(self, ctx: SparqlParser.AdditiveExpressionContext):
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        ctx.parentCtx.slots["var"] = ctx.slots["var"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        return super().enterAdditiveExpression(ctx)

    # Enter a parse tree produced by SparqlParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx: SparqlParser.MultiplicativeExpressionContext):
        ctx.slots = strictDict({"var": "", "dtype": "", "value": ""})
        return super().enterMultiplicativeExpression(ctx)

    # Exit a parse tree produced by SparqlParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx: SparqlParser.MultiplicativeExpressionContext):
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        ctx.parentCtx.slots["var"] = ctx.slots["var"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        return super().exitMultiplicativeExpression(ctx)

    # Enter a parse tree produced by SparqlParser#unaryExpression.
    def enterUnaryExpression(self, ctx: SparqlParser.UnaryExpressionContext):
        ctx.slots = strictDict({"var": "", "dtype": "", "value": ""})
        return super().enterUnaryExpression(ctx)

    # Exit a parse tree produced by SparqlParser#unaryExpression.
    def exitUnaryExpression(self, ctx: SparqlParser.UnaryExpressionContext):
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        ctx.parentCtx.slots["var"] = ctx.slots["var"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        return super().exitUnaryExpression(ctx)

    # Enter a parse tree produced by SparqlParser#primaryExpression.
    def enterPrimaryExpression(self, ctx: SparqlParser.PrimaryExpressionContext):
        ctx.slots = strictDict({"var": "", "dtype": "", "value": ""})
        return super().enterPrimaryExpression(ctx)

    # Exit a parse tree produced by SparqlParser#primaryExpression.
    def exitPrimaryExpression(self, ctx: SparqlParser.PrimaryExpressionContext):
        ctx.parentCtx.slots["dtype"] = ctx.slots["dtype"]
        ctx.parentCtx.slots["var"] = ctx.slots["var"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        return super().exitPrimaryExpression(ctx)

    # Enter a parse tree produced by SparqlParser#brackettedExpression.
    def enterBrackettedExpression(self, ctx: SparqlParser.BrackettedExpressionContext):
        ctx.slots = strictDict({'var': "", "sop": "", "vtype": "", "value": ""})
        return super().enterBrackettedExpression(ctx)

    # Exit a parse tree produced by SparqlParser#brackettedExpression.
    def exitBrackettedExpression(self, ctx: SparqlParser.BrackettedExpressionContext):
        ctx.parentCtx.slots['var'] = ctx.slots['var']
        ctx.parentCtx.slots['sop'] = ctx.slots['sop']
        ctx.parentCtx.slots['vtype'] = ctx.slots['vtype']
        ctx.parentCtx.slots['value'] = ctx.slots['value']
        return super().exitBrackettedExpression(ctx)

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
        if isinstance(ctx.parentCtx, SparqlParser.VarOrIRIrefContext):
            ctx.parentCtx.slots["predicate"] = ctx.getText()
        else:
            ctx.parentCtx.slots["dtype"] = ctx.getText()
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


def get_label(table: dict, var):
    assert var in table.keys()
    for triple in table[var]:
        if triple[0] == var and triple[1] == '<pred:name>':
            return triple[2]
    return ''


def get_attribute(triple_table: dict, filter_table: dict, var):
    assert var in triple_table.keys()
    constraints = []
    for triple in triple_table[var]:
        if triple[0] == var and triple[1] == '<pred:value>':
            if not triple[2].startswith('?'):
                return [('is', 'text', triple[2], '')]
            else:
                for tp in triple_table[var]:
                    if tp[0] == var and tp[1] == '<pred:unit>':
                        if tp[2] == '1':
                            unit = ''
                            break
                        else:
                            unit = tp[2] + ' '
                            break
                for ft in filter_table[triple[2]]:
                    constraints.append((*ft, unit))
                return constraints


def scout_entity_set(triple_table: dict, filter_table: dict, var: str, excluding=[]):
    entity = ''
    cls = ''
    entitySets = []
    for triple in triple_table[var]:
        if triple[2] == '?c':
            cls = '<C> {} </C>'.format(get_label(triple_table, '?c'))
        if triple[1] == '<pred:name>':
            entity = '<E> {} </E>'.format(triple[2])

    if entity == '' and cls != '':
        entity = cls
    elif entity == '' and cls == '':
        entity = 'Ones'
    elif cls != '' and cls != '':
        entity = '{} {}'.format(cls, entity)

    for triple in triple_table[var]:
        if triple[2].startswith('?pv') and triple[2] not in excluding and triple[1] not in excluding:
            entity_set = '<ES> {} whose <A> {} </A> {} {} <V> {} {}</V> </ES>'
            attr = triple[1].strip('"').replace('<', '').replace('>', '')
            constraints = get_attribute(triple_table, filter_table, triple[2])
            for constraint in constraints:
                entity_set = entity_set.format(entity, attr, *constraint)
                entitySets.append(entity_set)

    if entitySets:
        ES = f"{entitySets.pop()}"
        while len(entitySets) != 0:
            es = entitySets.pop()
            ES = "<ES> {} and {} </ES>".format(ES, es)
    else:
        ES = entity

    return ES
