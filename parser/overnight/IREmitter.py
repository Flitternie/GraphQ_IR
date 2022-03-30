import os
import re
from antlr4 import *

from .OvernightLexer import OvernightLexer
from .OvernightParser import OvernightParser
from .OvernightListener import OvernightListener

from ..utils import *
from ..ir.utils import *

class IREmitter(OvernightListener):
    def __init__(self):
        self.ir = ""
    
    def get_ir(self, ctx):
        return self.ir        

    def enterRoot(self, ctx: OvernightParser.RootContext):
        self.ir = ""
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterRoot(ctx)
    
    def exitRoot(self, ctx: OvernightParser.RootContext):
        self.ir = str(ctx.slots["entitySet"]).replace("  ", " ").strip()
        if self.ir.startswith("<{}>".format(data_type["attribute"])):
            self.ir = "what is the attribute " + self.ir
        elif self.ir.startswith("size of"):
            self.ir = self.ir.replace("size of", "how many")
        else:
            self.ir = "what is " + self.ir
        return super().exitRoot(ctx)
    
    def enterConcatNP(self, ctx: OvernightParser.ConcatNPContext):
        ctx.slots = strictDict({"entitySet": []})
        return super().enterConcatNP(ctx)   

    def exitConcatNP(self, ctx: OvernightParser.ConcatNPContext):
        assert isinstance(ctx.slots["entitySet"], list) and len(ctx.slots["entitySet"]) == 2
        insert(ctx.parentCtx, "{} or {}".format(scoping("entity", ctx.slots["entitySet"][0]), scoping("entity", ctx.slots["entitySet"][1])))
        if isinstance(ctx.parentCtx, OvernightParser.RootContext):
            ctx.parentCtx.slots["entitySet"] = scoping("entity", ctx.parentCtx.slots["entitySet"])
        return super().exitConcatNP(ctx) 
    
    def enterAggregateNP(self, ctx: OvernightParser.AggregateNPContext):
        ctx.slots = strictDict({"aggregateType": "", "entitySet": ""})
        return super().enterAggregateNP(ctx)
    
    def exitAggregateNP(self, ctx: OvernightParser.AggregateNPContext):
        insert(ctx.parentCtx, "{} of {}".format(ctx.slots["aggregateType"], ctx.slots["entitySet"]))
        return super().exitAggregateNP(ctx)
    
    def enterSizeNP(self, ctx: OvernightParser.SizeNPContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterSizeNP(ctx)
    
    def exitSizeNP(self, ctx: OvernightParser.SizeNPContext):
        insert(ctx.parentCtx, "size of {}".format(scoping("entity", ctx.slots["entitySet"])))
        return super().exitSizeNP(ctx)
    
    def enterGetPropertyNP(self, ctx: OvernightParser.GetPropertyNPContext):
        ctx.slots = strictDict({"entitySet": "", "relNP": ""})
        return super().enterGetPropertyNP(ctx)
    
    def exitGetPropertyNP(self, ctx: OvernightParser.GetPropertyNPContext):
        if isinstance(ctx.parentCtx, OvernightParser.NumericEntityNPContext):
            ctx.parentCtx.slots["value"] = "{} of {}".format(scoping("attribute", ctx.slots["relNP"]), scoping("entity", ctx.slots["entitySet"]))
        else:
            insert(ctx.parentCtx, "{} of {}".format(scoping("attribute", ctx.slots["relNP"]), scoping("entity", ctx.slots["entitySet"])))
        return super().exitGetPropertyNP(ctx)
    
    def enterDomainCPNP(self, ctx: OvernightParser.DomainCPNPContext):
        ctx.slots = strictDict({"entitySet": "", "relNP": ""})
        return super().enterDomainCPNP(ctx)
    
    def exitDomainCPNP(self, ctx: OvernightParser.DomainCPNPContext):
        insert(ctx.parentCtx, "{} {}".format(scoping("concept", ctx.slots["relNP"]), scoping("entity", ctx.slots["entitySet"])))
        if isinstance(ctx.parentCtx, OvernightParser.RootContext): 
            ctx.parentCtx.slots["entitySet"] = scoping("entity", ctx.parentCtx.slots["entitySet"])
        return super().exitDomainCPNP(ctx)
    
    def enterEntityNP(self, ctx: OvernightParser.EntityNPContext):
        ctx.slots = strictDict({"entity": ""})
        return super().enterEntityNP(ctx)

    def exitEntityNP(self, ctx: OvernightParser.EntityNPContext):
        insert(ctx.parentCtx, ctx.slots["entity"], is_atom=True)
        return super().exitEntityNP(ctx)
    
    def enterNumericNP(self, ctx: OvernightParser.NumericNPContext):
        ctx.slots = strictDict({"value": "", "valueType": ""})
        return super().enterNumericNP(ctx)
    
    def exitNumericNP(self, ctx: OvernightParser.NumericNPContext):
        if isinstance(ctx.parentCtx, OvernightParser.RootContext):
            insert(ctx.parentCtx, "{} {}".format(ctx.slots["valueType"], scoping("value", ctx.slots["value"])))
        else:
            ctx.parentCtx.slots["value"] = ctx.slots["value"]
            ctx.parentCtx.slots["valueType"] = ctx.slots["valueType"]
        return super().exitNumericNP(ctx)
    
    def enterFilterNP(self, ctx: OvernightParser.FilterNPContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterFilterNP(ctx)
    
    def exitFilterNP(self, ctx: OvernightParser.FilterNPContext):
        insert(ctx.parentCtx, ctx.slots["entitySet"])    
        return super().exitFilterNP(ctx)

    def enterCPNP(self, ctx: OvernightParser.CPNPContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterCPNP(ctx)
    
    def exitCPNP(self, ctx: OvernightParser.CPNPContext):
        insert(ctx.parentCtx, ctx.slots["entitySet"])
        if isinstance(ctx.parentCtx, OvernightParser.RootContext):
            ctx.parentCtx.slots["entitySet"] = scoping("entity", ctx.parentCtx.slots["entitySet"])
        return super().exitCPNP(ctx)
    
    def enterNestedCP(self, ctx: OvernightParser.NestedCPContext):
        ctx.slots = strictDict({"entitySet": "", "string": ""})
        return super().enterNestedCP(ctx)
    
    def exitNestedCP(self, ctx: OvernightParser.NestedCPContext):
        insert(ctx.parentCtx, ctx.slots["entitySet"])
        return super().exitNestedCP(ctx)
    
    def enterCP(self, ctx: OvernightParser.CPContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterCP(ctx)
    
    def exitCP(self, ctx: OvernightParser.CPContext):
        insert(ctx.parentCtx, ctx.slots["entitySet"])
        return super().exitCP(ctx)
    
    def enterFilterByPredicate(self, ctx: OvernightParser.FilterByPredicateContext):
        ctx.slots = strictDict({"entitySet": [], "predicate": "", "OP": "", "value": ""})
        return super().enterFilterByPredicate(ctx)

    def exitFilterByPredicate(self, ctx: OvernightParser.FilterByPredicateContext):
        assert isinstance(ctx.slots["entitySet"], list)
        if ctx.slots["OP"] == symbolOP_vocab["!="]:
            logic_gate = "not"
        else:
            logic_gate = ""
        if len(ctx.slots["entitySet"]) == 1:
            insert(ctx.parentCtx, "{} that {} {} forward to entities".format(scoping("entity", ctx.slots["entitySet"][0]), logic_gate, scoping("relation", ctx.slots["predicate"])))
        elif len(ctx.slots["entitySet"]) == 2:
            insert(ctx.parentCtx, "{} that {} {} forward to {}".format(scoping("entity", ctx.slots["entitySet"][0]), logic_gate, scoping("relation", ctx.slots["predicate"]), scoping("entity", ctx.slots["entitySet"][1])))
        else:
            print(ctx.slots["OP"])
            raise ValueError()
        return super().exitFilterByPredicate(ctx)
    
    def enterFilterByAttribute(self, ctx: OvernightParser.FilterByAttributeContext):
        ctx.slots = strictDict({"entitySet": "", "relNP": "", "OP": "", "valueType":"", "value": ""})
        return super().enterFilterByAttribute(ctx)
    
    def exitFilterByAttribute(self, ctx: OvernightParser.FilterByAttributeContext):
        insert(ctx.parentCtx, "{} whose {} {} {} {}".format(scoping("entity", ctx.slots["entitySet"]), scoping("attribute", ctx.slots["relNP"]), ctx.slots["OP"], ctx.slots["valueType"], scoping("value", ctx.slots["value"])))
        return super().exitFilterByAttribute(ctx)
    
    def enterFilterByReversePredicate(self, ctx: OvernightParser.FilterByReversePredicateContext):
        ctx.slots = strictDict({"entitySet": [], "predicate": "", "OP": ""})
        return super().enterFilterByReversePredicate(ctx)
    
    def exitFilterByReversePredicate(self, ctx: OvernightParser.FilterByReversePredicateContext):
        assert isinstance(ctx.slots["entitySet"], list) and len(ctx.slots["entitySet"]) == 2
        if ctx.slots["OP"] == symbolOP_vocab["="]:
            logic_gate = ""
        elif ctx.slots["OP"] == symbolOP_vocab["!="]:
            logic_gate = "not"
        else:
            print(ctx.slots["OP"])
            raise ValueError()
        insert(ctx.parentCtx, "{} that {} {} backward to {}".format(scoping("entity", ctx.slots["entitySet"][0]), logic_gate, scoping("relation", ctx.slots["predicate"]), scoping("entity", ctx.slots["entitySet"][1])))
        return super().exitFilterByReversePredicate(ctx)
    
    def enterSuperlativeByAttribute(self, ctx: OvernightParser.SuperlativeByAttributeContext):
        ctx.slots = strictDict({"entitySet": "", "relNP": "", "OP": ""})
        return super().enterSuperlativeByAttribute(ctx)

    def exitSuperlativeByAttribute(self, ctx: OvernightParser.SuperlativeByAttributeContext):
        insert(ctx.parentCtx, "{} that has {} {}".format(scoping("entity", ctx.slots["entitySet"]), ctx.slots["OP"], scoping("attribute", ctx.slots["relNP"])))
        return super().exitSuperlativeByAttribute(ctx)
    
    def enterSuperlativeByPredicate(self, ctx: OvernightParser.SuperlativeByPredicateContext):
        ctx.slots = strictDict({"entitySet": [], "relNP": "", "predicate": "", "OP": ""})
        return super().enterSuperlativeByPredicate(ctx)
    
    def exitSuperlativeByPredicate(self, ctx: OvernightParser.SuperlativeByPredicateContext):
        assert isinstance(ctx.slots["entitySet"], list) 
        if len(ctx.slots["entitySet"]) == 1 and ctx.slots["relNP"] != "":
            insert(ctx.parentCtx, "{} that {} forward to {} entities".format(scoping("entity", ctx.slots["entitySet"][0]), scoping("relation", ctx.slots["relNP"]), ctx.slots["OP"]))
        elif len(ctx.slots["entitySet"]) == 2 and ctx.slots["predicate"] != "":
            insert(ctx.parentCtx, "{} that {} forward to {} {}".format(scoping("entity", ctx.slots["entitySet"][0]), scoping("relation", ctx.slots["predicate"]), ctx.slots["OP"], scoping("entity", ctx.slots["entitySet"][1])))
        else:
            raise ValueError
        return super().exitSuperlativeByPredicate(ctx)

    def enterSuperlativeByReversePredicate(self, ctx: OvernightParser.SuperlativeByReversePredicateContext):
        ctx.slots = strictDict({"entitySet": [], "predicate": "", "OP": ""})
        return super().enterSuperlativeByReversePredicate(ctx)
    
    def exitSuperlativeByReversePredicate(self, ctx: OvernightParser.SuperlativeByReversePredicateContext):
        assert isinstance(ctx.slots["entitySet"], list) and len(ctx.slots["entitySet"]) == 2
        insert(ctx.parentCtx, "{} that {} backward to {} {}".format(scoping("entity", ctx.slots["entitySet"][0]), scoping("relation", ctx.slots["predicate"]), ctx.slots["OP"], scoping("entity", ctx.slots["entitySet"][1])))
        return super().exitSuperlativeByReversePredicate(ctx)
    
    # def enterComparativeByAttribute(self, ctx: OvernightParser.ComparativeByAttributeContext):
    #     ctx.slots = strictDict({"entitySet": "", "relNP": "", "OP": "", "valueType":"", "value": ""})
    #     return super().enterComparativeByAttribute(ctx)
    
    # def exitComparativeByAttribute(self, ctx: OvernightParser.ComparativeByAttributeContext):
    #     insert(ctx.parentCtx, "{} whose {} {} {} {}".format(scoping("entity", ctx.slots["entitySet"]), scoping("attribute", ctx.slots["relNP"]), ctx.slots["OP"], ctx.slots["valueType"], scoping("value", ctx.slots["value"])))
    #     return super().exitComparativeByAttribute(ctx)

    def enterComparativeByPredicate(self, ctx: OvernightParser.ComparativeByPredicateContext):
        ctx.slots = strictDict({"entitySet": [], "relNP": "", "predicate": "", "OP": "", "valueType":"", "value": ""})
        return super().enterComparativeByPredicate(ctx)
    
    def exitComparativeByPredicate(self, ctx: OvernightParser.ComparativeByPredicateContext):
        assert isinstance(ctx.slots["entitySet"], list) 
        if len(ctx.slots["entitySet"]) == 1 and ctx.slots["relNP"] != "":
            insert(ctx.parentCtx, "{} that {} forward to {} {} {} entities".format(scoping("entity", ctx.slots["entitySet"][0]), scoping("relation", ctx.slots["relNP"]), ctx.slots["OP"], ctx.slots["valueType"], scoping("value", ctx.slots["value"])))
        elif len(ctx.slots["entitySet"]) == 2 and ctx.slots["predicate"] != "":
            insert(ctx.parentCtx, "{} that {} forward to {} {} {} {}".format(scoping("entity", ctx.slots["entitySet"][0]), scoping("relation", ctx.slots["predicate"]), ctx.slots["OP"], ctx.slots["valueType"], scoping("value", ctx.slots["value"]), scoping("entity", ctx.slots["entitySet"][1])))
        else:
            raise ValueError
        return super().exitComparativeByPredicate(ctx)
    
    def enterComparativeByReversePredicate(self, ctx: OvernightParser.ComparativeByReversePredicateContext):
        ctx.slots = strictDict({"entitySet": [], "predicate": "", "OP": "", "valueType":"", "value": ""})
        return super().enterComparativeByReversePredicate(ctx)
    
    def exitComparativeByReversePredicate(self, ctx: OvernightParser.ComparativeByReversePredicateContext):
        insert(ctx.parentCtx, "{} that {} backward to {} {} {} {}".format(scoping("entity", ctx.slots["entitySet"][0]), scoping("relation", ctx.slots["predicate"]), ctx.slots["OP"], ctx.slots["valueType"], scoping("value", ctx.slots["value"]), scoping("entity", ctx.slots["entitySet"][1])))
        return super().exitComparativeByReversePredicate(ctx)
    
    def enterConcatValueNP(self, ctx: OvernightParser.ConcatValueNPContext):
        ctx.slots = strictDict({"value": [], "valueType": ""})
        return super().enterConcatValueNP(ctx)
    
    def exitConcatValueNP(self, ctx: OvernightParser.ConcatValueNPContext):
        ctx.parentCtx.slots["value"] = "{} or {}".format(scoping("value", ctx.slots["value"][0]), scoping("value", ctx.slots["value"][1]))
        ctx.parentCtx.slots["valueType"] = ctx.slots["valueType"]
        return super().exitConcatValueNP(ctx)
    
    def enterAttributeNP(self, ctx: OvernightParser.AttributeNPContext):
        ctx.slots = strictDict({"entitySet": "", "relNP": ""})
        return super().enterAttributeNP(ctx)
    
    def exitAttributeNP(self, ctx: OvernightParser.AttributeNPContext):
        ctx.parentCtx.slots["value"] = "{} of {}".format(scoping("attribute", ctx.slots["relNP"]), scoping("entity", ctx.slots["entitySet"]))
        return super().exitAttributeNP(ctx)

    def enterNumericEntityNP(self, ctx: OvernightParser.NumericEntityNPContext):
        ctx.slots = strictDict({"value": "", "valueType": ""})
        return super().enterNumericEntityNP(ctx)
    
    def exitNumericEntityNP(self, ctx: OvernightParser.NumericEntityNPContext):
        if isinstance(ctx.parentCtx, OvernightParser.ConcatValueNPContext):
            assert ctx.parentCtx.slots["valueType"] == "" or ctx.parentCtx.slots["valueType"] == ctx.slots["valueType"]
            ctx.parentCtx.slots["value"].append(ctx.slots["value"])
            ctx.parentCtx.slots["valueType"] = ctx.slots["valueType"]
        else:
            ctx.parentCtx.slots["value"] = ctx.slots["value"]
            ctx.parentCtx.slots["valueType"] = ctx.slots["valueType"]
        return super().exitNumericEntityNP(ctx)
    
    def enterNumberNP(self, ctx: OvernightParser.NumberNPContext):
        ctx.slots = strictDict({"quantity": "", "string": ""})
        return super().enterNumberNP(ctx)
    
    def exitNumberNP(self, ctx: OvernightParser.NumberNPContext):
        if isinstance(ctx.parentCtx, OvernightParser.ConcatValueNPContext):
            assert ctx.parentCtx.slots["valueType"] == "" or ctx.parentCtx.slots["valueType"] == "number"
            ctx.parentCtx.slots["value"].append("{} {}".format(ctx.slots["quantity"], ctx.slots["string"]))
            ctx.parentCtx.slots["valueType"] = "number"
        else:
            ctx.parentCtx.slots["value"] = "{} {}".format(ctx.slots["quantity"], ctx.slots["string"])
            ctx.parentCtx.slots["valueType"] = "number"
        return super().exitNumberNP(ctx)
    
    def enterDateNP(self, ctx: OvernightParser.DateNPContext):
        ctx.slots = strictDict({"date": ""})
        return super().enterDateNP(ctx)
    
    def exitDateNP(self, ctx: OvernightParser.DateNPContext):
        if isinstance(ctx.parentCtx, OvernightParser.ConcatValueNPContext):
            assert ctx.parentCtx.slots["valueType"] == "" or ctx.parentCtx.slots["valueType"] == "date"
            ctx.parentCtx.slots["value"].append(ctx.slots["date"])
            ctx.parentCtx.slots["valueType"] = "date"
        else:
            ctx.parentCtx.slots["value"] = ctx.slots["date"]
            ctx.parentCtx.slots["valueType"] = "date"
        return super().exitDateNP(ctx)
    
    def enterTimeNP(self, ctx: OvernightParser.TimeNPContext):
        ctx.slots = strictDict({"time": ""})
        return super().enterTimeNP(ctx)
    
    def exitTimeNP(self, ctx: OvernightParser.TimeNPContext):
        if isinstance(ctx.parentCtx, OvernightParser.ConcatValueNPContext):
            assert ctx.parentCtx.slots["valueType"] == "" or ctx.parentCtx.slots["valueType"] == "time"
            ctx.parentCtx.slots["value"].append(ctx.slots["time"])
            ctx.parentCtx.slots["valueType"] = "time"
        else:
            ctx.parentCtx.slots["value"] = ctx.slots["time"]
            ctx.parentCtx.slots["valueType"] = "time"
        return super().exitTimeNP(ctx)
    
    def enterTypeConstraintNP(self, ctx: OvernightParser.TypeConstraintNPContext):
        ctx.slots = strictDict({"concept": ""})
        return super().enterTypeConstraintNP(ctx)
    
    def exitTypeConstraintNP(self, ctx: OvernightParser.TypeConstraintNPContext):
        insert(ctx.parentCtx, scoping("concept", ctx.slots["concept"]))
        return super().exitTypeConstraintNP(ctx)
    
    def enterFilterConstraintNP(self, ctx: OvernightParser.FilterConstraintNPContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterFilterConstraintNP(ctx)
    
    def exitFilterConstraintNP(self, ctx: OvernightParser.FilterConstraintNPContext):
        insert(ctx.parentCtx, ctx.slots["entitySet"])
        return super().exitFilterConstraintNP(ctx)
    
    def enterEventConstraintNP(self, ctx: OvernightParser.EventConstraintNPContext):
        ctx.slots = strictDict({"entitySet": "", "predicate": ""})
        return super().enterEventConstraintNP(ctx)
    
    def exitEventConstraintNP(self, ctx: OvernightParser.EventConstraintNPContext):
        insert(ctx.parentCtx, "{} {}".format(scoping("concept", ctx.slots["predicate"]), scoping("entity", ctx.slots["entitySet"])))
        return super().exitEventConstraintNP(ctx)
    
    def enterVoidConstraintNP(self, ctx: OvernightParser.VoidConstraintNPContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterVoidConstraintNP(ctx)

    def exitVoidConstraintNP(self, ctx: OvernightParser.VoidConstraintNPContext):
        insert(ctx.parentCtx, "ones", is_pop=True)
        return super().exitVoidConstraintNP(ctx)
    
    def exitEqual(self, ctx: OvernightParser.EqualContext):
        if not isinstance(ctx.parentCtx, (OvernightParser.SuperlativeByPredicateContext, OvernightParser.SuperlativeByReversePredicateContext, OvernightParser.ComparativeByPredicateContext, OvernightParser.ComparativeByReversePredicateContext)):
            ctx.parentCtx.slots["OP"] = symbolOP_vocab["="]
        # else:
        #     ctx.parentCtx.slots["OP"] = " "
        return super().exitEqual(ctx) 
    
    def exitNotEqual(self, ctx: OvernightParser.NotEqualContext):
        ctx.parentCtx.slots["OP"] = symbolOP_vocab["!="]
        return super().exitNotEqual(ctx)
    
    def exitLessThan(self, ctx: OvernightParser.LessThanContext):
        ctx.parentCtx.slots["OP"] = symbolOP_vocab["<"]
        return super().exitLessThan(ctx)
    
    def exitGreaterThan(self, ctx: OvernightParser.GreaterThanContext):
        ctx.parentCtx.slots["OP"] = symbolOP_vocab[">"]
        return super().exitGreaterThan(ctx)
    
    def exitLessThanOrEqual(self, ctx: OvernightParser.LessThanOrEqualContext):
        ctx.parentCtx.slots["OP"] = symbolOP_vocab["<="]
        return super().exitLessThanOrEqual(ctx)
    
    def exitGreaterThanOrEqual(self, ctx: OvernightParser.GreaterThanOrEqualContext):
        ctx.parentCtx.slots["OP"] = symbolOP_vocab[">="]
        return super().exitGreaterThanOrEqual(ctx)
    
    def exitMin(self, ctx: OvernightParser.MinContext):
        ctx.parentCtx.slots["OP"] = symbolOP_vocab["min"]
        return super().exitMin(ctx)
    
    def exitMax(self, ctx: OvernightParser.MaxContext):
        ctx.parentCtx.slots["OP"] = symbolOP_vocab["max"]
        return super().exitMax(ctx)
    
    def exitSumAggregate(self, ctx: OvernightParser.SumAggregateContext):
        ctx.parentCtx.slots["aggregateType"] = "sum"
        return super().exitSumAggregate(ctx)
    
    def exitAvgAggregate(self, ctx: OvernightParser.AvgAggregateContext):
        ctx.parentCtx.slots["aggregateType"] = "average"
        return super().exitAvgAggregate(ctx)
    
    def enterEntity(self, ctx: OvernightParser.EntityContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterEntity(ctx)
    
    def exitEntity(self, ctx: OvernightParser.EntityContext):
        ctx.parentCtx.slots["entity"] = ctx.slots["string"]
        return super().exitEntity(ctx)
    
    def enterConcept(self, ctx: OvernightParser.ConceptContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterConcept(ctx)
    
    def exitConcept(self, ctx: OvernightParser.ConceptContext):
        ctx.parentCtx.slots["concept"] = ctx.slots["string"]
        return super().exitConcept(ctx)
    
    def enterPredicate(self, ctx: OvernightParser.PredicateContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterPredicate(ctx)
    
    def exitPredicate(self, ctx: OvernightParser.PredicateContext):
        ctx.parentCtx.slots["predicate"] = ctx.slots["string"]
        return super().exitPredicate(ctx)
    
    def enterStringRelNP(self, ctx: OvernightParser.StringRelNPContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterStringRelNP(ctx)
    
    def exitStringRelNP(self, ctx: OvernightParser.StringRelNPContext):
        ctx.parentCtx.slots["relNP"] = ctx.slots["string"]
        return super().exitStringRelNP(ctx)
    
    def enterNumberRelNP(self, ctx: OvernightParser.NumberRelNPContext):
        ctx.slots = strictDict({"relNP": ""})
        return super().enterNumberRelNP(ctx)
    
    def exitNumberRelNP(self, ctx: OvernightParser.NumberRelNPContext):
        ctx.parentCtx.slots["relNP"] = ctx.slots["relNP"]
        return super().exitNumberRelNP(ctx)
    
    def enterReversePredicate(self, ctx: OvernightParser.ReversePredicateContext):
        ctx.slots = strictDict({"predicate": "", "relNP": ""})
        return super().enterReversePredicate(ctx)
    
    def exitReversePredicate(self, ctx: OvernightParser.ReversePredicateContext):
        if ctx.slots["relNP"] != "":
            ctx.parentCtx.slots["relNP"] = ctx.slots["relNP"]
        else:
            ctx.parentCtx.slots["predicate"] = ctx.slots["predicate"]
        return super().exitReversePredicate(ctx)
    
    def exitString(self, ctx: OvernightParser.StringContext):
        ctx.parentCtx.slots["string"] = str(ctx.getText()).replace("_", " ")
        return super().exitString(ctx)
    
    def exitQuantity(self, ctx: OvernightParser.QuantityContext):
        ctx.parentCtx.slots["quantity"] = str(ctx.getText())
        return super().exitQuantity(ctx)
    
    def exitDate(self, ctx: OvernightParser.DateContext):
        ctx.parentCtx.slots["date"] = str(ctx.getText()).replace("date ", "")
        return super().exitDate(ctx)
    
    def exitTime(self, ctx: OvernightParser.TimeContext):
        ctx.parentCtx.slots["time"] = str(ctx.getText()).replace("time ", "").replace(" ", " : ")
        return super().exitTime(ctx)