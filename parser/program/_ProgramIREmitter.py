from os import set_inheritable
import os
import sys
import json
from itertools import chain
from tqdm import tqdm
import argparse

from collections import OrderedDict
from string import Template

from antlr4 import *
from antlr4.InputStream import InputStream

from .ProgramLexer import ProgramLexer
from .ProgramParser import ProgramParser
from .ProgramListener import ProgramListener

from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

class IREmitter(ProgramListener):
    def __init__(self):
        self.ir = ""
        self.setOP_vocab = {"and": "and",
                            "or": "or" }
        self.symbolOP_vocab = { "=": "is", 
                                "<": "larger than", 
                                ">": "smaller than", 
                                "!=": "is not" }
        self.stringOP_vocab = { "largest": "largest", 
                                "smallest": "smallest", 
                                "greater": "larger", 
                                "less": "smaller"}
    
    def getIR(self, ctx):
        return self.ir
    
    def insertParentEntitySet(self, ctx, value):
        if isinstance(ctx.slots["entitySet"], list):
            ctx.slots["entitySet"].append(value)
        else: 
            ctx.slots["entitySet"] = value



    def enterQuery(self, ctx: ProgramParser.QueryContext):
        self.ir = ""
        ctx.slots = {"query": ""}
        return super().enterQuery(ctx)
    
    def exitQuery(self, ctx: ProgramParser.QueryContext):
        self.ir = ctx.slots["query"]
        return super().exitQuery(ctx)



    def enterWhatEntityQuery(self, ctx: ProgramParser.WhatEntityQueryContext):
        ctx.slots = {"entitySet": ""}
        return super().enterWhatEntityQuery(ctx)
    
    def exitWhatEntityQuery(self, ctx: ProgramParser.WhatEntityQueryContext):
        ctx.parentCtx.slots["query"] = "what is entity <E> {} </E>".format(ctx.slots["entitySet"])
        return super().exitWhatEntityQuery(ctx)
    
    def enterHowManyEntityQuery(self, ctx: ProgramParser.HowManyEntityQueryContext):
        ctx.slots = {"entitySet": ""}
        return super().enterHowManyEntityQuery(ctx)
    
    def exitHowManyEntityQuery(self, ctx: ProgramParser.HowManyEntityQueryContext):
        ctx.parentCtx.slots["query"] = "how many entity <E> {} </E>".format(ctx.slots["entitySet"])
        return super().exitHowManyEntityQuery(ctx)

    def enterWhatAttributeQuery(self, ctx: ProgramParser.WhatAttributeQueryContext):
        ctx.slots = {"entitySet": "", "attribute": ""}
        return super().enterWhatAttributeQuery(ctx)

    def exitWhatAttributeQuery(self, ctx: ProgramParser.WhatAttributeQueryContext):
        ctx.parentCtx.slots["query"] = "for entity <E> {} </E>, what is attribute <A> {} </A>".format(ctx.slots["entitySet"], ctx.slots["attribute"])
        return super().exitWhatAttributeQuery(ctx)
    
    def enterWhatRelationQuery(self, ctx: ProgramParser.WhatRelationQueryContext):
        ctx.slots = {"entitySetGroup": []}
        return super().enterWhatRelationQuery(ctx)
    
    def exitWhatRelationQuery(self, ctx: ProgramParser.WhatRelationQueryContext):
        ctx.parentCtx.slots["query"] = "what is the relation from entity <E> {} </E> to entity <E> {} </E>".format(ctx.slots["entitySetGroup"][0], ctx.slots["entitySetGroup"][1])
        return super().exitWhatRelationQuery(ctx)

    # def enterSelectAmongQuery(self, ctx: ProgramParser.SelectAmongQueryContext):
    #     ctx.slots = {"entitySet": "", "attribute": "", "selectOP": ""}
    #     return super().enterSelectAmongQuery(ctx)
    
    # def exitSelectAmongQuery(self, ctx: ProgramParser.SelectAmongQueryContext):
    #     ctx.parentCtx.slots["query"] = "among entity <E> {} </E>, which one has the {} attribute <A> {} </A> ".format(ctx.slots["entitySet"], ctx.slots["selectOP"], ctx.slots["attribute"])
    #     return super().exitSelectAmongQuery(ctx)
    
    # def enterSelectBetweenQuery(self, ctx: ProgramParser.SelectBetweenQueryContext):
    #     ctx.slots = {"entitySetGroup": [], "attribute": "", "selectOP": ""}
    #     return super().enterSelectBetweenQuery(ctx)
    
    # def exitSelectBetweenQuery(self, ctx: ProgramParser.SelectBetweenQueryContext):
    #     ctx.parentCtx.slots["query"] = "which one has the {} attribute <A> {} </A>, entity <E> {} </E> or entity <E> {} </E>".format(ctx.slots["selectOP"], ctx.slots["attribute"], ctx.slots["entitySetGroup"][0], ctx.slots["entitySetGroup"][1])
    #     return super().exitSelectBetweenQuery(ctx)  
    
    def enterAttributeSatisfyQuery(self, ctx: ProgramParser.AttributeSatisfyQueryContext):
        ctx.slots = {"entitySet": "", "attribute": "", "verify": "", "qualifier": ""}
        return super().enterAttributeSatisfyQuery(ctx)
    
    def exitAttributeSatisfyQuery(self, ctx: ProgramParser.AttributeSatisfyQueryContext):
        ctx.parentCtx.slots["query"] = "for entity <E> {} </E>, whether attribute <A> {} </A> {}{}".format(ctx.slots["entitySet"], ctx.slots["attribute"], ctx.slots["verify"], ctx.slots["qualifier"])
        return super().exitAttributeSatisfyQuery(ctx)

    def enterWhatAttributeQualifierQuery(self, ctx: ProgramParser.WhatAttributeQualifierQueryContext):
        ctx.slots = {"entitySet": "", "attribute": "", "value": "", "qualifier": ""}
        return super().enterWhatAttributeQualifierQuery(ctx)

    def exitWhatAttributeQualifierQuery(self, ctx: ProgramParser.WhatAttributeQualifierQueryContext):
        ctx.parentCtx.slots["query"] = "for entity <E> {} </E> whose attribute <A> {} </A> is value <V> {} </V>, what is the qualifier <Q> {} </Q>".format(ctx.slots["entitySet"], ctx.slots["attribute"], ctx.slots["value"], ctx.slots["qualifier"])
        return super().exitWhatAttributeQualifierQuery(ctx)
    
    def enterQueryAttrQualifier(self, ctx: ProgramParser.QueryAttrQualifierContext):
        ctx.slots = {"key": "", "value": "", "qkey": ""}
        return super().enterQueryAttrQualifier(ctx)
    
    def exitQueryAttrQualifier(self, ctx: ProgramParser.QueryAttrQualifierContext):
        ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        ctx.parentCtx.slots["qualifier"] = ctx.slots["qkey"]
        return super().exitQueryAttrQualifier(ctx)


    def enterWhatRelationQualifierQuery(self, ctx: ProgramParser.WhatRelationQualifierQueryContext):
        ctx.slots = {"entitySetGroup": [], "predicate": "", "qualifier": ""}
        return super().enterWhatRelationQualifierQuery(ctx)
    
    def exitWhatRelationQualifierQuery(self, ctx: ProgramParser.WhatRelationQualifierQueryContext):
        ctx.parentCtx.slots["query"] = "entity <E> {} </E> that relation <R> {} </R> to entity <E> {} </E>, what is the qualifier <Q> {} </Q> ".format(ctx.slots["entitySetGroup"][0], ctx.slots["predicate"], ctx.slots["entitySetGroup"][1], ctx.slots["qualifier"])
        return super().exitWhatRelationQualifierQuery(ctx)

    def enterQueryRelationQualifier(self, ctx: ProgramParser.QueryRelationQualifierContext):
        ctx.slots = {"predicate": "", "qkey": ""}
        return super().enterQueryRelationQualifier(ctx)
    
    def exitQueryRelationQualifier(self, ctx: ProgramParser.QueryRelationQualifierContext):
        ctx.parentCtx.slots["predicate"] = ctx.slots["predicate"]
        ctx.parentCtx.slots["qualifier"] = ctx.slots["qkey"]
        return super().exitQueryRelationQualifier(ctx)
 

    def enterEntitySetGroup(self, ctx: ProgramParser.EntitySetGroupContext):
        ctx.slots = {"entitySet": []}
        return super().enterEntitySetGroup(ctx)
    
    def exitEntitySetGroup(self, ctx: ProgramParser.EntitySetGroupContext):
        assert len(ctx.slots["entitySet"]) == 2
        ctx.parentCtx.slots["entitySetGroup"] = ctx.slots["entitySet"]
        return super().exitEntitySetGroup(ctx)

    def enterEntitySetByOP(self, ctx: ProgramParser.EntitySetByOPContext):
        ctx.slots = {"entitySet": [], "setOP": ""}
        return super().enterEntitySetByOP(ctx)
    
    def exitEntitySetByOP(self, ctx: ProgramParser.EntitySetByOPContext):
        assert len(ctx.slots["entitySet"]) == 2
        self.insertParentEntitySet(ctx.parentCtx, "entity <E> {} </E> {} entity <E> {} </E>".format(ctx.slots["entitySet"][0], ctx.slots["setOP"], ctx.slots["entitySet"][1]))
        return super().exitEntitySetByOP(ctx)
    
    def enterEntitySetByRank(self, ctx: ProgramParser.EntitySetByRankContext):
        ctx.slots = {"entitySet": "", "attributeRankFilter": ""}
        return super().enterEntitySetByRank(ctx)
    
    def exitEntitySetByRank(self, ctx: ProgramParser.EntitySetByRankContext):
        self.insertParentEntitySet(ctx.parentCtx, "{} among entity <E> {} </E>".format(ctx.slots["attributeRankFilter"], ctx.slots["entitySet"]))
        return super().exitEntitySetByRank(ctx)
    
    def enterEntitySetNested(self, ctx: ProgramParser.EntitySetNestedContext):
        ctx.slots = {"entitySet": "", "relationFilter": "", "attributeFilter": "", "conceptFilter": "", "qualifierFilter": ""}
        return super().enterEntitySetNested(ctx)
    
    def exitEntitySetNested(self, ctx: ProgramParser.EntitySetNestedContext):
        if ctx.slots["relationFilter"]:
            if ctx.slots["conceptFilter"]:
                self.insertParentEntitySet(ctx.parentCtx, "the {} {} entity <E> {} </E> {}".format(ctx.slots["conceptFilter"], ctx.slots["relationFilter"], ctx.slots["entitySet"], ctx.slots["qualifierFilter"]))
            else:
                self.insertParentEntitySet(ctx.parentCtx, "the one {} entity <E> {} </E> {}".format(ctx.slots["relationFilter"], ctx.slots["entitySet"], ctx.slots["qualifierFilter"]))
        elif ctx.slots["attributeFilter"]:
            self.insertParentEntitySet(ctx.parentCtx, "{}entity <E> {} </E> {}{}".format(ctx.slots["conceptFilter"], ctx.slots["entitySet"], ctx.slots["attributeFilter"], ctx.slots["qualifierFilter"]))
        return super().exitEntitySetNested(ctx)
    
    def enterEntitySetByFilter(self, ctx: ProgramParser.EntitySetByFilterContext):
        ctx.slots = {"attributeFilter": "", "conceptFilter": "", "qualifierFilter": ""}
        return super().enterEntitySetByFilter(ctx)
    
    def exitEntitySetByFilter(self, ctx: ProgramParser.EntitySetByFilterContext):
        self.insertParentEntitySet(ctx.parentCtx, "{}{}{}".format(ctx.slots["conceptFilter"], ctx.slots["attributeFilter"], ctx.slots["qualifierFilter"]))
        return super().exitEntitySetByFilter(ctx)

    def enterEntitySetAtom(self, ctx: ProgramParser.EntitySetAtomContext):
        ctx.slots = {"entity": ""}
        return super().enterEntitySetAtom(ctx)
    
    def exitEntitySetAtom(self, ctx: ProgramParser.EntitySetAtomContext):
        self.insertParentEntitySet(ctx.parentCtx, ctx.slots["entity"])
        return super().exitEntitySetAtom(ctx)

    def enterEntityFilterByRelation(self, ctx: ProgramParser.EntityFilterByRelationContext):
        ctx.slots = {"predicate": "", "direction": "", "qualifier": "", "concept": ""}
        return super().enterEntityFilterByRelation(ctx)
    
    def exitEntityFilterByRelation(self, ctx: ProgramParser.EntityFilterByRelationContext):
        ctx.parentCtx.slots["relationFilter"] = "that relation <R> {} </R> {} to".format(ctx.slots["predicate"], ctx.slots["direction"])
        if ctx.slots["qualifier"]:
            ctx.parentCtx.slots["qualifierFilter"] = ctx.slots["qualifier"]
        if ctx.slots["concept"]:
            ctx.parentCtx.slots["conceptFilter"] = "concept <C> {} </C> ".format(ctx.slots["concept"])
        return super().exitEntityFilterByRelation(ctx)
    
    def enterEntityFilterByAttribute(self, ctx: ProgramParser.EntityFilterByAttributeContext):
        ctx.slots = {"attribute": "", "qualifier": "", "concept": ""}
        return super().enterEntityFilterByAttribute(ctx)
    
    def exitEntityFilterByAttribute(self, ctx: ProgramParser.EntityFilterByAttributeContext):
        ctx.parentCtx.slots["attributeFilter"] = "whose {}".format(ctx.slots["attribute"])
        if ctx.slots["qualifier"]:
            ctx.parentCtx.slots["qualifierFilter"] = ctx.slots["qualifier"]
        if ctx.slots["concept"]:
            ctx.parentCtx.slots["conceptFilter"] = "concept <C> {} </C> ".format(ctx.slots["concept"])
        return super().exitEntityFilterByAttribute(ctx)   

    def enterEntityFilterByConcept(self, ctx: ProgramParser.EntityFilterByConceptContext):
        ctx.slots = {"concept": ""}
        return super().enterEntityFilterByConcept(ctx)
    
    def exitEntityFilterByConcept(self, ctx: ProgramParser.EntityFilterByConceptContext):
        ctx.parentCtx.slots["conceptFilter"] = "concept <C> {} </C> ".format(ctx.slots["concept"])
        return super().exitEntityFilterByConcept(ctx)



    def enterFilterConcept(self, ctx: ProgramParser.FilterConceptContext):
        ctx.slots = {"concept": ""}
        return super().enterFilterConcept(ctx)

    def exitFilterConcept(self, ctx: ProgramParser.FilterConceptContext):
        ctx.parentCtx.slots["concept"] = ctx.slots["concept"]
        return super().exitFilterConcept(ctx)
    
    def enterRelate(self, ctx: ProgramParser.RelateContext):
        ctx.slots = {"predicate": "", "direction": ""}
        return super().enterRelate(ctx)
    
    def exitRelate(self, ctx: ProgramParser.RelateContext):
        ctx.parentCtx.slots["predicate"] = ctx.slots["predicate"]
        ctx.parentCtx.slots["direction"] = ctx.slots["direction"]
        return super().exitRelate(ctx)

    def enterFilterAttr(self, ctx: ProgramParser.FilterAttrContext):
        ctx.slots = {"attribute": "", "value": "", "value_type": "", "OP": ""}
        return super().enterFilterAttr(ctx)
    
    def exitFilterAttr(self, ctx: ProgramParser.FilterAttrContext):
        ctx.parentCtx.slots["attribute"] = "attribute <A> {} </A> {} {} <V> {} </V>".format(ctx.slots["attribute"], ctx.slots["OP"], ctx.slots["value_type"], ctx.slots["value"])
        return super().exitFilterAttr(ctx)
    
    def enterFilterQualifier(self, ctx: ProgramParser.FilterQualifierContext):
        ctx.slots = {"attribute": "", "value": "", "value_type": "", "OP": ""}
        return super().enterFilterQualifier(ctx)
    
    def exitFilterQualifier(self, ctx: ProgramParser.FilterQualifierContext):
        ctx.parentCtx.slots["qualifier"] = " ( qualifier <Q> {} </Q> {} {} <V> {} </V> )".format(ctx.slots["attribute"], ctx.slots["OP"], ctx.slots["value_type"], ctx.slots["value"])
        return super().exitFilterQualifier(ctx)     
    
    # def enterSelectAmong(self, ctx: ProgramParser.SelectAmongContext):
    #     ctx.slots = {"key": "", "OP": ""}
    #     return super().enterSelectAmong(ctx)
    
    # def exitSelectAmong(self, ctx: ProgramParser.SelectAmongContext):
    #     ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
    #     ctx.parentCtx.slots["selectOP"] = ctx.slots["OP"]
    #     return super().exitSelectAmong(ctx)

    # def enterSelectBetween(self, ctx: ProgramParser.SelectBetweenContext):
    #     ctx.slots = {"key": "", "OP": ""}
    #     return super().enterSelectBetween(ctx)
    
    # def exitSelectBetween(self, ctx: ProgramParser.SelectBetweenContext):
    #     ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
    #     ctx.parentCtx.slots["selectOP"] = ctx.slots["OP"]
    #     return super().exitSelectBetween(ctx)

    def enterSelect(self, ctx: ProgramParser.SelectContext):
        ctx.slots = {"key": "", "OP": "", "topK": "", "start": ""}
        return super().enterSelect(ctx)
    
    def exitSelect(self, ctx: ProgramParser.SelectContext):
        try:
            assert ctx.slots["start"] == 0
        except:
            raise NotImplementedError("start position arugment of Select() function is not supported yet.")
        if ctx.slots["topK"] == 1:
            ctx.parentCtx.slots["attributeRankFilter"] = "which one has the {} attribute <A> {} </A>".format(ctx.slots["OP"], ctx.slots["key"])
        else:
            ctx.parentCtx.slots["attributeRankFilter"] = "which one has the top {} {} attribute <A> {} </A>".format(ctx.slots["topK"], ctx.slots["OP"], ctx.slots["key"])
        return super().exitSelect(ctx)
    
    def enterQueryAttribute(self, ctx: ProgramParser.QueryAttributeContext):
        ctx.slots = {"key": ""}
        return super().enterQueryAttribute(ctx)

    def exitQueryAttribute(self, ctx: ProgramParser.QueryAttributeContext):
        ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
        return super().exitQueryAttribute(ctx)

    def enterQueryAttributeUnderCondition(self, ctx: ProgramParser.QueryAttributeUnderConditionContext):
        ctx.slots = {"key": "", "qkey": "", "qvalue": ""}
        return super().enterQueryAttributeUnderCondition(ctx)
    
    def exitQueryAttributeUnderCondition(self, ctx: ProgramParser.QueryAttributeUnderConditionContext):
        ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
        ctx.parentCtx.slots["qualifier"] = " ( qualifier <Q> {} </Q> is value <V> {} </V> )".format(ctx.slots["qkey"], ctx.slots["qvalue"])
        return super().exitQueryAttributeUnderCondition(ctx)

    def enterVerify(self, ctx: ProgramParser.VerifyContext):
        ctx.slots = {"value": "", "value_type": "", "OP": ""}
        return super().enterVerify(ctx)
    
    def exitVerify(self, ctx: ProgramParser.VerifyContext):
        ctx.parentCtx.slots["verify"] = "{} {} <V> {} </V>".format(ctx.slots["OP"], ctx.slots["value_type"], ctx.slots["value"])
        return super().exitVerify(ctx)

    
    def enterFilterStr(self, ctx: ProgramParser.FilterStrContext):
        ctx.slots = {"key": "", "OP": "", "value": ""}
        return super().enterFilterStr(ctx)

    def exitFilterStr(self, ctx: ProgramParser.FilterStrContext):
        ctx.parentCtx.slots["value_type"] = "text"
        ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
        ctx.parentCtx.slots["OP"] = "is"
        ctx.parentCtx.slots["value"] = ctx.slots["value"] 
        return super().exitFilterStr(ctx)

    def enterFilterNum(self, ctx: ProgramParser.FilterNumContext):
        ctx.slots = {"key": "", "OP": "", "value": ""}
        return super().enterFilterNum(ctx)

    def exitFilterNum(self, ctx: ProgramParser.FilterNumContext):
        ctx.parentCtx.slots["value_type"] = "number"
        ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"] 
        return super().exitFilterNum(ctx)

    def enterFilterYear(self, ctx: ProgramParser.FilterYearContext):
        ctx.slots = {"key": "", "OP": "", "value": ""}
        return super().enterFilterYear(ctx)

    def exitFilterYear(self, ctx: ProgramParser.FilterYearContext):
        ctx.parentCtx.slots["value_type"] = "year"
        ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"] 
        return super().exitFilterYear(ctx)

    def enterFilterDate(self, ctx: ProgramParser.FilterDateContext):
        ctx.slots = {"key": "", "OP": "", "value": ""}
        return super().enterFilterDate(ctx)

    def exitFilterDate(self, ctx: ProgramParser.FilterDateContext):
        ctx.parentCtx.slots["value_type"] = "date"
        ctx.parentCtx.slots["attribute"] = ctx.slots["key"]
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"] 
        return super().exitFilterDate(ctx)



    def enterFilterStrQualifier(self, ctx: ProgramParser.FilterStrQualifierContext):
        ctx.slots = {"qkey": "", "OP": "", "qvalue": ""}
        return super().enterFilterStrQualifier(ctx)
    
    def exitFilterStrQualifier(self, ctx: ProgramParser.FilterStrQualifierContext):
        ctx.parentCtx.slots["value_type"] = "text"
        ctx.parentCtx.slots["attribute"] = ctx.slots["qkey"]
        ctx.parentCtx.slots["OP"] = "is"
        ctx.parentCtx.slots["value"] = ctx.slots["qvalue"] 
        return super().exitFilterStrQualifier(ctx)
    
    def enterFilterNumQualifier(self, ctx: ProgramParser.FilterNumQualifierContext):
        ctx.slots = {"qkey": "", "OP": "", "value": ""}
        return super().enterFilterNumQualifier(ctx)
    
    def exitFilterNumQualifier(self, ctx: ProgramParser.FilterNumQualifierContext):
        ctx.parentCtx.slots["value_type"] = "number"
        ctx.parentCtx.slots["attribute"] = ctx.slots["qkey"]
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["qvalue"] 
        return super().exitFilterNumQualifier(ctx)
    
    def enterFilterYearQualifier(self, ctx: ProgramParser.FilterYearQualifierContext):
        ctx.slots = {"qkey": "", "OP": "", "qvalue": ""}
        return super().enterFilterYearQualifier(ctx)

    def exitFilterYearQualifier(self, ctx: ProgramParser.FilterYearQualifierContext):
        ctx.parentCtx.slots["value_type"] = "year"
        ctx.parentCtx.slots["attribute"] = ctx.slots["qkey"]
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["qvalue"] 
        return super().exitFilterYearQualifier(ctx)

    def enterFilterDateQualifier(self, ctx: ProgramParser.FilterDateQualifierContext):
        ctx.slots = {"qkey": "", "OP": "", "qvalue": ""}
        return super().enterFilterDateQualifier(ctx)

    def exitFilterDateQualifier(self, ctx: ProgramParser.FilterDateQualifierContext):
        ctx.parentCtx.slots["value_type"] = "date"
        ctx.parentCtx.slots["attribute"] = ctx.slots["qkey"]
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["qvalue"] 
        return super().exitFilterDateQualifier(ctx)



    def enterVerifyStr(self, ctx: ProgramParser.VerifyStrContext):
        ctx.slots = {"value": "", "value_type": "", "OP": ""}
        return super().enterVerifyStr(ctx)

    def exitVerifyStr(self, ctx: ProgramParser.VerifyStrContext):
        ctx.parentCtx.slots["value_type"] = "text"
        ctx.parentCtx.slots["OP"] = "is"
        ctx.parentCtx.slots["value"] = ctx.slots["value"] 
        return super().enterVerifyStr(ctx)
    
    def enterVerifyNum(self, ctx: ProgramParser.VerifyNumContext):
        ctx.slots = {"value": "", "value_type": "", "OP": ""}
        return super().enterVerifyNum(ctx)
    
    def exitVerifyNum(self, ctx: ProgramParser.VerifyNumContext):
        ctx.parentCtx.slots["value_type"] = "number"
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"] 
        return super().exitVerifyNum(ctx)
    
    def enterVerifyYear(self, ctx: ProgramParser.VerifyYearContext):
        ctx.slots = {"value": "", "value_type": "", "OP": ""}
        return super().enterVerifyYear(ctx)

    def exitVerifyYear(self, ctx: ProgramParser.VerifyYearContext):
        ctx.parentCtx.slots["value_type"] = "year"
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"] 
        return super().exitVerifyYear(ctx)
    
    def enterVerifyDate(self, ctx: ProgramParser.VerifyDateContext):
        ctx.slots = {"value": "", "value_type": "", "OP": ""}
        return super().enterVerifyDate(ctx)

    def exitVerifyDate(self, ctx: ProgramParser.VerifyDateContext):
        ctx.parentCtx.slots["value_type"] = "date"
        ctx.parentCtx.slots["OP"] = ctx.slots["OP"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"] 
        return super().exitVerifyDate(ctx)
    

    def enterEntity(self, ctx: ProgramParser.EntityContext):
        ctx.slots = {"string": ""}
        return super().enterEntity(ctx)
    
    def exitEntity(self, ctx: ProgramParser.EntityContext):
        ctx.parentCtx.slots["entity"] = ctx.slots["string"]
        return super().exitEntity(ctx)
    
    def enterConcept(self, ctx: ProgramParser.ConceptContext):
        ctx.slots = {"string": ""}
        return super().enterConcept(ctx)
    
    def exitConcept(self, ctx: ProgramParser.ConceptContext):
        ctx.parentCtx.slots["concept"] = ctx.slots["string"]
        return super().exitConcept(ctx)
    
    def enterPredicate(self, ctx: ProgramParser.PredicateContext):
        ctx.slots = {"string": ""}
        return super().enterPredicate(ctx)
    
    def exitPredicate(self, ctx: ProgramParser.PredicateContext):
        ctx.parentCtx.slots["predicate"] = ctx.slots["string"]
        return super().exitPredicate(ctx)
    
    def enterKey(self, ctx: ProgramParser.KeyContext):
        ctx.slots = {"string": ""}
        return super().enterKey(ctx)
    
    def exitKey(self, ctx: ProgramParser.KeyContext):
        ctx.parentCtx.slots["key"] = ctx.slots["string"]
        return super().exitKey(ctx)
    
    def enterValue(self, ctx: ProgramParser.ValueContext):
        ctx.slots = {"string": ""}
        return super().enterValue(ctx)
    
    def exitValue(self, ctx: ProgramParser.ValueContext):
        ctx.parentCtx.slots["value"] = ctx.slots["string"]
        return super().exitValue(ctx)
    
    def enterQkey(self, ctx: ProgramParser.QkeyContext):
        ctx.slots = {"string": ""}
        return super().enterQkey(ctx)
    
    def exitQkey(self, ctx: ProgramParser.QkeyContext):
        ctx.parentCtx.slots["qkey"] = ctx.slots["string"]
        return super().exitQkey(ctx)
    
    def enterQvalue(self, ctx: ProgramParser.QvalueContext):
        ctx.slots = {"string": ""}
        return super().enterQvalue(ctx)
    
    def exitQvalue(self, ctx: ProgramParser.QvalueContext):
        ctx.parentCtx.slots["qvalue"] = ctx.slots["string"]
        return super().exitQvalue(ctx)
    
    def enterTopk(self, ctx: ProgramParser.TopkContext):
        ctx.slots = {"string": ""}
        return super().enterTopk(ctx)
    
    def exitTopk(self, ctx: ProgramParser.TopkContext):
        ctx.parentCtx.slots["topK"] = ctx.slots["string"]
        return super().exitTopk(ctx)
    
    def enterStart(self, ctx: ProgramParser.StartContext):
        ctx.slots = {"string": ""}
        return super().enterStart(ctx)

    def exitStart(self, ctx: ProgramParser.StartContext):
        ctx.parentCtx.slots["start"] = ctx.slots["string"]
        return super().exitStart(ctx)

    def exitSymbolOP(self, ctx: ProgramParser.SymbolOPContext):
        op = ctx.stop.text
        ctx.parentCtx.parentCtx.slots["OP"] = self.symbolOP_vocab[op]
        return super().exitSymbolOP(ctx)
    
    def exitStringOP(self, ctx: ProgramParser.StringOPContext):
        op = ctx.stop.text
        ctx.parentCtx.parentCtx.slots["OP"] = self.stringOP_vocab[op]
        return super().exitStringOP(ctx)
    
    def exitAnd(self, ctx: ProgramParser.AndContext):
        ctx.parentCtx.parentCtx.slots["setOP"] = self.setOP_vocab["and"]
        return super().exitAnd(ctx)
    
    def exitOr(self, ctx: ProgramParser.OrContext):
        ctx.parentCtx.parentCtx.slots["setOP"] = self.setOP_vocab["or"]
        return super().exitOr(ctx)
    
    def exitDirection(self, ctx: ProgramParser.DirectionContext):
        if not isinstance(ctx.parentCtx, ProgramParser.StringContext):
            ctx.parentCtx.slots["direction"] = str(ctx.getText())
        return super().exitDirection(ctx)

    def enterString(self, ctx: ProgramParser.StringContext):
        if not isinstance(ctx.parentCtx, ProgramParser.StringContext):
            ctx.parentCtx.slots["string"] = str(ctx.getText())
        

    # def exitString(self, ctx: ProgramParser.StringContext):
    #     ctx.parentCtx.slots["string"] = str(ctx.getText())
    #     return super().exitString(ctx)
    

def get_program_seq(program):
    seq = []
    for item in program:
        func = item['function']
        inputs = item['inputs']
        seq.append(func + '(' + '<c>'.join(inputs) + ')')
    seq = '<b>'.join(seq)
    return seq

def program_to_ir(program):
    listener = IREmitter()
    walker = ParseTreeWalker() 

    program = get_program_seq(program)
    input_stream = InputStream(program)
    lexer = ProgramLexer(input_stream)       
    token_stream = CommonTokenStream(lexer)
    parser = ProgramParser(token_stream)
    
    tree = parser.query()
    walker.walk(listener, tree)
    ir = listener.getIR(tree)

    return ir

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()

    train_data = json.load(open(os.path.join(args.input_dir, 'train.json')))
    train_program = [get_program_seq(item['program']) for item in train_data]
    val_data = json.load(open(os.path.join(args.input_dir, 'val.json')))
    val_program = [get_program_seq(item['program']) for item in val_data]
    test_data = json.load(open(os.path.join(args.input_dir, 'test.json')))
    test_program = [get_program_seq(item['program']) for item in test_data]
        
    listener = IREmitter()
    walker = ParseTreeWalker() 

    for name, program_file in zip(["train", "val", "test"], [train_program, val_program, test_program]):
        print("Processing {} set IRs".format(name))
        file = open(os.path.join(args.output_dir, "{}_IR.txt".format(name)), "w+")
        for program in tqdm(program_file):
            input_stream = InputStream(program)
            lexer = ProgramLexer(input_stream)       
            token_stream = CommonTokenStream(lexer)
            parser = ProgramParser(token_stream)

            tree = parser.query()
            lisp_tree_str = tree.toStringTree(recog=parser)
            # print(lisp_tree_str)
                    
            walker.walk(listener, tree)
            file.write(listener.getIR(tree)+"\n")
        file.close()

    