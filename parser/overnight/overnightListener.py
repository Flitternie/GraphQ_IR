# Generated from ./overnight.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .overnightParser import overnightParser
else:
    from overnightParser import overnightParser

# This class defines a complete listener for a parse tree produced by overnightParser.
class overnightListener(ParseTreeListener):

    # Enter a parse tree produced by overnightParser#root.
    def enterRoot(self, ctx:overnightParser.RootContext):
        pass

    # Exit a parse tree produced by overnightParser#root.
    def exitRoot(self, ctx:overnightParser.RootContext):
        pass


    # Enter a parse tree produced by overnightParser#np.
    def enterNp(self, ctx:overnightParser.NpContext):
        pass

    # Exit a parse tree produced by overnightParser#np.
    def exitNp(self, ctx:overnightParser.NpContext):
        pass


    # Enter a parse tree produced by overnightParser#entityNP.
    def enterEntityNP(self, ctx:overnightParser.EntityNPContext):
        pass

    # Exit a parse tree produced by overnightParser#entityNP.
    def exitEntityNP(self, ctx:overnightParser.EntityNPContext):
        pass


    # Enter a parse tree produced by overnightParser#eventNP.
    def enterEventNP(self, ctx:overnightParser.EventNPContext):
        pass

    # Exit a parse tree produced by overnightParser#eventNP.
    def exitEventNP(self, ctx:overnightParser.EventNPContext):
        pass


    # Enter a parse tree produced by overnightParser#stringRelNP.
    def enterStringRelNP(self, ctx:overnightParser.StringRelNPContext):
        pass

    # Exit a parse tree produced by overnightParser#stringRelNP.
    def exitStringRelNP(self, ctx:overnightParser.StringRelNPContext):
        pass


    # Enter a parse tree produced by overnightParser#numberRelNP.
    def enterNumberRelNP(self, ctx:overnightParser.NumberRelNPContext):
        pass

    # Exit a parse tree produced by overnightParser#numberRelNP.
    def exitNumberRelNP(self, ctx:overnightParser.NumberRelNPContext):
        pass


    # Enter a parse tree produced by overnightParser#reverseRelNP.
    def enterReverseRelNP(self, ctx:overnightParser.ReverseRelNPContext):
        pass

    # Exit a parse tree produced by overnightParser#reverseRelNP.
    def exitReverseRelNP(self, ctx:overnightParser.ReverseRelNPContext):
        pass


    # Enter a parse tree produced by overnightParser#typeConstraintNP.
    def enterTypeConstraintNP(self, ctx:overnightParser.TypeConstraintNPContext):
        pass

    # Exit a parse tree produced by overnightParser#typeConstraintNP.
    def exitTypeConstraintNP(self, ctx:overnightParser.TypeConstraintNPContext):
        pass


    # Enter a parse tree produced by overnightParser#varConstraintNP.
    def enterVarConstraintNP(self, ctx:overnightParser.VarConstraintNPContext):
        pass

    # Exit a parse tree produced by overnightParser#varConstraintNP.
    def exitVarConstraintNP(self, ctx:overnightParser.VarConstraintNPContext):
        pass


    # Enter a parse tree produced by overnightParser#filterConstraintNP.
    def enterFilterConstraintNP(self, ctx:overnightParser.FilterConstraintNPContext):
        pass

    # Exit a parse tree produced by overnightParser#filterConstraintNP.
    def exitFilterConstraintNP(self, ctx:overnightParser.FilterConstraintNPContext):
        pass


    # Enter a parse tree produced by overnightParser#eventConstraintNP.
    def enterEventConstraintNP(self, ctx:overnightParser.EventConstraintNPContext):
        pass

    # Exit a parse tree produced by overnightParser#eventConstraintNP.
    def exitEventConstraintNP(self, ctx:overnightParser.EventConstraintNPContext):
        pass


    # Enter a parse tree produced by overnightParser#entityType.
    def enterEntityType(self, ctx:overnightParser.EntityTypeContext):
        pass

    # Exit a parse tree produced by overnightParser#entityType.
    def exitEntityType(self, ctx:overnightParser.EntityTypeContext):
        pass


    # Enter a parse tree produced by overnightParser#vp.
    def enterVp(self, ctx:overnightParser.VpContext):
        pass

    # Exit a parse tree produced by overnightParser#vp.
    def exitVp(self, ctx:overnightParser.VpContext):
        pass


    # Enter a parse tree produced by overnightParser#vpnp.
    def enterVpnp(self, ctx:overnightParser.VpnpContext):
        pass

    # Exit a parse tree produced by overnightParser#vpnp.
    def exitVpnp(self, ctx:overnightParser.VpnpContext):
        pass


    # Enter a parse tree produced by overnightParser#valueNP.
    def enterValueNP(self, ctx:overnightParser.ValueNPContext):
        pass

    # Exit a parse tree produced by overnightParser#valueNP.
    def exitValueNP(self, ctx:overnightParser.ValueNPContext):
        pass


    # Enter a parse tree produced by overnightParser#numberNP.
    def enterNumberNP(self, ctx:overnightParser.NumberNPContext):
        pass

    # Exit a parse tree produced by overnightParser#numberNP.
    def exitNumberNP(self, ctx:overnightParser.NumberNPContext):
        pass


    # Enter a parse tree produced by overnightParser#dateNP.
    def enterDateNP(self, ctx:overnightParser.DateNPContext):
        pass

    # Exit a parse tree produced by overnightParser#dateNP.
    def exitDateNP(self, ctx:overnightParser.DateNPContext):
        pass


    # Enter a parse tree produced by overnightParser#timeNP.
    def enterTimeNP(self, ctx:overnightParser.TimeNPContext):
        pass

    # Exit a parse tree produced by overnightParser#timeNP.
    def exitTimeNP(self, ctx:overnightParser.TimeNPContext):
        pass


    # Enter a parse tree produced by overnightParser#cp.
    def enterCp(self, ctx:overnightParser.CpContext):
        pass

    # Exit a parse tree produced by overnightParser#cp.
    def exitCp(self, ctx:overnightParser.CpContext):
        pass


    # Enter a parse tree produced by overnightParser#variable.
    def enterVariable(self, ctx:overnightParser.VariableContext):
        pass

    # Exit a parse tree produced by overnightParser#variable.
    def exitVariable(self, ctx:overnightParser.VariableContext):
        pass


    # Enter a parse tree produced by overnightParser#filterCP.
    def enterFilterCP(self, ctx:overnightParser.FilterCPContext):
        pass

    # Exit a parse tree produced by overnightParser#filterCP.
    def exitFilterCP(self, ctx:overnightParser.FilterCPContext):
        pass


    # Enter a parse tree produced by overnightParser#superlativeCP.
    def enterSuperlativeCP(self, ctx:overnightParser.SuperlativeCPContext):
        pass

    # Exit a parse tree produced by overnightParser#superlativeCP.
    def exitSuperlativeCP(self, ctx:overnightParser.SuperlativeCPContext):
        pass


    # Enter a parse tree produced by overnightParser#comparativeCP.
    def enterComparativeCP(self, ctx:overnightParser.ComparativeCPContext):
        pass

    # Exit a parse tree produced by overnightParser#comparativeCP.
    def exitComparativeCP(self, ctx:overnightParser.ComparativeCPContext):
        pass


    # Enter a parse tree produced by overnightParser#equal.
    def enterEqual(self, ctx:overnightParser.EqualContext):
        pass

    # Exit a parse tree produced by overnightParser#equal.
    def exitEqual(self, ctx:overnightParser.EqualContext):
        pass


    # Enter a parse tree produced by overnightParser#notEqual.
    def enterNotEqual(self, ctx:overnightParser.NotEqualContext):
        pass

    # Exit a parse tree produced by overnightParser#notEqual.
    def exitNotEqual(self, ctx:overnightParser.NotEqualContext):
        pass


    # Enter a parse tree produced by overnightParser#lessThan.
    def enterLessThan(self, ctx:overnightParser.LessThanContext):
        pass

    # Exit a parse tree produced by overnightParser#lessThan.
    def exitLessThan(self, ctx:overnightParser.LessThanContext):
        pass


    # Enter a parse tree produced by overnightParser#greaterThan.
    def enterGreaterThan(self, ctx:overnightParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by overnightParser#greaterThan.
    def exitGreaterThan(self, ctx:overnightParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by overnightParser#lessThanOrEqual.
    def enterLessThanOrEqual(self, ctx:overnightParser.LessThanOrEqualContext):
        pass

    # Exit a parse tree produced by overnightParser#lessThanOrEqual.
    def exitLessThanOrEqual(self, ctx:overnightParser.LessThanOrEqualContext):
        pass


    # Enter a parse tree produced by overnightParser#greaterThanOrEqual.
    def enterGreaterThanOrEqual(self, ctx:overnightParser.GreaterThanOrEqualContext):
        pass

    # Exit a parse tree produced by overnightParser#greaterThanOrEqual.
    def exitGreaterThanOrEqual(self, ctx:overnightParser.GreaterThanOrEqualContext):
        pass


    # Enter a parse tree produced by overnightParser#min.
    def enterMin(self, ctx:overnightParser.MinContext):
        pass

    # Exit a parse tree produced by overnightParser#min.
    def exitMin(self, ctx:overnightParser.MinContext):
        pass


    # Enter a parse tree produced by overnightParser#max.
    def enterMax(self, ctx:overnightParser.MaxContext):
        pass

    # Exit a parse tree produced by overnightParser#max.
    def exitMax(self, ctx:overnightParser.MaxContext):
        pass


    # Enter a parse tree produced by overnightParser#sum.
    def enterSum(self, ctx:overnightParser.SumContext):
        pass

    # Exit a parse tree produced by overnightParser#sum.
    def exitSum(self, ctx:overnightParser.SumContext):
        pass


    # Enter a parse tree produced by overnightParser#avg.
    def enterAvg(self, ctx:overnightParser.AvgContext):
        pass

    # Exit a parse tree produced by overnightParser#avg.
    def exitAvg(self, ctx:overnightParser.AvgContext):
        pass


    # Enter a parse tree produced by overnightParser#listValue.
    def enterListValue(self, ctx:overnightParser.ListValueContext):
        pass

    # Exit a parse tree produced by overnightParser#listValue.
    def exitListValue(self, ctx:overnightParser.ListValueContext):
        pass


    # Enter a parse tree produced by overnightParser#size.
    def enterSize(self, ctx:overnightParser.SizeContext):
        pass

    # Exit a parse tree produced by overnightParser#size.
    def exitSize(self, ctx:overnightParser.SizeContext):
        pass


    # Enter a parse tree produced by overnightParser#domain.
    def enterDomain(self, ctx:overnightParser.DomainContext):
        pass

    # Exit a parse tree produced by overnightParser#domain.
    def exitDomain(self, ctx:overnightParser.DomainContext):
        pass


    # Enter a parse tree produced by overnightParser#singleton.
    def enterSingleton(self, ctx:overnightParser.SingletonContext):
        pass

    # Exit a parse tree produced by overnightParser#singleton.
    def exitSingleton(self, ctx:overnightParser.SingletonContext):
        pass


    # Enter a parse tree produced by overnightParser#filterFunc.
    def enterFilterFunc(self, ctx:overnightParser.FilterFuncContext):
        pass

    # Exit a parse tree produced by overnightParser#filterFunc.
    def exitFilterFunc(self, ctx:overnightParser.FilterFuncContext):
        pass


    # Enter a parse tree produced by overnightParser#getProperty.
    def enterGetProperty(self, ctx:overnightParser.GetPropertyContext):
        pass

    # Exit a parse tree produced by overnightParser#getProperty.
    def exitGetProperty(self, ctx:overnightParser.GetPropertyContext):
        pass


    # Enter a parse tree produced by overnightParser#superlative.
    def enterSuperlative(self, ctx:overnightParser.SuperlativeContext):
        pass

    # Exit a parse tree produced by overnightParser#superlative.
    def exitSuperlative(self, ctx:overnightParser.SuperlativeContext):
        pass


    # Enter a parse tree produced by overnightParser#countSuperlative.
    def enterCountSuperlative(self, ctx:overnightParser.CountSuperlativeContext):
        pass

    # Exit a parse tree produced by overnightParser#countSuperlative.
    def exitCountSuperlative(self, ctx:overnightParser.CountSuperlativeContext):
        pass


    # Enter a parse tree produced by overnightParser#countComparative.
    def enterCountComparative(self, ctx:overnightParser.CountComparativeContext):
        pass

    # Exit a parse tree produced by overnightParser#countComparative.
    def exitCountComparative(self, ctx:overnightParser.CountComparativeContext):
        pass


    # Enter a parse tree produced by overnightParser#aggregate.
    def enterAggregate(self, ctx:overnightParser.AggregateContext):
        pass

    # Exit a parse tree produced by overnightParser#aggregate.
    def exitAggregate(self, ctx:overnightParser.AggregateContext):
        pass


    # Enter a parse tree produced by overnightParser#concat.
    def enterConcat(self, ctx:overnightParser.ConcatContext):
        pass

    # Exit a parse tree produced by overnightParser#concat.
    def exitConcat(self, ctx:overnightParser.ConcatContext):
        pass


    # Enter a parse tree produced by overnightParser#reverse.
    def enterReverse(self, ctx:overnightParser.ReverseContext):
        pass

    # Exit a parse tree produced by overnightParser#reverse.
    def exitReverse(self, ctx:overnightParser.ReverseContext):
        pass


    # Enter a parse tree produced by overnightParser#ensureNumericProperty.
    def enterEnsureNumericProperty(self, ctx:overnightParser.EnsureNumericPropertyContext):
        pass

    # Exit a parse tree produced by overnightParser#ensureNumericProperty.
    def exitEnsureNumericProperty(self, ctx:overnightParser.EnsureNumericPropertyContext):
        pass


    # Enter a parse tree produced by overnightParser#ensureNumericEntity.
    def enterEnsureNumericEntity(self, ctx:overnightParser.EnsureNumericEntityContext):
        pass

    # Exit a parse tree produced by overnightParser#ensureNumericEntity.
    def exitEnsureNumericEntity(self, ctx:overnightParser.EnsureNumericEntityContext):
        pass


    # Enter a parse tree produced by overnightParser#string.
    def enterString(self, ctx:overnightParser.StringContext):
        pass

    # Exit a parse tree produced by overnightParser#string.
    def exitString(self, ctx:overnightParser.StringContext):
        pass


    # Enter a parse tree produced by overnightParser#typeString.
    def enterTypeString(self, ctx:overnightParser.TypeStringContext):
        pass

    # Exit a parse tree produced by overnightParser#typeString.
    def exitTypeString(self, ctx:overnightParser.TypeStringContext):
        pass


    # Enter a parse tree produced by overnightParser#entityString.
    def enterEntityString(self, ctx:overnightParser.EntityStringContext):
        pass

    # Exit a parse tree produced by overnightParser#entityString.
    def exitEntityString(self, ctx:overnightParser.EntityStringContext):
        pass


    # Enter a parse tree produced by overnightParser#date.
    def enterDate(self, ctx:overnightParser.DateContext):
        pass

    # Exit a parse tree produced by overnightParser#date.
    def exitDate(self, ctx:overnightParser.DateContext):
        pass


    # Enter a parse tree produced by overnightParser#time.
    def enterTime(self, ctx:overnightParser.TimeContext):
        pass

    # Exit a parse tree produced by overnightParser#time.
    def exitTime(self, ctx:overnightParser.TimeContext):
        pass


    # Enter a parse tree produced by overnightParser#quantity.
    def enterQuantity(self, ctx:overnightParser.QuantityContext):
        pass

    # Exit a parse tree produced by overnightParser#quantity.
    def exitQuantity(self, ctx:overnightParser.QuantityContext):
        pass



del overnightParser