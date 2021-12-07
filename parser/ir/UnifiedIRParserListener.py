# Generated from ./KqaPro_Parser/ir/UnifiedIRParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .UnifiedIRParser import UnifiedIRParser
else:
    from UnifiedIRParser import UnifiedIRParser

# This class defines a complete listener for a parse tree produced by UnifiedIRParser.
class UnifiedIRParserListener(ParseTreeListener):

    # Enter a parse tree produced by UnifiedIRParser#query.
    def enterQuery(self, ctx:UnifiedIRParser.QueryContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#query.
    def exitQuery(self, ctx:UnifiedIRParser.QueryContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entityQuery.
    def enterEntityQuery(self, ctx:UnifiedIRParser.EntityQueryContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entityQuery.
    def exitEntityQuery(self, ctx:UnifiedIRParser.EntityQueryContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#attributeQuery.
    def enterAttributeQuery(self, ctx:UnifiedIRParser.AttributeQueryContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#attributeQuery.
    def exitAttributeQuery(self, ctx:UnifiedIRParser.AttributeQueryContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#predicateQuery.
    def enterPredicateQuery(self, ctx:UnifiedIRParser.PredicateQueryContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#predicateQuery.
    def exitPredicateQuery(self, ctx:UnifiedIRParser.PredicateQueryContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#qualifierQuery.
    def enterQualifierQuery(self, ctx:UnifiedIRParser.QualifierQueryContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#qualifierQuery.
    def exitQualifierQuery(self, ctx:UnifiedIRParser.QualifierQueryContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#countQuery.
    def enterCountQuery(self, ctx:UnifiedIRParser.CountQueryContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#countQuery.
    def exitCountQuery(self, ctx:UnifiedIRParser.CountQueryContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#verifyQuery.
    def enterVerifyQuery(self, ctx:UnifiedIRParser.VerifyQueryContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#verifyQuery.
    def exitVerifyQuery(self, ctx:UnifiedIRParser.VerifyQueryContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#selectQuery.
    def enterSelectQuery(self, ctx:UnifiedIRParser.SelectQueryContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#selectQuery.
    def exitSelectQuery(self, ctx:UnifiedIRParser.SelectQueryContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#verifyByAttribute.
    def enterVerifyByAttribute(self, ctx:UnifiedIRParser.VerifyByAttributeContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#verifyByAttribute.
    def exitVerifyByAttribute(self, ctx:UnifiedIRParser.VerifyByAttributeContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#verifyByPredicate.
    def enterVerifyByPredicate(self, ctx:UnifiedIRParser.VerifyByPredicateContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#verifyByPredicate.
    def exitVerifyByPredicate(self, ctx:UnifiedIRParser.VerifyByPredicateContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entitySetGroup.
    def enterEntitySetGroup(self, ctx:UnifiedIRParser.EntitySetGroupContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entitySetGroup.
    def exitEntitySetGroup(self, ctx:UnifiedIRParser.EntitySetGroupContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entitySetIntersect.
    def enterEntitySetIntersect(self, ctx:UnifiedIRParser.EntitySetIntersectContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entitySetIntersect.
    def exitEntitySetIntersect(self, ctx:UnifiedIRParser.EntitySetIntersectContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entitySetFilter.
    def enterEntitySetFilter(self, ctx:UnifiedIRParser.EntitySetFilterContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entitySetFilter.
    def exitEntitySetFilter(self, ctx:UnifiedIRParser.EntitySetFilterContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entitySetAtom.
    def enterEntitySetAtom(self, ctx:UnifiedIRParser.EntitySetAtomContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entitySetAtom.
    def exitEntitySetAtom(self, ctx:UnifiedIRParser.EntitySetAtomContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entitySetPlaceholder.
    def enterEntitySetPlaceholder(self, ctx:UnifiedIRParser.EntitySetPlaceholderContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entitySetPlaceholder.
    def exitEntitySetPlaceholder(self, ctx:UnifiedIRParser.EntitySetPlaceholderContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entitySetByAttribute.
    def enterEntitySetByAttribute(self, ctx:UnifiedIRParser.EntitySetByAttributeContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entitySetByAttribute.
    def exitEntitySetByAttribute(self, ctx:UnifiedIRParser.EntitySetByAttributeContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entitySetByPredicate.
    def enterEntitySetByPredicate(self, ctx:UnifiedIRParser.EntitySetByPredicateContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entitySetByPredicate.
    def exitEntitySetByPredicate(self, ctx:UnifiedIRParser.EntitySetByPredicateContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entitySetByConcept.
    def enterEntitySetByConcept(self, ctx:UnifiedIRParser.EntitySetByConceptContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entitySetByConcept.
    def exitEntitySetByConcept(self, ctx:UnifiedIRParser.EntitySetByConceptContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#filterByRank.
    def enterFilterByRank(self, ctx:UnifiedIRParser.FilterByRankContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#filterByRank.
    def exitFilterByRank(self, ctx:UnifiedIRParser.FilterByRankContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#filterByAttribute.
    def enterFilterByAttribute(self, ctx:UnifiedIRParser.FilterByAttributeContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#filterByAttribute.
    def exitFilterByAttribute(self, ctx:UnifiedIRParser.FilterByAttributeContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#filterByPredicate.
    def enterFilterByPredicate(self, ctx:UnifiedIRParser.FilterByPredicateContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#filterByPredicate.
    def exitFilterByPredicate(self, ctx:UnifiedIRParser.FilterByPredicateContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#filterByQualifier.
    def enterFilterByQualifier(self, ctx:UnifiedIRParser.FilterByQualifierContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#filterByQualifier.
    def exitFilterByQualifier(self, ctx:UnifiedIRParser.FilterByQualifierContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#forward.
    def enterForward(self, ctx:UnifiedIRParser.ForwardContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#forward.
    def exitForward(self, ctx:UnifiedIRParser.ForwardContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#backward.
    def enterBackward(self, ctx:UnifiedIRParser.BackwardContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#backward.
    def exitBackward(self, ctx:UnifiedIRParser.BackwardContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#and.
    def enterAnd(self, ctx:UnifiedIRParser.AndContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#and.
    def exitAnd(self, ctx:UnifiedIRParser.AndContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#or.
    def enterOr(self, ctx:UnifiedIRParser.OrContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#or.
    def exitOr(self, ctx:UnifiedIRParser.OrContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#equal.
    def enterEqual(self, ctx:UnifiedIRParser.EqualContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#equal.
    def exitEqual(self, ctx:UnifiedIRParser.EqualContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#notEqual.
    def enterNotEqual(self, ctx:UnifiedIRParser.NotEqualContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#notEqual.
    def exitNotEqual(self, ctx:UnifiedIRParser.NotEqualContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#larger.
    def enterLarger(self, ctx:UnifiedIRParser.LargerContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#larger.
    def exitLarger(self, ctx:UnifiedIRParser.LargerContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#smaller.
    def enterSmaller(self, ctx:UnifiedIRParser.SmallerContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#smaller.
    def exitSmaller(self, ctx:UnifiedIRParser.SmallerContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#largerEqual.
    def enterLargerEqual(self, ctx:UnifiedIRParser.LargerEqualContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#largerEqual.
    def exitLargerEqual(self, ctx:UnifiedIRParser.LargerEqualContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#smallerEqual.
    def enterSmallerEqual(self, ctx:UnifiedIRParser.SmallerEqualContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#smallerEqual.
    def exitSmallerEqual(self, ctx:UnifiedIRParser.SmallerEqualContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#largest.
    def enterLargest(self, ctx:UnifiedIRParser.LargestContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#largest.
    def exitLargest(self, ctx:UnifiedIRParser.LargestContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#smallest.
    def enterSmallest(self, ctx:UnifiedIRParser.SmallestContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#smallest.
    def exitSmallest(self, ctx:UnifiedIRParser.SmallestContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#text.
    def enterText(self, ctx:UnifiedIRParser.TextContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#text.
    def exitText(self, ctx:UnifiedIRParser.TextContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#quantity.
    def enterQuantity(self, ctx:UnifiedIRParser.QuantityContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#quantity.
    def exitQuantity(self, ctx:UnifiedIRParser.QuantityContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#date.
    def enterDate(self, ctx:UnifiedIRParser.DateContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#date.
    def exitDate(self, ctx:UnifiedIRParser.DateContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#year.
    def enterYear(self, ctx:UnifiedIRParser.YearContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#year.
    def exitYear(self, ctx:UnifiedIRParser.YearContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#entity.
    def enterEntity(self, ctx:UnifiedIRParser.EntityContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#entity.
    def exitEntity(self, ctx:UnifiedIRParser.EntityContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#attribute.
    def enterAttribute(self, ctx:UnifiedIRParser.AttributeContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#attribute.
    def exitAttribute(self, ctx:UnifiedIRParser.AttributeContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#concept.
    def enterConcept(self, ctx:UnifiedIRParser.ConceptContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#concept.
    def exitConcept(self, ctx:UnifiedIRParser.ConceptContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#predicate.
    def enterPredicate(self, ctx:UnifiedIRParser.PredicateContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#predicate.
    def exitPredicate(self, ctx:UnifiedIRParser.PredicateContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#qualifier.
    def enterQualifier(self, ctx:UnifiedIRParser.QualifierContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#qualifier.
    def exitQualifier(self, ctx:UnifiedIRParser.QualifierContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#value.
    def enterValue(self, ctx:UnifiedIRParser.ValueContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#value.
    def exitValue(self, ctx:UnifiedIRParser.ValueContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#number.
    def enterNumber(self, ctx:UnifiedIRParser.NumberContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#number.
    def exitNumber(self, ctx:UnifiedIRParser.NumberContext):
        pass


    # Enter a parse tree produced by UnifiedIRParser#string.
    def enterString(self, ctx:UnifiedIRParser.StringContext):
        pass

    # Exit a parse tree produced by UnifiedIRParser#string.
    def exitString(self, ctx:UnifiedIRParser.StringContext):
        pass



del UnifiedIRParser