from antlr4 import *

from .ProgramLexer import ProgramLexer
from .ProgramParser import ProgramParser
from .ProgramListener import ProgramListener

class IREmitter(ProgramListener):
    def __init__(self):
        self.ir = ""

        self.data_type = {  "entity": "E", 
                            "attribute": "A",
                            "concept": "C",
                            "value": "V",
                            "qualifier": "Q",
                            "relation": "R"}
        
        self.setOP_vocab = {    "and": "and",
                                "or": "or" }

        self.symbolOP_vocab = { "=": "is", 
                                "<": "larger than", 
                                ">": "smaller than", 
                                "!=": "not is" }

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
    
    def scoping(self, type, text):
        if type not in self.data_type.keys():
            raise TypeError("{} is not a valid type.".format(type))
        return "<{}> {} </{}>".format(self.data_type[type], text, self.data_type[type])



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
        if ctx.slots["entitySet"][:5] == "which":
            ctx.parentCtx.slots["query"] = ctx.slots["entitySet"]
        else:
            ctx.parentCtx.slots["query"] = "what is {}".format(self.scoping("entity", ctx.slots["entitySet"]))
        return super().exitWhatEntityQuery(ctx)
    
    def enterHowManyEntityQuery(self, ctx: ProgramParser.HowManyEntityQueryContext):
        ctx.slots = {"entitySet": ""}
        return super().enterHowManyEntityQuery(ctx)
    
    def exitHowManyEntityQuery(self, ctx: ProgramParser.HowManyEntityQueryContext):
        ctx.parentCtx.slots["query"] = "count {}".format(self.scoping("entity", ctx.slots["entitySet"]))
        return super().exitHowManyEntityQuery(ctx)

    def enterWhatAttributeQuery(self, ctx: ProgramParser.WhatAttributeQueryContext):
        ctx.slots = {"entitySet": "", "attribute": ""}
        return super().enterWhatAttributeQuery(ctx)

    def exitWhatAttributeQuery(self, ctx: ProgramParser.WhatAttributeQueryContext):
        ctx.parentCtx.slots["query"] = "what is {} of {}".format(self.scoping("attribute", ctx.slots["attribute"]), self.scoping("entity", ctx.slots["entitySet"]))
        return super().exitWhatAttributeQuery(ctx)
    
    def enterWhatRelationQuery(self, ctx: ProgramParser.WhatRelationQueryContext):
        ctx.slots = {"entitySetGroup": []}
        return super().enterWhatRelationQuery(ctx)
    
    def exitWhatRelationQuery(self, ctx: ProgramParser.WhatRelationQueryContext):
        ctx.parentCtx.slots["query"] = "what is the relation from {} to {}".format(self.scoping("entity", ctx.slots["entitySetGroup"][0]), self.scoping("entity", ctx.slots["entitySetGroup"][1]))
        return super().exitWhatRelationQuery(ctx)

    def enterAttributeSatisfyQuery(self, ctx: ProgramParser.AttributeSatisfyQueryContext):
        ctx.slots = {"entitySet": "", "attribute": "", "verify": "", "qualifier": ""}
        return super().enterAttributeSatisfyQuery(ctx)
    
    def exitAttributeSatisfyQuery(self, ctx: ProgramParser.AttributeSatisfyQueryContext):
        ctx.parentCtx.slots["query"] = "whether {} {} {}{}".format(self.scoping("entity", ctx.slots["entitySet"]), self.scoping("attribute", ctx.slots["attribute"]), ctx.slots["verify"], ctx.slots["qualifier"])
        return super().exitAttributeSatisfyQuery(ctx)

    def enterWhatAttributeQualifierQuery(self, ctx: ProgramParser.WhatAttributeQualifierQueryContext):
        ctx.slots = {"entitySet": "", "attribute": "", "value": "", "qualifier": ""}
        return super().enterWhatAttributeQualifierQuery(ctx)

    def exitWhatAttributeQualifierQuery(self, ctx: ProgramParser.WhatAttributeQualifierQueryContext):
        ctx.parentCtx.slots["query"] = "what is the {} of {} whose {} is {}".format(self.scoping("qualifier", ctx.slots["qualifier"]), self.scoping("entity", ctx.slots["entitySet"]), self.scoping("attribute", ctx.slots["attribute"]), self.scoping("value", ctx.slots["value"]))
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
        ctx.parentCtx.slots["query"] = "what is the {} of {} that {} to {}".format(self.scoping("qualifier", ctx.slots["qualifier"]), self.scoping("entity", ctx.slots["entitySetGroup"][0]), self.scoping("relation", ctx.slots["predicate"]), self.scoping("entity", ctx.slots["entitySetGroup"][1]))
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
        self.insertParentEntitySet(ctx.parentCtx, "{} {} {}".format(self.scoping("entity", ctx.slots["entitySet"][0]), ctx.slots["setOP"], self.scoping("entity", ctx.slots["entitySet"][1])))
        return super().exitEntitySetByOP(ctx)

    def enterEntitySetByRank(self, ctx: ProgramParser.EntitySetByRankContext):
        ctx.slots = {"entitySet": "", "attributeRankFilter": ""}
        return super().enterEntitySetByRank(ctx)
    
    def exitEntitySetByRank(self, ctx: ProgramParser.EntitySetByRankContext):
        self.insertParentEntitySet(ctx.parentCtx, "{} among {}".format(ctx.slots["attributeRankFilter"], self.scoping("entity", ctx.slots["entitySet"])))
        return super().exitEntitySetByRank(ctx)
    
    def enterEntitySetNested(self, ctx: ProgramParser.EntitySetNestedContext):
        ctx.slots = {"entitySet": "", "relationFilter": "", "attributeFilter": "", "conceptFilter": "", "qualifierFilter": ""}
        return super().enterEntitySetNested(ctx)
    
    def exitEntitySetNested(self, ctx: ProgramParser.EntitySetNestedContext):
        if ctx.slots["relationFilter"]:
            if ctx.slots["conceptFilter"]:
                self.insertParentEntitySet(ctx.parentCtx, "the {}{} {}{}".format(ctx.slots["conceptFilter"], ctx.slots["relationFilter"], ctx.slots["entitySet"], ctx.slots["qualifierFilter"]))
            else:
                self.insertParentEntitySet(ctx.parentCtx, "the one {} {}{}".format(ctx.slots["relationFilter"], self.scoping("entity", ctx.slots["entitySet"]), ctx.slots["qualifierFilter"]))
        elif ctx.slots["attributeFilter"]:
            self.insertParentEntitySet(ctx.parentCtx, "{}{} {}{}".format(ctx.slots["conceptFilter"], self.scoping("entity", ctx.slots["entitySet"]), ctx.slots["attributeFilter"], ctx.slots["qualifierFilter"]))
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
        ctx.parentCtx.slots["relationFilter"] = "that {} {} to".format(self.scoping("relation", ctx.slots["predicate"]), ctx.slots["direction"])
        if ctx.slots["qualifier"]:
            ctx.parentCtx.slots["qualifierFilter"] = ctx.slots["qualifier"]
        if ctx.slots["concept"]:
            ctx.parentCtx.slots["conceptFilter"] = "{} ".format(self.scoping("concept", ctx.slots["concept"]))
        return super().exitEntityFilterByRelation(ctx)
    
    def enterEntityFilterByAttribute(self, ctx: ProgramParser.EntityFilterByAttributeContext):
        ctx.slots = {"attribute": "", "qualifier": "", "concept": ""}
        return super().enterEntityFilterByAttribute(ctx)
    
    def exitEntityFilterByAttribute(self, ctx: ProgramParser.EntityFilterByAttributeContext):
        ctx.parentCtx.slots["attributeFilter"] = "whose {}".format(ctx.slots["attribute"])
        if ctx.slots["qualifier"]:
            ctx.parentCtx.slots["qualifierFilter"] = ctx.slots["qualifier"]
        if ctx.slots["concept"]:
            ctx.parentCtx.slots["conceptFilter"] = "{} ".format(self.scoping("concept", ctx.slots["concept"]))
        return super().exitEntityFilterByAttribute(ctx)   

    def enterEntityFilterByConcept(self, ctx: ProgramParser.EntityFilterByConceptContext):
        ctx.slots = {"concept": ""}
        return super().enterEntityFilterByConcept(ctx)
    
    def exitEntityFilterByConcept(self, ctx: ProgramParser.EntityFilterByConceptContext):
        ctx.parentCtx.slots["conceptFilter"] = "{} ".format(self.scoping("concept", ctx.slots["concept"]))
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
        ctx.parentCtx.slots["attribute"] = "{} {} {} {}".format(self.scoping("attribute", ctx.slots["attribute"]), ctx.slots["OP"], ctx.slots["value_type"], self.scoping("value", ctx.slots["value"]))
        return super().exitFilterAttr(ctx)
    
    def enterFilterQualifier(self, ctx: ProgramParser.FilterQualifierContext):
        ctx.slots = {"attribute": "", "value": "", "value_type": "", "OP": ""}
        return super().enterFilterQualifier(ctx)
    
    def exitFilterQualifier(self, ctx: ProgramParser.FilterQualifierContext):
        ctx.parentCtx.slots["qualifier"] = " ( {} {} {} {} )".format(self.scoping("qualifier", ctx.slots["attribute"]), ctx.slots["OP"], ctx.slots["value_type"], self.scoping("value", ctx.slots["value"]))
        return super().exitFilterQualifier(ctx)

    def enterSelect(self, ctx: ProgramParser.SelectContext):
        ctx.slots = {"key": "", "OP": "", "topK": "", "start": ""}
        return super().enterSelect(ctx)
    
    def exitSelect(self, ctx: ProgramParser.SelectContext):
        try:
            assert ctx.slots["start"] == '0'
        except:
            raise NotImplementedError("customized start position inside Select() function is not supported yet.")
        if ctx.slots["topK"] == '1':
            ctx.parentCtx.slots["attributeRankFilter"] = "which one has the {} {}".format(ctx.slots["OP"], self.scoping("attribute", ctx.slots["key"]))
        else:
            ctx.parentCtx.slots["attributeRankFilter"] = "which one has the top {} {} {}".format(ctx.slots["topK"], ctx.slots["OP"], self.scoping("attribute", ctx.slots["key"]))
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
        ctx.parentCtx.slots["qualifier"] = " ( {} is {} )".format(self.scoping("qualifier", ctx.slots["qkey"]), self.scoping("value", ctx.slots["qvalue"]))
        return super().exitQueryAttributeUnderCondition(ctx)

    def enterVerify(self, ctx: ProgramParser.VerifyContext):
        ctx.slots = {"value": "", "value_type": "", "OP": ""}
        return super().enterVerify(ctx)
    
    def exitVerify(self, ctx: ProgramParser.VerifyContext):
        ctx.parentCtx.slots["verify"] = "{} {} {}".format(ctx.slots["OP"], ctx.slots["value_type"], self.scoping("value", ctx.slots["value"]))
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
        


    


    