# Generated from Sparql.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SparqlParser import SparqlParser
else:
    from SparqlParser import SparqlParser

# This class defines a complete listener for a parse tree produced by SparqlParser.
class SparqlListener(ParseTreeListener):

    # Enter a parse tree produced by SparqlParser#query.
    def enterQuery(self, ctx:SparqlParser.QueryContext):
        pass

    # Exit a parse tree produced by SparqlParser#query.
    def exitQuery(self, ctx:SparqlParser.QueryContext):
        pass


    # Enter a parse tree produced by SparqlParser#prologue.
    def enterPrologue(self, ctx:SparqlParser.PrologueContext):
        pass

    # Exit a parse tree produced by SparqlParser#prologue.
    def exitPrologue(self, ctx:SparqlParser.PrologueContext):
        pass


    # Enter a parse tree produced by SparqlParser#baseDecl.
    def enterBaseDecl(self, ctx:SparqlParser.BaseDeclContext):
        pass

    # Exit a parse tree produced by SparqlParser#baseDecl.
    def exitBaseDecl(self, ctx:SparqlParser.BaseDeclContext):
        pass


    # Enter a parse tree produced by SparqlParser#prefixDecl.
    def enterPrefixDecl(self, ctx:SparqlParser.PrefixDeclContext):
        pass

    # Exit a parse tree produced by SparqlParser#prefixDecl.
    def exitPrefixDecl(self, ctx:SparqlParser.PrefixDeclContext):
        pass


    # Enter a parse tree produced by SparqlParser#selectQuery.
    def enterSelectQuery(self, ctx:SparqlParser.SelectQueryContext):
        pass

    # Exit a parse tree produced by SparqlParser#selectQuery.
    def exitSelectQuery(self, ctx:SparqlParser.SelectQueryContext):
        pass


    # Enter a parse tree produced by SparqlParser#entityQueryCondition.
    def enterEntityQueryCondition(self, ctx:SparqlParser.EntityQueryConditionContext):
        pass

    # Exit a parse tree produced by SparqlParser#entityQueryCondition.
    def exitEntityQueryCondition(self, ctx:SparqlParser.EntityQueryConditionContext):
        pass


    # Enter a parse tree produced by SparqlParser#countQueryCondition.
    def enterCountQueryCondition(self, ctx:SparqlParser.CountQueryConditionContext):
        pass

    # Exit a parse tree produced by SparqlParser#countQueryCondition.
    def exitCountQueryCondition(self, ctx:SparqlParser.CountQueryConditionContext):
        pass


    # Enter a parse tree produced by SparqlParser#constructQuery.
    def enterConstructQuery(self, ctx:SparqlParser.ConstructQueryContext):
        pass

    # Exit a parse tree produced by SparqlParser#constructQuery.
    def exitConstructQuery(self, ctx:SparqlParser.ConstructQueryContext):
        pass


    # Enter a parse tree produced by SparqlParser#describeQuery.
    def enterDescribeQuery(self, ctx:SparqlParser.DescribeQueryContext):
        pass

    # Exit a parse tree produced by SparqlParser#describeQuery.
    def exitDescribeQuery(self, ctx:SparqlParser.DescribeQueryContext):
        pass


    # Enter a parse tree produced by SparqlParser#askQuery.
    def enterAskQuery(self, ctx:SparqlParser.AskQueryContext):
        pass

    # Exit a parse tree produced by SparqlParser#askQuery.
    def exitAskQuery(self, ctx:SparqlParser.AskQueryContext):
        pass


    # Enter a parse tree produced by SparqlParser#datasetClause.
    def enterDatasetClause(self, ctx:SparqlParser.DatasetClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#datasetClause.
    def exitDatasetClause(self, ctx:SparqlParser.DatasetClauseContext):
        pass


    # Enter a parse tree produced by SparqlParser#defaultGraphClause.
    def enterDefaultGraphClause(self, ctx:SparqlParser.DefaultGraphClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#defaultGraphClause.
    def exitDefaultGraphClause(self, ctx:SparqlParser.DefaultGraphClauseContext):
        pass


    # Enter a parse tree produced by SparqlParser#namedGraphClause.
    def enterNamedGraphClause(self, ctx:SparqlParser.NamedGraphClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#namedGraphClause.
    def exitNamedGraphClause(self, ctx:SparqlParser.NamedGraphClauseContext):
        pass


    # Enter a parse tree produced by SparqlParser#sourceSelector.
    def enterSourceSelector(self, ctx:SparqlParser.SourceSelectorContext):
        pass

    # Exit a parse tree produced by SparqlParser#sourceSelector.
    def exitSourceSelector(self, ctx:SparqlParser.SourceSelectorContext):
        pass


    # Enter a parse tree produced by SparqlParser#whereClause.
    def enterWhereClause(self, ctx:SparqlParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#whereClause.
    def exitWhereClause(self, ctx:SparqlParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by SparqlParser#solutionModifier.
    def enterSolutionModifier(self, ctx:SparqlParser.SolutionModifierContext):
        pass

    # Exit a parse tree produced by SparqlParser#solutionModifier.
    def exitSolutionModifier(self, ctx:SparqlParser.SolutionModifierContext):
        pass


    # Enter a parse tree produced by SparqlParser#limitOffsetClauses.
    def enterLimitOffsetClauses(self, ctx:SparqlParser.LimitOffsetClausesContext):
        pass

    # Exit a parse tree produced by SparqlParser#limitOffsetClauses.
    def exitLimitOffsetClauses(self, ctx:SparqlParser.LimitOffsetClausesContext):
        pass


    # Enter a parse tree produced by SparqlParser#orderClause.
    def enterOrderClause(self, ctx:SparqlParser.OrderClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#orderClause.
    def exitOrderClause(self, ctx:SparqlParser.OrderClauseContext):
        pass


    # Enter a parse tree produced by SparqlParser#orderCondition.
    def enterOrderCondition(self, ctx:SparqlParser.OrderConditionContext):
        pass

    # Exit a parse tree produced by SparqlParser#orderCondition.
    def exitOrderCondition(self, ctx:SparqlParser.OrderConditionContext):
        pass


    # Enter a parse tree produced by SparqlParser#limitClause.
    def enterLimitClause(self, ctx:SparqlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#limitClause.
    def exitLimitClause(self, ctx:SparqlParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by SparqlParser#offsetClause.
    def enterOffsetClause(self, ctx:SparqlParser.OffsetClauseContext):
        pass

    # Exit a parse tree produced by SparqlParser#offsetClause.
    def exitOffsetClause(self, ctx:SparqlParser.OffsetClauseContext):
        pass


    # Enter a parse tree produced by SparqlParser#groupGraphPattern.
    def enterGroupGraphPattern(self, ctx:SparqlParser.GroupGraphPatternContext):
        pass

    # Exit a parse tree produced by SparqlParser#groupGraphPattern.
    def exitGroupGraphPattern(self, ctx:SparqlParser.GroupGraphPatternContext):
        pass


    # Enter a parse tree produced by SparqlParser#triplesBlock.
    def enterTriplesBlock(self, ctx:SparqlParser.TriplesBlockContext):
        pass

    # Exit a parse tree produced by SparqlParser#triplesBlock.
    def exitTriplesBlock(self, ctx:SparqlParser.TriplesBlockContext):
        pass


    # Enter a parse tree produced by SparqlParser#graphPatternNotTriples.
    def enterGraphPatternNotTriples(self, ctx:SparqlParser.GraphPatternNotTriplesContext):
        pass

    # Exit a parse tree produced by SparqlParser#graphPatternNotTriples.
    def exitGraphPatternNotTriples(self, ctx:SparqlParser.GraphPatternNotTriplesContext):
        pass


    # Enter a parse tree produced by SparqlParser#optionalGraphPattern.
    def enterOptionalGraphPattern(self, ctx:SparqlParser.OptionalGraphPatternContext):
        pass

    # Exit a parse tree produced by SparqlParser#optionalGraphPattern.
    def exitOptionalGraphPattern(self, ctx:SparqlParser.OptionalGraphPatternContext):
        pass


    # Enter a parse tree produced by SparqlParser#graphGraphPattern.
    def enterGraphGraphPattern(self, ctx:SparqlParser.GraphGraphPatternContext):
        pass

    # Exit a parse tree produced by SparqlParser#graphGraphPattern.
    def exitGraphGraphPattern(self, ctx:SparqlParser.GraphGraphPatternContext):
        pass


    # Enter a parse tree produced by SparqlParser#groupOrUnionGraphPattern.
    def enterGroupOrUnionGraphPattern(self, ctx:SparqlParser.GroupOrUnionGraphPatternContext):
        pass

    # Exit a parse tree produced by SparqlParser#groupOrUnionGraphPattern.
    def exitGroupOrUnionGraphPattern(self, ctx:SparqlParser.GroupOrUnionGraphPatternContext):
        pass


    # Enter a parse tree produced by SparqlParser#filter_.
    def enterFilter_(self, ctx:SparqlParser.Filter_Context):
        pass

    # Exit a parse tree produced by SparqlParser#filter_.
    def exitFilter_(self, ctx:SparqlParser.Filter_Context):
        pass


    # Enter a parse tree produced by SparqlParser#constraint.
    def enterConstraint(self, ctx:SparqlParser.ConstraintContext):
        pass

    # Exit a parse tree produced by SparqlParser#constraint.
    def exitConstraint(self, ctx:SparqlParser.ConstraintContext):
        pass


    # Enter a parse tree produced by SparqlParser#functionCall.
    def enterFunctionCall(self, ctx:SparqlParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SparqlParser#functionCall.
    def exitFunctionCall(self, ctx:SparqlParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SparqlParser#argList.
    def enterArgList(self, ctx:SparqlParser.ArgListContext):
        pass

    # Exit a parse tree produced by SparqlParser#argList.
    def exitArgList(self, ctx:SparqlParser.ArgListContext):
        pass


    # Enter a parse tree produced by SparqlParser#constructTemplate.
    def enterConstructTemplate(self, ctx:SparqlParser.ConstructTemplateContext):
        pass

    # Exit a parse tree produced by SparqlParser#constructTemplate.
    def exitConstructTemplate(self, ctx:SparqlParser.ConstructTemplateContext):
        pass


    # Enter a parse tree produced by SparqlParser#constructTriples.
    def enterConstructTriples(self, ctx:SparqlParser.ConstructTriplesContext):
        pass

    # Exit a parse tree produced by SparqlParser#constructTriples.
    def exitConstructTriples(self, ctx:SparqlParser.ConstructTriplesContext):
        pass


    # Enter a parse tree produced by SparqlParser#triplesSameSubject.
    def enterTriplesSameSubject(self, ctx:SparqlParser.TriplesSameSubjectContext):
        pass

    # Exit a parse tree produced by SparqlParser#triplesSameSubject.
    def exitTriplesSameSubject(self, ctx:SparqlParser.TriplesSameSubjectContext):
        pass


    # Enter a parse tree produced by SparqlParser#propertyListNotEmpty.
    def enterPropertyListNotEmpty(self, ctx:SparqlParser.PropertyListNotEmptyContext):
        pass

    # Exit a parse tree produced by SparqlParser#propertyListNotEmpty.
    def exitPropertyListNotEmpty(self, ctx:SparqlParser.PropertyListNotEmptyContext):
        pass


    # Enter a parse tree produced by SparqlParser#propertyList.
    def enterPropertyList(self, ctx:SparqlParser.PropertyListContext):
        pass

    # Exit a parse tree produced by SparqlParser#propertyList.
    def exitPropertyList(self, ctx:SparqlParser.PropertyListContext):
        pass


    # Enter a parse tree produced by SparqlParser#objectList.
    def enterObjectList(self, ctx:SparqlParser.ObjectListContext):
        pass

    # Exit a parse tree produced by SparqlParser#objectList.
    def exitObjectList(self, ctx:SparqlParser.ObjectListContext):
        pass


    # Enter a parse tree produced by SparqlParser#object_.
    def enterObject_(self, ctx:SparqlParser.Object_Context):
        pass

    # Exit a parse tree produced by SparqlParser#object_.
    def exitObject_(self, ctx:SparqlParser.Object_Context):
        pass


    # Enter a parse tree produced by SparqlParser#verb.
    def enterVerb(self, ctx:SparqlParser.VerbContext):
        pass

    # Exit a parse tree produced by SparqlParser#verb.
    def exitVerb(self, ctx:SparqlParser.VerbContext):
        pass


    # Enter a parse tree produced by SparqlParser#triplesNode.
    def enterTriplesNode(self, ctx:SparqlParser.TriplesNodeContext):
        pass

    # Exit a parse tree produced by SparqlParser#triplesNode.
    def exitTriplesNode(self, ctx:SparqlParser.TriplesNodeContext):
        pass


    # Enter a parse tree produced by SparqlParser#blankNodePropertyList.
    def enterBlankNodePropertyList(self, ctx:SparqlParser.BlankNodePropertyListContext):
        pass

    # Exit a parse tree produced by SparqlParser#blankNodePropertyList.
    def exitBlankNodePropertyList(self, ctx:SparqlParser.BlankNodePropertyListContext):
        pass


    # Enter a parse tree produced by SparqlParser#collection.
    def enterCollection(self, ctx:SparqlParser.CollectionContext):
        pass

    # Exit a parse tree produced by SparqlParser#collection.
    def exitCollection(self, ctx:SparqlParser.CollectionContext):
        pass


    # Enter a parse tree produced by SparqlParser#graphNode.
    def enterGraphNode(self, ctx:SparqlParser.GraphNodeContext):
        pass

    # Exit a parse tree produced by SparqlParser#graphNode.
    def exitGraphNode(self, ctx:SparqlParser.GraphNodeContext):
        pass


    # Enter a parse tree produced by SparqlParser#varOrTerm.
    def enterVarOrTerm(self, ctx:SparqlParser.VarOrTermContext):
        pass

    # Exit a parse tree produced by SparqlParser#varOrTerm.
    def exitVarOrTerm(self, ctx:SparqlParser.VarOrTermContext):
        pass


    # Enter a parse tree produced by SparqlParser#varOrIRIref.
    def enterVarOrIRIref(self, ctx:SparqlParser.VarOrIRIrefContext):
        pass

    # Exit a parse tree produced by SparqlParser#varOrIRIref.
    def exitVarOrIRIref(self, ctx:SparqlParser.VarOrIRIrefContext):
        pass


    # Enter a parse tree produced by SparqlParser#var_.
    def enterVar_(self, ctx:SparqlParser.Var_Context):
        pass

    # Exit a parse tree produced by SparqlParser#var_.
    def exitVar_(self, ctx:SparqlParser.Var_Context):
        pass


    # Enter a parse tree produced by SparqlParser#graphTerm.
    def enterGraphTerm(self, ctx:SparqlParser.GraphTermContext):
        pass

    # Exit a parse tree produced by SparqlParser#graphTerm.
    def exitGraphTerm(self, ctx:SparqlParser.GraphTermContext):
        pass


    # Enter a parse tree produced by SparqlParser#expression.
    def enterExpression(self, ctx:SparqlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#expression.
    def exitExpression(self, ctx:SparqlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:SparqlParser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx:SparqlParser.ConditionalOrExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:SparqlParser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:SparqlParser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#valueLogical.
    def enterValueLogical(self, ctx:SparqlParser.ValueLogicalContext):
        pass

    # Exit a parse tree produced by SparqlParser#valueLogical.
    def exitValueLogical(self, ctx:SparqlParser.ValueLogicalContext):
        pass


    # Enter a parse tree produced by SparqlParser#relationalExpression.
    def enterRelationalExpression(self, ctx:SparqlParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#relationalExpression.
    def exitRelationalExpression(self, ctx:SparqlParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#numericExpression.
    def enterNumericExpression(self, ctx:SparqlParser.NumericExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericExpression.
    def exitNumericExpression(self, ctx:SparqlParser.NumericExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:SparqlParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:SparqlParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:SparqlParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:SparqlParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#unaryExpression.
    def enterUnaryExpression(self, ctx:SparqlParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#unaryExpression.
    def exitUnaryExpression(self, ctx:SparqlParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:SparqlParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:SparqlParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#brackettedExpression.
    def enterBrackettedExpression(self, ctx:SparqlParser.BrackettedExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#brackettedExpression.
    def exitBrackettedExpression(self, ctx:SparqlParser.BrackettedExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#builtInCall.
    def enterBuiltInCall(self, ctx:SparqlParser.BuiltInCallContext):
        pass

    # Exit a parse tree produced by SparqlParser#builtInCall.
    def exitBuiltInCall(self, ctx:SparqlParser.BuiltInCallContext):
        pass


    # Enter a parse tree produced by SparqlParser#regexExpression.
    def enterRegexExpression(self, ctx:SparqlParser.RegexExpressionContext):
        pass

    # Exit a parse tree produced by SparqlParser#regexExpression.
    def exitRegexExpression(self, ctx:SparqlParser.RegexExpressionContext):
        pass


    # Enter a parse tree produced by SparqlParser#iriRefOrFunction.
    def enterIriRefOrFunction(self, ctx:SparqlParser.IriRefOrFunctionContext):
        pass

    # Exit a parse tree produced by SparqlParser#iriRefOrFunction.
    def exitIriRefOrFunction(self, ctx:SparqlParser.IriRefOrFunctionContext):
        pass


    # Enter a parse tree produced by SparqlParser#rdfLiteral.
    def enterRdfLiteral(self, ctx:SparqlParser.RdfLiteralContext):
        pass

    # Exit a parse tree produced by SparqlParser#rdfLiteral.
    def exitRdfLiteral(self, ctx:SparqlParser.RdfLiteralContext):
        pass


    # Enter a parse tree produced by SparqlParser#numericLiteral.
    def enterNumericLiteral(self, ctx:SparqlParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericLiteral.
    def exitNumericLiteral(self, ctx:SparqlParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by SparqlParser#numericLiteralUnsigned.
    def enterNumericLiteralUnsigned(self, ctx:SparqlParser.NumericLiteralUnsignedContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericLiteralUnsigned.
    def exitNumericLiteralUnsigned(self, ctx:SparqlParser.NumericLiteralUnsignedContext):
        pass


    # Enter a parse tree produced by SparqlParser#numericLiteralPositive.
    def enterNumericLiteralPositive(self, ctx:SparqlParser.NumericLiteralPositiveContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericLiteralPositive.
    def exitNumericLiteralPositive(self, ctx:SparqlParser.NumericLiteralPositiveContext):
        pass


    # Enter a parse tree produced by SparqlParser#numericLiteralNegative.
    def enterNumericLiteralNegative(self, ctx:SparqlParser.NumericLiteralNegativeContext):
        pass

    # Exit a parse tree produced by SparqlParser#numericLiteralNegative.
    def exitNumericLiteralNegative(self, ctx:SparqlParser.NumericLiteralNegativeContext):
        pass


    # Enter a parse tree produced by SparqlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SparqlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SparqlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SparqlParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SparqlParser#string.
    def enterString(self, ctx:SparqlParser.StringContext):
        pass

    # Exit a parse tree produced by SparqlParser#string.
    def exitString(self, ctx:SparqlParser.StringContext):
        pass


    # Enter a parse tree produced by SparqlParser#iriRef.
    def enterIriRef(self, ctx:SparqlParser.IriRefContext):
        pass

    # Exit a parse tree produced by SparqlParser#iriRef.
    def exitIriRef(self, ctx:SparqlParser.IriRefContext):
        pass


    # Enter a parse tree produced by SparqlParser#prefixedName.
    def enterPrefixedName(self, ctx:SparqlParser.PrefixedNameContext):
        pass

    # Exit a parse tree produced by SparqlParser#prefixedName.
    def exitPrefixedName(self, ctx:SparqlParser.PrefixedNameContext):
        pass


    # Enter a parse tree produced by SparqlParser#blankNode.
    def enterBlankNode(self, ctx:SparqlParser.BlankNodeContext):
        pass

    # Exit a parse tree produced by SparqlParser#blankNode.
    def exitBlankNode(self, ctx:SparqlParser.BlankNodeContext):
        pass



del SparqlParser