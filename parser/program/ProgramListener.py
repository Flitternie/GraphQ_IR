# Generated from ./KqaPro_Parser/program/Program.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ProgramParser import ProgramParser
else:
    from ProgramParser import ProgramParser

# This class defines a complete listener for a parse tree produced by ProgramParser.
class ProgramListener(ParseTreeListener):

    # Enter a parse tree produced by ProgramParser#query.
    def enterQuery(self, ctx:ProgramParser.QueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#query.
    def exitQuery(self, ctx:ProgramParser.QueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#whatEntityQuery.
    def enterWhatEntityQuery(self, ctx:ProgramParser.WhatEntityQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#whatEntityQuery.
    def exitWhatEntityQuery(self, ctx:ProgramParser.WhatEntityQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#howManyEntityQuery.
    def enterHowManyEntityQuery(self, ctx:ProgramParser.HowManyEntityQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#howManyEntityQuery.
    def exitHowManyEntityQuery(self, ctx:ProgramParser.HowManyEntityQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#whatAttributeQuery.
    def enterWhatAttributeQuery(self, ctx:ProgramParser.WhatAttributeQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#whatAttributeQuery.
    def exitWhatAttributeQuery(self, ctx:ProgramParser.WhatAttributeQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#whatRelationQuery.
    def enterWhatRelationQuery(self, ctx:ProgramParser.WhatRelationQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#whatRelationQuery.
    def exitWhatRelationQuery(self, ctx:ProgramParser.WhatRelationQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#selectAmongQuery.
    def enterSelectAmongQuery(self, ctx:ProgramParser.SelectAmongQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#selectAmongQuery.
    def exitSelectAmongQuery(self, ctx:ProgramParser.SelectAmongQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#selectBetweenQuery.
    def enterSelectBetweenQuery(self, ctx:ProgramParser.SelectBetweenQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#selectBetweenQuery.
    def exitSelectBetweenQuery(self, ctx:ProgramParser.SelectBetweenQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#attributeSatisfyQuery.
    def enterAttributeSatisfyQuery(self, ctx:ProgramParser.AttributeSatisfyQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#attributeSatisfyQuery.
    def exitAttributeSatisfyQuery(self, ctx:ProgramParser.AttributeSatisfyQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#whatAttributeQualifierQuery.
    def enterWhatAttributeQualifierQuery(self, ctx:ProgramParser.WhatAttributeQualifierQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#whatAttributeQualifierQuery.
    def exitWhatAttributeQualifierQuery(self, ctx:ProgramParser.WhatAttributeQualifierQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#whatRelationQualifierQuery.
    def enterWhatRelationQualifierQuery(self, ctx:ProgramParser.WhatRelationQualifierQueryContext):
        pass

    # Exit a parse tree produced by ProgramParser#whatRelationQualifierQuery.
    def exitWhatRelationQualifierQuery(self, ctx:ProgramParser.WhatRelationQualifierQueryContext):
        pass


    # Enter a parse tree produced by ProgramParser#entitySetGroup.
    def enterEntitySetGroup(self, ctx:ProgramParser.EntitySetGroupContext):
        pass

    # Exit a parse tree produced by ProgramParser#entitySetGroup.
    def exitEntitySetGroup(self, ctx:ProgramParser.EntitySetGroupContext):
        pass


    # Enter a parse tree produced by ProgramParser#entitySetByFilter.
    def enterEntitySetByFilter(self, ctx:ProgramParser.EntitySetByFilterContext):
        pass

    # Exit a parse tree produced by ProgramParser#entitySetByFilter.
    def exitEntitySetByFilter(self, ctx:ProgramParser.EntitySetByFilterContext):
        pass


    # Enter a parse tree produced by ProgramParser#entitySetAtom.
    def enterEntitySetAtom(self, ctx:ProgramParser.EntitySetAtomContext):
        pass

    # Exit a parse tree produced by ProgramParser#entitySetAtom.
    def exitEntitySetAtom(self, ctx:ProgramParser.EntitySetAtomContext):
        pass


    # Enter a parse tree produced by ProgramParser#entitySetByOP.
    def enterEntitySetByOP(self, ctx:ProgramParser.EntitySetByOPContext):
        pass

    # Exit a parse tree produced by ProgramParser#entitySetByOP.
    def exitEntitySetByOP(self, ctx:ProgramParser.EntitySetByOPContext):
        pass


    # Enter a parse tree produced by ProgramParser#entitySetNested.
    def enterEntitySetNested(self, ctx:ProgramParser.EntitySetNestedContext):
        pass

    # Exit a parse tree produced by ProgramParser#entitySetNested.
    def exitEntitySetNested(self, ctx:ProgramParser.EntitySetNestedContext):
        pass


    # Enter a parse tree produced by ProgramParser#entityFilterByRelation.
    def enterEntityFilterByRelation(self, ctx:ProgramParser.EntityFilterByRelationContext):
        pass

    # Exit a parse tree produced by ProgramParser#entityFilterByRelation.
    def exitEntityFilterByRelation(self, ctx:ProgramParser.EntityFilterByRelationContext):
        pass


    # Enter a parse tree produced by ProgramParser#entityFilterByAttribute.
    def enterEntityFilterByAttribute(self, ctx:ProgramParser.EntityFilterByAttributeContext):
        pass

    # Exit a parse tree produced by ProgramParser#entityFilterByAttribute.
    def exitEntityFilterByAttribute(self, ctx:ProgramParser.EntityFilterByAttributeContext):
        pass


    # Enter a parse tree produced by ProgramParser#entityFilterByConcept.
    def enterEntityFilterByConcept(self, ctx:ProgramParser.EntityFilterByConceptContext):
        pass

    # Exit a parse tree produced by ProgramParser#entityFilterByConcept.
    def exitEntityFilterByConcept(self, ctx:ProgramParser.EntityFilterByConceptContext):
        pass


    # Enter a parse tree produced by ProgramParser#queryName.
    def enterQueryName(self, ctx:ProgramParser.QueryNameContext):
        pass

    # Exit a parse tree produced by ProgramParser#queryName.
    def exitQueryName(self, ctx:ProgramParser.QueryNameContext):
        pass


    # Enter a parse tree produced by ProgramParser#count.
    def enterCount(self, ctx:ProgramParser.CountContext):
        pass

    # Exit a parse tree produced by ProgramParser#count.
    def exitCount(self, ctx:ProgramParser.CountContext):
        pass


    # Enter a parse tree produced by ProgramParser#findAll.
    def enterFindAll(self, ctx:ProgramParser.FindAllContext):
        pass

    # Exit a parse tree produced by ProgramParser#findAll.
    def exitFindAll(self, ctx:ProgramParser.FindAllContext):
        pass


    # Enter a parse tree produced by ProgramParser#setOP.
    def enterSetOP(self, ctx:ProgramParser.SetOPContext):
        pass

    # Exit a parse tree produced by ProgramParser#setOP.
    def exitSetOP(self, ctx:ProgramParser.SetOPContext):
        pass


    # Enter a parse tree produced by ProgramParser#and.
    def enterAnd(self, ctx:ProgramParser.AndContext):
        pass

    # Exit a parse tree produced by ProgramParser#and.
    def exitAnd(self, ctx:ProgramParser.AndContext):
        pass


    # Enter a parse tree produced by ProgramParser#or.
    def enterOr(self, ctx:ProgramParser.OrContext):
        pass

    # Exit a parse tree produced by ProgramParser#or.
    def exitOr(self, ctx:ProgramParser.OrContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterAttr.
    def enterFilterAttr(self, ctx:ProgramParser.FilterAttrContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterAttr.
    def exitFilterAttr(self, ctx:ProgramParser.FilterAttrContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterStr.
    def enterFilterStr(self, ctx:ProgramParser.FilterStrContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterStr.
    def exitFilterStr(self, ctx:ProgramParser.FilterStrContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterNum.
    def enterFilterNum(self, ctx:ProgramParser.FilterNumContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterNum.
    def exitFilterNum(self, ctx:ProgramParser.FilterNumContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterYear.
    def enterFilterYear(self, ctx:ProgramParser.FilterYearContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterYear.
    def exitFilterYear(self, ctx:ProgramParser.FilterYearContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterDate.
    def enterFilterDate(self, ctx:ProgramParser.FilterDateContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterDate.
    def exitFilterDate(self, ctx:ProgramParser.FilterDateContext):
        pass


    # Enter a parse tree produced by ProgramParser#queryRelation.
    def enterQueryRelation(self, ctx:ProgramParser.QueryRelationContext):
        pass

    # Exit a parse tree produced by ProgramParser#queryRelation.
    def exitQueryRelation(self, ctx:ProgramParser.QueryRelationContext):
        pass


    # Enter a parse tree produced by ProgramParser#selectAmong.
    def enterSelectAmong(self, ctx:ProgramParser.SelectAmongContext):
        pass

    # Exit a parse tree produced by ProgramParser#selectAmong.
    def exitSelectAmong(self, ctx:ProgramParser.SelectAmongContext):
        pass


    # Enter a parse tree produced by ProgramParser#selectBetween.
    def enterSelectBetween(self, ctx:ProgramParser.SelectBetweenContext):
        pass

    # Exit a parse tree produced by ProgramParser#selectBetween.
    def exitSelectBetween(self, ctx:ProgramParser.SelectBetweenContext):
        pass


    # Enter a parse tree produced by ProgramParser#queryAttributeUnderCondition.
    def enterQueryAttributeUnderCondition(self, ctx:ProgramParser.QueryAttributeUnderConditionContext):
        pass

    # Exit a parse tree produced by ProgramParser#queryAttributeUnderCondition.
    def exitQueryAttributeUnderCondition(self, ctx:ProgramParser.QueryAttributeUnderConditionContext):
        pass


    # Enter a parse tree produced by ProgramParser#queryAttribute.
    def enterQueryAttribute(self, ctx:ProgramParser.QueryAttributeContext):
        pass

    # Exit a parse tree produced by ProgramParser#queryAttribute.
    def exitQueryAttribute(self, ctx:ProgramParser.QueryAttributeContext):
        pass


    # Enter a parse tree produced by ProgramParser#verify.
    def enterVerify(self, ctx:ProgramParser.VerifyContext):
        pass

    # Exit a parse tree produced by ProgramParser#verify.
    def exitVerify(self, ctx:ProgramParser.VerifyContext):
        pass


    # Enter a parse tree produced by ProgramParser#verifyStr.
    def enterVerifyStr(self, ctx:ProgramParser.VerifyStrContext):
        pass

    # Exit a parse tree produced by ProgramParser#verifyStr.
    def exitVerifyStr(self, ctx:ProgramParser.VerifyStrContext):
        pass


    # Enter a parse tree produced by ProgramParser#verifyNum.
    def enterVerifyNum(self, ctx:ProgramParser.VerifyNumContext):
        pass

    # Exit a parse tree produced by ProgramParser#verifyNum.
    def exitVerifyNum(self, ctx:ProgramParser.VerifyNumContext):
        pass


    # Enter a parse tree produced by ProgramParser#verifyYear.
    def enterVerifyYear(self, ctx:ProgramParser.VerifyYearContext):
        pass

    # Exit a parse tree produced by ProgramParser#verifyYear.
    def exitVerifyYear(self, ctx:ProgramParser.VerifyYearContext):
        pass


    # Enter a parse tree produced by ProgramParser#verifyDate.
    def enterVerifyDate(self, ctx:ProgramParser.VerifyDateContext):
        pass

    # Exit a parse tree produced by ProgramParser#verifyDate.
    def exitVerifyDate(self, ctx:ProgramParser.VerifyDateContext):
        pass


    # Enter a parse tree produced by ProgramParser#queryAttrQualifier.
    def enterQueryAttrQualifier(self, ctx:ProgramParser.QueryAttrQualifierContext):
        pass

    # Exit a parse tree produced by ProgramParser#queryAttrQualifier.
    def exitQueryAttrQualifier(self, ctx:ProgramParser.QueryAttrQualifierContext):
        pass


    # Enter a parse tree produced by ProgramParser#queryRelationQualifier.
    def enterQueryRelationQualifier(self, ctx:ProgramParser.QueryRelationQualifierContext):
        pass

    # Exit a parse tree produced by ProgramParser#queryRelationQualifier.
    def exitQueryRelationQualifier(self, ctx:ProgramParser.QueryRelationQualifierContext):
        pass


    # Enter a parse tree produced by ProgramParser#relate.
    def enterRelate(self, ctx:ProgramParser.RelateContext):
        pass

    # Exit a parse tree produced by ProgramParser#relate.
    def exitRelate(self, ctx:ProgramParser.RelateContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterQualifier.
    def enterFilterQualifier(self, ctx:ProgramParser.FilterQualifierContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterQualifier.
    def exitFilterQualifier(self, ctx:ProgramParser.FilterQualifierContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterStrQualifier.
    def enterFilterStrQualifier(self, ctx:ProgramParser.FilterStrQualifierContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterStrQualifier.
    def exitFilterStrQualifier(self, ctx:ProgramParser.FilterStrQualifierContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterNumQualifier.
    def enterFilterNumQualifier(self, ctx:ProgramParser.FilterNumQualifierContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterNumQualifier.
    def exitFilterNumQualifier(self, ctx:ProgramParser.FilterNumQualifierContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterYearQualifier.
    def enterFilterYearQualifier(self, ctx:ProgramParser.FilterYearQualifierContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterYearQualifier.
    def exitFilterYearQualifier(self, ctx:ProgramParser.FilterYearQualifierContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterDateQualifier.
    def enterFilterDateQualifier(self, ctx:ProgramParser.FilterDateQualifierContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterDateQualifier.
    def exitFilterDateQualifier(self, ctx:ProgramParser.FilterDateQualifierContext):
        pass


    # Enter a parse tree produced by ProgramParser#filterConcept.
    def enterFilterConcept(self, ctx:ProgramParser.FilterConceptContext):
        pass

    # Exit a parse tree produced by ProgramParser#filterConcept.
    def exitFilterConcept(self, ctx:ProgramParser.FilterConceptContext):
        pass


    # Enter a parse tree produced by ProgramParser#entity.
    def enterEntity(self, ctx:ProgramParser.EntityContext):
        pass

    # Exit a parse tree produced by ProgramParser#entity.
    def exitEntity(self, ctx:ProgramParser.EntityContext):
        pass


    # Enter a parse tree produced by ProgramParser#concept.
    def enterConcept(self, ctx:ProgramParser.ConceptContext):
        pass

    # Exit a parse tree produced by ProgramParser#concept.
    def exitConcept(self, ctx:ProgramParser.ConceptContext):
        pass


    # Enter a parse tree produced by ProgramParser#predicate.
    def enterPredicate(self, ctx:ProgramParser.PredicateContext):
        pass

    # Exit a parse tree produced by ProgramParser#predicate.
    def exitPredicate(self, ctx:ProgramParser.PredicateContext):
        pass


    # Enter a parse tree produced by ProgramParser#key.
    def enterKey(self, ctx:ProgramParser.KeyContext):
        pass

    # Exit a parse tree produced by ProgramParser#key.
    def exitKey(self, ctx:ProgramParser.KeyContext):
        pass


    # Enter a parse tree produced by ProgramParser#value.
    def enterValue(self, ctx:ProgramParser.ValueContext):
        pass

    # Exit a parse tree produced by ProgramParser#value.
    def exitValue(self, ctx:ProgramParser.ValueContext):
        pass


    # Enter a parse tree produced by ProgramParser#qkey.
    def enterQkey(self, ctx:ProgramParser.QkeyContext):
        pass

    # Exit a parse tree produced by ProgramParser#qkey.
    def exitQkey(self, ctx:ProgramParser.QkeyContext):
        pass


    # Enter a parse tree produced by ProgramParser#qvalue.
    def enterQvalue(self, ctx:ProgramParser.QvalueContext):
        pass

    # Exit a parse tree produced by ProgramParser#qvalue.
    def exitQvalue(self, ctx:ProgramParser.QvalueContext):
        pass


    # Enter a parse tree produced by ProgramParser#op.
    def enterOp(self, ctx:ProgramParser.OpContext):
        pass

    # Exit a parse tree produced by ProgramParser#op.
    def exitOp(self, ctx:ProgramParser.OpContext):
        pass


    # Enter a parse tree produced by ProgramParser#symbolOP.
    def enterSymbolOP(self, ctx:ProgramParser.SymbolOPContext):
        pass

    # Exit a parse tree produced by ProgramParser#symbolOP.
    def exitSymbolOP(self, ctx:ProgramParser.SymbolOPContext):
        pass


    # Enter a parse tree produced by ProgramParser#stringOP.
    def enterStringOP(self, ctx:ProgramParser.StringOPContext):
        pass

    # Exit a parse tree produced by ProgramParser#stringOP.
    def exitStringOP(self, ctx:ProgramParser.StringOPContext):
        pass


    # Enter a parse tree produced by ProgramParser#direction.
    def enterDirection(self, ctx:ProgramParser.DirectionContext):
        pass

    # Exit a parse tree produced by ProgramParser#direction.
    def exitDirection(self, ctx:ProgramParser.DirectionContext):
        pass


    # Enter a parse tree produced by ProgramParser#string.
    def enterString(self, ctx:ProgramParser.StringContext):
        pass

    # Exit a parse tree produced by ProgramParser#string.
    def exitString(self, ctx:ProgramParser.StringContext):
        pass


    # Enter a parse tree produced by ProgramParser#date.
    def enterDate(self, ctx:ProgramParser.DateContext):
        pass

    # Exit a parse tree produced by ProgramParser#date.
    def exitDate(self, ctx:ProgramParser.DateContext):
        pass


    # Enter a parse tree produced by ProgramParser#year.
    def enterYear(self, ctx:ProgramParser.YearContext):
        pass

    # Exit a parse tree produced by ProgramParser#year.
    def exitYear(self, ctx:ProgramParser.YearContext):
        pass


    # Enter a parse tree produced by ProgramParser#number.
    def enterNumber(self, ctx:ProgramParser.NumberContext):
        pass

    # Exit a parse tree produced by ProgramParser#number.
    def exitNumber(self, ctx:ProgramParser.NumberContext):
        pass



del ProgramParser