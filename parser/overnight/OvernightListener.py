# Generated from ./parser/overnight/Overnight.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OvernightParser import OvernightParser
else:
    from OvernightParser import OvernightParser

# This class defines a complete listener for a parse tree produced by OvernightParser.
class OvernightListener(ParseTreeListener):

    # Enter a parse tree produced by OvernightParser#root.
    def enterRoot(self, ctx:OvernightParser.RootContext):
        pass

    # Exit a parse tree produced by OvernightParser#root.
    def exitRoot(self, ctx:OvernightParser.RootContext):
        pass


    # Enter a parse tree produced by OvernightParser#CPNP.
    def enterCPNP(self, ctx:OvernightParser.CPNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#CPNP.
    def exitCPNP(self, ctx:OvernightParser.CPNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#entityNP.
    def enterEntityNP(self, ctx:OvernightParser.EntityNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#entityNP.
    def exitEntityNP(self, ctx:OvernightParser.EntityNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#getPropertyNP.
    def enterGetPropertyNP(self, ctx:OvernightParser.GetPropertyNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#getPropertyNP.
    def exitGetPropertyNP(self, ctx:OvernightParser.GetPropertyNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#numericNP.
    def enterNumericNP(self, ctx:OvernightParser.NumericNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#numericNP.
    def exitNumericNP(self, ctx:OvernightParser.NumericNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#concatNP.
    def enterConcatNP(self, ctx:OvernightParser.ConcatNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#concatNP.
    def exitConcatNP(self, ctx:OvernightParser.ConcatNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#aggregateNP.
    def enterAggregateNP(self, ctx:OvernightParser.AggregateNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#aggregateNP.
    def exitAggregateNP(self, ctx:OvernightParser.AggregateNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#sizeNP.
    def enterSizeNP(self, ctx:OvernightParser.SizeNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#sizeNP.
    def exitSizeNP(self, ctx:OvernightParser.SizeNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#domainCPNP.
    def enterDomainCPNP(self, ctx:OvernightParser.DomainCPNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#domainCPNP.
    def exitDomainCPNP(self, ctx:OvernightParser.DomainCPNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#filterNP.
    def enterFilterNP(self, ctx:OvernightParser.FilterNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#filterNP.
    def exitFilterNP(self, ctx:OvernightParser.FilterNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#entity.
    def enterEntity(self, ctx:OvernightParser.EntityContext):
        pass

    # Exit a parse tree produced by OvernightParser#entity.
    def exitEntity(self, ctx:OvernightParser.EntityContext):
        pass


    # Enter a parse tree produced by OvernightParser#concept.
    def enterConcept(self, ctx:OvernightParser.ConceptContext):
        pass

    # Exit a parse tree produced by OvernightParser#concept.
    def exitConcept(self, ctx:OvernightParser.ConceptContext):
        pass


    # Enter a parse tree produced by OvernightParser#predicate.
    def enterPredicate(self, ctx:OvernightParser.PredicateContext):
        pass

    # Exit a parse tree produced by OvernightParser#predicate.
    def exitPredicate(self, ctx:OvernightParser.PredicateContext):
        pass


    # Enter a parse tree produced by OvernightParser#stringRelNP.
    def enterStringRelNP(self, ctx:OvernightParser.StringRelNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#stringRelNP.
    def exitStringRelNP(self, ctx:OvernightParser.StringRelNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#numberRelNP.
    def enterNumberRelNP(self, ctx:OvernightParser.NumberRelNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#numberRelNP.
    def exitNumberRelNP(self, ctx:OvernightParser.NumberRelNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#reversePredicate.
    def enterReversePredicate(self, ctx:OvernightParser.ReversePredicateContext):
        pass

    # Exit a parse tree produced by OvernightParser#reversePredicate.
    def exitReversePredicate(self, ctx:OvernightParser.ReversePredicateContext):
        pass


    # Enter a parse tree produced by OvernightParser#concatValueNP.
    def enterConcatValueNP(self, ctx:OvernightParser.ConcatValueNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#concatValueNP.
    def exitConcatValueNP(self, ctx:OvernightParser.ConcatValueNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#attributeNP.
    def enterAttributeNP(self, ctx:OvernightParser.AttributeNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#attributeNP.
    def exitAttributeNP(self, ctx:OvernightParser.AttributeNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#numericEntityNP.
    def enterNumericEntityNP(self, ctx:OvernightParser.NumericEntityNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#numericEntityNP.
    def exitNumericEntityNP(self, ctx:OvernightParser.NumericEntityNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#numberNP.
    def enterNumberNP(self, ctx:OvernightParser.NumberNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#numberNP.
    def exitNumberNP(self, ctx:OvernightParser.NumberNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#dateNP.
    def enterDateNP(self, ctx:OvernightParser.DateNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#dateNP.
    def exitDateNP(self, ctx:OvernightParser.DateNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#timeNP.
    def enterTimeNP(self, ctx:OvernightParser.TimeNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#timeNP.
    def exitTimeNP(self, ctx:OvernightParser.TimeNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#typeConstraintNP.
    def enterTypeConstraintNP(self, ctx:OvernightParser.TypeConstraintNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#typeConstraintNP.
    def exitTypeConstraintNP(self, ctx:OvernightParser.TypeConstraintNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#filterConstraintNP.
    def enterFilterConstraintNP(self, ctx:OvernightParser.FilterConstraintNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#filterConstraintNP.
    def exitFilterConstraintNP(self, ctx:OvernightParser.FilterConstraintNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#eventConstraintNP.
    def enterEventConstraintNP(self, ctx:OvernightParser.EventConstraintNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#eventConstraintNP.
    def exitEventConstraintNP(self, ctx:OvernightParser.EventConstraintNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#voidConstraintNP.
    def enterVoidConstraintNP(self, ctx:OvernightParser.VoidConstraintNPContext):
        pass

    # Exit a parse tree produced by OvernightParser#voidConstraintNP.
    def exitVoidConstraintNP(self, ctx:OvernightParser.VoidConstraintNPContext):
        pass


    # Enter a parse tree produced by OvernightParser#nestedCP.
    def enterNestedCP(self, ctx:OvernightParser.NestedCPContext):
        pass

    # Exit a parse tree produced by OvernightParser#nestedCP.
    def exitNestedCP(self, ctx:OvernightParser.NestedCPContext):
        pass


    # Enter a parse tree produced by OvernightParser#CP.
    def enterCP(self, ctx:OvernightParser.CPContext):
        pass

    # Exit a parse tree produced by OvernightParser#CP.
    def exitCP(self, ctx:OvernightParser.CPContext):
        pass


    # Enter a parse tree produced by OvernightParser#filterByPredicate.
    def enterFilterByPredicate(self, ctx:OvernightParser.FilterByPredicateContext):
        pass

    # Exit a parse tree produced by OvernightParser#filterByPredicate.
    def exitFilterByPredicate(self, ctx:OvernightParser.FilterByPredicateContext):
        pass


    # Enter a parse tree produced by OvernightParser#filterByAttribute.
    def enterFilterByAttribute(self, ctx:OvernightParser.FilterByAttributeContext):
        pass

    # Exit a parse tree produced by OvernightParser#filterByAttribute.
    def exitFilterByAttribute(self, ctx:OvernightParser.FilterByAttributeContext):
        pass


    # Enter a parse tree produced by OvernightParser#filterByReversePredicate.
    def enterFilterByReversePredicate(self, ctx:OvernightParser.FilterByReversePredicateContext):
        pass

    # Exit a parse tree produced by OvernightParser#filterByReversePredicate.
    def exitFilterByReversePredicate(self, ctx:OvernightParser.FilterByReversePredicateContext):
        pass


    # Enter a parse tree produced by OvernightParser#superlativeByAttribute.
    def enterSuperlativeByAttribute(self, ctx:OvernightParser.SuperlativeByAttributeContext):
        pass

    # Exit a parse tree produced by OvernightParser#superlativeByAttribute.
    def exitSuperlativeByAttribute(self, ctx:OvernightParser.SuperlativeByAttributeContext):
        pass


    # Enter a parse tree produced by OvernightParser#superlativeByPredicate.
    def enterSuperlativeByPredicate(self, ctx:OvernightParser.SuperlativeByPredicateContext):
        pass

    # Exit a parse tree produced by OvernightParser#superlativeByPredicate.
    def exitSuperlativeByPredicate(self, ctx:OvernightParser.SuperlativeByPredicateContext):
        pass


    # Enter a parse tree produced by OvernightParser#superlativeByReversePredicate.
    def enterSuperlativeByReversePredicate(self, ctx:OvernightParser.SuperlativeByReversePredicateContext):
        pass

    # Exit a parse tree produced by OvernightParser#superlativeByReversePredicate.
    def exitSuperlativeByReversePredicate(self, ctx:OvernightParser.SuperlativeByReversePredicateContext):
        pass


    # Enter a parse tree produced by OvernightParser#comparativeByPredicate.
    def enterComparativeByPredicate(self, ctx:OvernightParser.ComparativeByPredicateContext):
        pass

    # Exit a parse tree produced by OvernightParser#comparativeByPredicate.
    def exitComparativeByPredicate(self, ctx:OvernightParser.ComparativeByPredicateContext):
        pass


    # Enter a parse tree produced by OvernightParser#comparativeByReversePredicate.
    def enterComparativeByReversePredicate(self, ctx:OvernightParser.ComparativeByReversePredicateContext):
        pass

    # Exit a parse tree produced by OvernightParser#comparativeByReversePredicate.
    def exitComparativeByReversePredicate(self, ctx:OvernightParser.ComparativeByReversePredicateContext):
        pass


    # Enter a parse tree produced by OvernightParser#equal.
    def enterEqual(self, ctx:OvernightParser.EqualContext):
        pass

    # Exit a parse tree produced by OvernightParser#equal.
    def exitEqual(self, ctx:OvernightParser.EqualContext):
        pass


    # Enter a parse tree produced by OvernightParser#notEqual.
    def enterNotEqual(self, ctx:OvernightParser.NotEqualContext):
        pass

    # Exit a parse tree produced by OvernightParser#notEqual.
    def exitNotEqual(self, ctx:OvernightParser.NotEqualContext):
        pass


    # Enter a parse tree produced by OvernightParser#lessThan.
    def enterLessThan(self, ctx:OvernightParser.LessThanContext):
        pass

    # Exit a parse tree produced by OvernightParser#lessThan.
    def exitLessThan(self, ctx:OvernightParser.LessThanContext):
        pass


    # Enter a parse tree produced by OvernightParser#greaterThan.
    def enterGreaterThan(self, ctx:OvernightParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by OvernightParser#greaterThan.
    def exitGreaterThan(self, ctx:OvernightParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by OvernightParser#lessThanOrEqual.
    def enterLessThanOrEqual(self, ctx:OvernightParser.LessThanOrEqualContext):
        pass

    # Exit a parse tree produced by OvernightParser#lessThanOrEqual.
    def exitLessThanOrEqual(self, ctx:OvernightParser.LessThanOrEqualContext):
        pass


    # Enter a parse tree produced by OvernightParser#greaterThanOrEqual.
    def enterGreaterThanOrEqual(self, ctx:OvernightParser.GreaterThanOrEqualContext):
        pass

    # Exit a parse tree produced by OvernightParser#greaterThanOrEqual.
    def exitGreaterThanOrEqual(self, ctx:OvernightParser.GreaterThanOrEqualContext):
        pass


    # Enter a parse tree produced by OvernightParser#min.
    def enterMin(self, ctx:OvernightParser.MinContext):
        pass

    # Exit a parse tree produced by OvernightParser#min.
    def exitMin(self, ctx:OvernightParser.MinContext):
        pass


    # Enter a parse tree produced by OvernightParser#max.
    def enterMax(self, ctx:OvernightParser.MaxContext):
        pass

    # Exit a parse tree produced by OvernightParser#max.
    def exitMax(self, ctx:OvernightParser.MaxContext):
        pass


    # Enter a parse tree produced by OvernightParser#sumAggregate.
    def enterSumAggregate(self, ctx:OvernightParser.SumAggregateContext):
        pass

    # Exit a parse tree produced by OvernightParser#sumAggregate.
    def exitSumAggregate(self, ctx:OvernightParser.SumAggregateContext):
        pass


    # Enter a parse tree produced by OvernightParser#avgAggregate.
    def enterAvgAggregate(self, ctx:OvernightParser.AvgAggregateContext):
        pass

    # Exit a parse tree produced by OvernightParser#avgAggregate.
    def exitAvgAggregate(self, ctx:OvernightParser.AvgAggregateContext):
        pass


    # Enter a parse tree produced by OvernightParser#listValue.
    def enterListValue(self, ctx:OvernightParser.ListValueContext):
        pass

    # Exit a parse tree produced by OvernightParser#listValue.
    def exitListValue(self, ctx:OvernightParser.ListValueContext):
        pass


    # Enter a parse tree produced by OvernightParser#size.
    def enterSize(self, ctx:OvernightParser.SizeContext):
        pass

    # Exit a parse tree produced by OvernightParser#size.
    def exitSize(self, ctx:OvernightParser.SizeContext):
        pass


    # Enter a parse tree produced by OvernightParser#domain.
    def enterDomain(self, ctx:OvernightParser.DomainContext):
        pass

    # Exit a parse tree produced by OvernightParser#domain.
    def exitDomain(self, ctx:OvernightParser.DomainContext):
        pass


    # Enter a parse tree produced by OvernightParser#singleton.
    def enterSingleton(self, ctx:OvernightParser.SingletonContext):
        pass

    # Exit a parse tree produced by OvernightParser#singleton.
    def exitSingleton(self, ctx:OvernightParser.SingletonContext):
        pass


    # Enter a parse tree produced by OvernightParser#filterFunc.
    def enterFilterFunc(self, ctx:OvernightParser.FilterFuncContext):
        pass

    # Exit a parse tree produced by OvernightParser#filterFunc.
    def exitFilterFunc(self, ctx:OvernightParser.FilterFuncContext):
        pass


    # Enter a parse tree produced by OvernightParser#getProperty.
    def enterGetProperty(self, ctx:OvernightParser.GetPropertyContext):
        pass

    # Exit a parse tree produced by OvernightParser#getProperty.
    def exitGetProperty(self, ctx:OvernightParser.GetPropertyContext):
        pass


    # Enter a parse tree produced by OvernightParser#superlative.
    def enterSuperlative(self, ctx:OvernightParser.SuperlativeContext):
        pass

    # Exit a parse tree produced by OvernightParser#superlative.
    def exitSuperlative(self, ctx:OvernightParser.SuperlativeContext):
        pass


    # Enter a parse tree produced by OvernightParser#countSuperlative.
    def enterCountSuperlative(self, ctx:OvernightParser.CountSuperlativeContext):
        pass

    # Exit a parse tree produced by OvernightParser#countSuperlative.
    def exitCountSuperlative(self, ctx:OvernightParser.CountSuperlativeContext):
        pass


    # Enter a parse tree produced by OvernightParser#countComparative.
    def enterCountComparative(self, ctx:OvernightParser.CountComparativeContext):
        pass

    # Exit a parse tree produced by OvernightParser#countComparative.
    def exitCountComparative(self, ctx:OvernightParser.CountComparativeContext):
        pass


    # Enter a parse tree produced by OvernightParser#aggregate.
    def enterAggregate(self, ctx:OvernightParser.AggregateContext):
        pass

    # Exit a parse tree produced by OvernightParser#aggregate.
    def exitAggregate(self, ctx:OvernightParser.AggregateContext):
        pass


    # Enter a parse tree produced by OvernightParser#concat.
    def enterConcat(self, ctx:OvernightParser.ConcatContext):
        pass

    # Exit a parse tree produced by OvernightParser#concat.
    def exitConcat(self, ctx:OvernightParser.ConcatContext):
        pass


    # Enter a parse tree produced by OvernightParser#reverse.
    def enterReverse(self, ctx:OvernightParser.ReverseContext):
        pass

    # Exit a parse tree produced by OvernightParser#reverse.
    def exitReverse(self, ctx:OvernightParser.ReverseContext):
        pass


    # Enter a parse tree produced by OvernightParser#ensureNumericProperty.
    def enterEnsureNumericProperty(self, ctx:OvernightParser.EnsureNumericPropertyContext):
        pass

    # Exit a parse tree produced by OvernightParser#ensureNumericProperty.
    def exitEnsureNumericProperty(self, ctx:OvernightParser.EnsureNumericPropertyContext):
        pass


    # Enter a parse tree produced by OvernightParser#ensureNumericEntity.
    def enterEnsureNumericEntity(self, ctx:OvernightParser.EnsureNumericEntityContext):
        pass

    # Exit a parse tree produced by OvernightParser#ensureNumericEntity.
    def exitEnsureNumericEntity(self, ctx:OvernightParser.EnsureNumericEntityContext):
        pass


    # Enter a parse tree produced by OvernightParser#string.
    def enterString(self, ctx:OvernightParser.StringContext):
        pass

    # Exit a parse tree produced by OvernightParser#string.
    def exitString(self, ctx:OvernightParser.StringContext):
        pass


    # Enter a parse tree produced by OvernightParser#date.
    def enterDate(self, ctx:OvernightParser.DateContext):
        pass

    # Exit a parse tree produced by OvernightParser#date.
    def exitDate(self, ctx:OvernightParser.DateContext):
        pass


    # Enter a parse tree produced by OvernightParser#time.
    def enterTime(self, ctx:OvernightParser.TimeContext):
        pass

    # Exit a parse tree produced by OvernightParser#time.
    def exitTime(self, ctx:OvernightParser.TimeContext):
        pass


    # Enter a parse tree produced by OvernightParser#quantity.
    def enterQuantity(self, ctx:OvernightParser.QuantityContext):
        pass

    # Exit a parse tree produced by OvernightParser#quantity.
    def exitQuantity(self, ctx:OvernightParser.QuantityContext):
        pass



del OvernightParser