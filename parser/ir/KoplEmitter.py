import os
import re
from antlr4 import *

from .UnifiedIRLexer import UnifiedIRLexer
from .UnifiedIRParser import UnifiedIRParser
from .UnifiedIRParserListener import UnifiedIRParserListener

from ..utils import *

class KoplEmitter(UnifiedIRParserListener):
    def __init__(self):
        self.logical_form = ""
        self.SEP = '<b>'
        
        ARG_SEP = '<c>'
        self.func = { 
            "QueryName": "What()",
            "Count": "Count()",
            "QueryRelation": "QueryRelation()",
            "QueryAttr": "QueryAttr(%s)" % ARG_SEP.join(["{}"]*1),
            "QueryAttrUnderCondition": "QueryAttrUnderCondition(%s)" % ARG_SEP.join(["{}"]*3),
            "Population": "FindAll()",
            "And": "And()",
            "Or": "Or()",
            "FilterEntity": "Find(%s)" % ARG_SEP.join(["{}"]*1),
            "FilterRelation": "Relate(%s)" % ARG_SEP.join(["{}"]*2),
            "FilterRank": "Select(%s)" % ARG_SEP.join(["{}"]*4),
            "FilterConcept": "FilterConcept(%s)" % ARG_SEP.join(["{}"]*1),
            "FilterAttrStr": "FilterStr(%s)" % ARG_SEP.join(["{}"]*2),
            "FilterAttrNum": "FilterNum(%s)" % ARG_SEP.join(["{}"]*3),
            "FilterAttrYear": "FilterYear(%s)" % ARG_SEP.join(["{}"]*3),
            "FilterAttrDate": "FilterDate(%s)" % ARG_SEP.join(["{}"]*3),
            "FilterQualifierStr": "QFilterStr(%s)" % ARG_SEP.join(["{}"]*2),
            "FilterQualifierNum": "QFilterNum(%s)" % ARG_SEP.join(["{}"]*3),
            "FilterQualifierYear": "QFilterYear(%s)" % ARG_SEP.join(["{}"]*3),
            "FilterQualifierDate": "QFilterDate(%s)" % ARG_SEP.join(["{}"]*3),
            "VerifyStr": "VerifyStr(%s)" % ARG_SEP.join(["{}"]*1),
            "VerifyNum": "VerifyNum(%s)" % ARG_SEP.join(["{}"]*2),
            "VerifyYear": "VerifyYear(%s)" % ARG_SEP.join(["{}"]*2),
            "VerifyDate": "VerifyDate(%s)" % ARG_SEP.join(["{}"]*2),
            "QueryQualifierAttr": "QueryAttrQualifier(%s)" % ARG_SEP.join(["{}"]*3),
            "QueryQualifierRelation": "QueryRelationQualifier(%s)" % ARG_SEP.join(["{}"]*2)
        }

        self.stringOP_vocab = { 
            "largest": "largest", 
            "smallest": "smallest", 
            "larger": "greater", 
            "smaller": "less"
        }


    def initialize(self):
        self.logical_form = ""

    def get_logical_form(self, ctx):
        return self.logical_form
    
    def enterRoot(self, ctx: UnifiedIRParser.RootContext):
        self.initialize()
        ctx.slots = strictDict({"query": ""})
        return super().enterRoot(ctx)
    
    def exitRoot(self, ctx: UnifiedIRParser.RootContext):
        self.logical_form = ctx.slots["query"]
        return super().exitRoot(ctx)
    
    def enterEntityQuery(self, ctx: UnifiedIRParser.EntityQueryContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterEntityQuery(ctx)
    
    def exitEntityQuery(self, ctx: UnifiedIRParser.EntityQueryContext):
        ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["QueryName"]
        return super().exitEntityQuery(ctx)
    
    def enterAttributeQuery(self, ctx: UnifiedIRParser.AttributeQueryContext):
        ctx.slots = strictDict({"entitySet": "", "attribute": ""})
        return super().enterAttributeQuery(ctx)
    
    def exitAttributeQuery(self, ctx: UnifiedIRParser.AttributeQueryContext):
        ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["QueryAttr"].format(ctx.slots["attribute"])
        return super().exitAttributeQuery(ctx)
    
    def enterPredicateQuery(self, ctx: UnifiedIRParser.PredicateQueryContext):
        ctx.slots = strictDict({"entitySet": []})
        return super().enterPredicateQuery(ctx)
    
    def exitPredicateQuery(self, ctx: UnifiedIRParser.PredicateQueryContext):
        ctx.parentCtx.slots["query"] = ctx.slots["entitySet"][0] + self.SEP + ctx.slots["entitySet"][1] + self.SEP + self.func["QueryRelation"] 
        return super().exitPredicateQuery(ctx)
    
    def enterQualifierQuery(self, ctx: UnifiedIRParser.QualifierQueryContext):
        ctx.slots = strictDict({"entitySet": "", "attribute": "", "value": "", "predicate": "",  "qualifier": ""})
        return super().enterQualifierQuery(ctx)
    
    def exitQualifierQuery(self, ctx: UnifiedIRParser.QualifierQueryContext):
        assert ctx.slots["qualifier"] != ""
        if ctx.slots["attribute"] and ctx.slots["value"] and not ctx.slots["predicate"]:
            ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["QueryQualifierAttr"].format(ctx.slots["attribute"], ctx.slots["value"], ctx.slots["qualifier"])
        elif ctx.slots["predicate"]:
            ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["QueryQualifierRelation"].format(ctx.slots["predicate"], ctx.slots["qualifier"])
        else:
            raise Exception("Unknown qualifier query")
        return super().exitQualifierQuery(ctx)
    
    def enterCountQuery(self, ctx: UnifiedIRParser.CountQueryContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterCountQuery(ctx)
    
    def exitCountQuery(self, ctx: UnifiedIRParser.CountQueryContext):
        ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["Count"]
        return super().exitCountQuery(ctx)
    
    def enterVerifyQuery(self, ctx: UnifiedIRParser.VerifyQueryContext):
        ctx.slots = strictDict({"entitySet": "", "op": "", "valueType": "", "value": ""}) 
        return super().enterVerifyQuery(ctx)
    
    def exitVerifyQuery(self, ctx: UnifiedIRParser.VerifyQueryContext):
        if ctx.slots["valueType"] == "string":
            ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["VerifyStr"].format(ctx.slots["value"])
        elif ctx.slots["valueType"] == "quantity":
            ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["VerifyNum"].format(ctx.slots["value"], ctx.slots["op"])
        elif ctx.slots["valueType"] == "year":
            ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["VerifyYear"].format(ctx.slots["value"], ctx.slots["op"])
        elif ctx.slots["valueType"] == "date":
            ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + self.func["VerifyDate"].format(ctx.slots["value"], ctx.slots["op"])
        else:
            raise Exception("Unknown verify query")
        return super().exitVerifyQuery(ctx)
    
    def enterSelectQuery(self, ctx: UnifiedIRParser.SelectQueryContext):
        ctx.slots = strictDict({"entitySet": "", "rankFilter": ""})
        return super().enterSelectQuery(ctx)
    
    def exitSelectQuery(self, ctx: UnifiedIRParser.SelectQueryContext):
        ctx.parentCtx.slots["query"] = ctx.slots["entitySet"] + self.SEP + ctx.slots["rankFilter"] + self.SEP + self.func["QueryName"]
        return super().exitSelectQuery(ctx)
    
    def enterVerifyByAttribute(self, ctx: UnifiedIRParser.VerifyByAttributeContext):
        if isinstance(ctx.parentCtx, UnifiedIRParser.QualifierQueryContext):
            ctx.slots = strictDict({"entitySet": "", "attribute": "", "value": "", "op": "", "valueType": "", "qualifierFilter": {}})
        elif isinstance(ctx.parentCtx, UnifiedIRParser.VerifyQueryContext):
            ctx.slots = strictDict({"entitySet": "", "attribute": "", "value": "", "op": "", "valueType": "", "qualifierFilter": {}})
        else:
            raise Exception("Unexpected parent context")
        return super().enterVerifyByAttribute(ctx)
    
    def exitVerifyByAttribute(self, ctx: UnifiedIRParser.VerifyByAttributeContext):
        if isinstance(ctx.parentCtx, UnifiedIRParser.QualifierQueryContext):
            insert(ctx.parentCtx, ctx.slots["entitySet"])
            ctx.parentCtx.slots["attribute"] = ctx.slots["attribute"]
            ctx.parentCtx.slots["value"] = ctx.slots["value"]
        elif isinstance(ctx.parentCtx, UnifiedIRParser.VerifyQueryContext):
            if ctx.slots["qualifierFilter"] == {}:
                insert(ctx.parentCtx, ctx.slots["entitySet"] + self.SEP + self.func["QueryAttr"].format(ctx.slots["attribute"]))
            else:
                insert(ctx.parentCtx, ctx.slots["entitySet"] + self.SEP + self.func["QueryAttrUnderCondition"].format(ctx.slots["attribute"], ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"]))
            ctx.parentCtx.slots["value"] = ctx.slots["value"]
            ctx.parentCtx.slots["op"] = ctx.slots["op"]
            ctx.parentCtx.slots["valueType"] = ctx.slots["valueType"]
        return super().exitVerifyByAttribute(ctx)

    def enterVerifyByPredicate(self, ctx: UnifiedIRParser.VerifyByPredicateContext):
        if isinstance(ctx.parentCtx, UnifiedIRParser.QualifierQueryContext):
            ctx.slots = strictDict({"entitySet": [], "predicate": "", "qualifierFilter": ""})
        else:
            raise Exception("Unexpected parent context")
        return super().enterVerifyByPredicate(ctx)
    
    def exitVerifyByPredicate(self, ctx: UnifiedIRParser.VerifyByPredicateContext):
        if isinstance(ctx.parentCtx, UnifiedIRParser.QualifierQueryContext):
            insert(ctx.parentCtx, ctx.slots["entitySet"][0] + self.SEP + ctx.slots["entitySet"][1])
            ctx.parentCtx.slots["predicate"] = ctx.slots["predicate"]
        else:
            raise Exception("Unexpected parent context")
        return super().exitVerifyByPredicate(ctx)
    
    def enterEntitySetGroup(self, ctx: UnifiedIRParser.EntitySetGroupContext):
        ctx.slots = strictDict({"entitySet": [], "setOP": ""})
        return super().enterEntitySetGroup(ctx)

    def exitEntitySetGroup(self, ctx: UnifiedIRParser.EntitySetGroupContext):
        assert isinstance(ctx.slots["entitySet"], list) and len(ctx.slots["entitySet"]) == 2
        if ctx.slots["setOP"] == "and":
            insert(ctx.parentCtx, ctx.slots["entitySet"][0] + self.SEP + ctx.slots["entitySet"][1] + self.SEP + self.func["And"])
        elif ctx.slots["setOP"] == "or":
            insert(ctx.parentCtx, ctx.slots["entitySet"][0] + self.SEP + ctx.slots["entitySet"][1] + self.SEP + self.func["Or"])
        else:
            raise Exception("Unexpected set operator")
        return super().exitEntitySetGroup(ctx)    
    
    def enterEntitySetIntersect(self, ctx: UnifiedIRParser.EntitySetIntersectContext):
        ctx.slots = strictDict({"entitySet": []})
        return super().enterEntitySetIntersect(ctx)
    
    def exitEntitySetIntersect(self, ctx: UnifiedIRParser.EntitySetIntersectContext):
        assert isinstance(ctx.slots["entitySet"], list) and len(ctx.slots["entitySet"]) == 2
        if ctx.slots["entitySet"][0].is_pop:
            insert(ctx.parentCtx, ctx.slots["entitySet"][1])
        elif ctx.slots["entitySet"][1].is_pop:
            insert(ctx.parentCtx, ctx.slots["entitySet"][0])
        else:
            insert(ctx.parentCtx, ctx.slots["entitySet"][1] + self.SEP + ctx.slots["entitySet"][0] + self.SEP + self.func["And"])
        return super().exitEntitySetIntersect(ctx)

    def enterEntitySetFilter(self, ctx: UnifiedIRParser.EntitySetFilterContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterEntitySetFilter(ctx)
    
    def exitEntitySetFilter(self, ctx: UnifiedIRParser.EntitySetFilterContext):
        insert(ctx.parentCtx, ctx.slots["entitySet"])
        return super().exitEntitySetFilter(ctx)

    def enterEntitySetAtom(self, ctx: UnifiedIRParser.EntitySetAtomContext):
        ctx.slots = strictDict({"entity": ""})
        return super().enterEntitySetAtom(ctx)

    def exitEntitySetAtom(self, ctx: UnifiedIRParser.EntitySetAtomContext):
        insert(ctx.parentCtx, self.func["FilterEntity"].format(ctx.slots["entity"]), is_atom=True)
        return super().exitEntitySetAtom(ctx)
    
    def exitEntitySetPlaceholder(self, ctx: UnifiedIRParser.EntitySetPlaceholderContext):
        insert(ctx.parentCtx, self.func["Population"], is_pop=True)
        return super().exitEntitySetPlaceholder(ctx)
    
    def enterEntitySetByAttribute(self, ctx: UnifiedIRParser.EntitySetByAttributeContext):
        ctx.slots = strictDict({"concept": "", "entitySet": "", "attributeFilter": "", "qualifierFilter": ""})
        return super().enterEntitySetByAttribute(ctx)
    
    def exitEntitySetByAttribute(self, ctx: UnifiedIRParser.EntitySetByAttributeContext):
        assert ctx.slots["attributeFilter"] != ""
        if not ctx.slots["entitySet"]:
            ctx.slots["entitySet"] = entitySet(self.func["Population"], is_pop=True)
        subquery = ctx.slots["entitySet"]
        subquery += self.SEP + ctx.slots["attributeFilter"]
        if ctx.slots["qualifierFilter"]:
            subquery += self.SEP + ctx.slots["qualifierFilter"]
        if ctx.slots["concept"]:
            subquery += self.SEP + self.func["FilterConcept"].format(ctx.slots["concept"])
        insert(ctx.parentCtx, subquery)
        return super().exitEntitySetByAttribute(ctx)
    
    def enterFilterByAttribute(self, ctx: UnifiedIRParser.FilterByAttributeContext):
        ctx.slots = strictDict({"attribute": "", "op": "", "value": "", "valueType": ""})
        return super().enterFilterByAttribute(ctx)
    
    def exitFilterByAttribute(self, ctx: UnifiedIRParser.FilterByAttributeContext):
        if isinstance(ctx.parentCtx, UnifiedIRParser.VerifyByAttributeContext):
            ctx.parentCtx.slots["attribute"] = ctx.slots["attribute"]
            ctx.parentCtx.slots["op"] = ctx.slots["op"]
            ctx.parentCtx.slots["value"] = ctx.slots["value"]
            ctx.parentCtx.slots["valueType"] = ctx.slots["valueType"]
        else:
            if ctx.slots["valueType"] == "string":
                ctx.parentCtx.slots["attributeFilter"] = self.func["FilterAttrStr"].format(ctx.slots["attribute"], ctx.slots["value"])
            elif ctx.slots["valueType"] == "quantity":
                ctx.parentCtx.slots["attributeFilter"] = self.func["FilterAttrNum"].format(ctx.slots["attribute"], ctx.slots["value"], ctx.slots["op"])
            elif ctx.slots["valueType"] == "year":
                ctx.parentCtx.slots["attributeFilter"] = self.func["FilterAttrYear"].format(ctx.slots["attribute"], ctx.slots["value"], ctx.slots["op"])
            elif ctx.slots["valueType"] == "date":
                ctx.parentCtx.slots["attributeFilter"] = self.func["FilterAttrDate"].format(ctx.slots["attribute"], ctx.slots["value"], ctx.slots["op"])
            else:
                raise Exception("Unexpected value type")
        return super().exitFilterByAttribute(ctx)
    
    def enterEntitySetByPredicate(self, ctx: UnifiedIRParser.EntitySetByPredicateContext):
        ctx.slots = strictDict({"concept": "", "entitySet": [], "predicateFilter": "", "qualifierFilter": ""})
        return super().enterEntitySetByPredicate(ctx)
    
    def exitEntitySetByPredicate(self, ctx: UnifiedIRParser.EntitySetByPredicateContext):
        assert ctx.slots["predicateFilter"] != ""
        if len(ctx.slots["entitySet"]) == 1:
            subquery = ctx.slots["entitySet"][0] + self.SEP + ctx.slots["predicateFilter"]
        elif ctx.slots["entitySet"][0].is_pop:
            subquery = ctx.slots["entitySet"][1] + self.SEP + ctx.slots["predicateFilter"]
        else:
            subquery = ctx.slots["entitySet"][1] + self.SEP + ctx.slots["predicateFilter"] + self.SEP + ctx.slots["entitySet"][0] 
        if ctx.slots["qualifierFilter"]:
            subquery += self.SEP + ctx.slots["qualifierFilter"]
        if ctx.slots["concept"]:
            subquery += self.SEP + self.func["FilterConcept"].format(ctx.slots["concept"])
        insert(ctx.parentCtx, subquery)
        return super().exitEntitySetByPredicate(ctx)
    
    def enterFilterByPredicate(self, ctx: UnifiedIRParser.FilterByPredicateContext):
        ctx.slots = strictDict({"predicate": "", "direction": "forward"})
        return super().enterFilterByPredicate(ctx)
    
    def exitFilterByPredicate(self, ctx: UnifiedIRParser.FilterByPredicateContext):
        if isinstance(ctx.parentCtx, UnifiedIRParser.VerifyByPredicateContext):
            ctx.parentCtx.slots["predicate"] = ctx.slots["predicate"]
        else:
            ctx.parentCtx.slots["predicateFilter"] = self.func["FilterRelation"].format(ctx.slots["predicate"], ctx.slots["direction"])
        return super().exitFilterByPredicate(ctx)
    
    def enterFilterByQualifier(self, ctx: UnifiedIRParser.FilterByQualifierContext):
        ctx.slots = strictDict({"qualifier": "", "op": "", "value": "", "valueType": ""})
        return super().enterFilterByQualifier(ctx)
    
    def exitFilterByQualifier(self, ctx: UnifiedIRParser.FilterByQualifierContext):
        if isinstance(ctx.parentCtx, UnifiedIRParser.VerifyByAttributeContext):
            ctx.parentCtx.slots["qualifierFilter"]["qualifier"] = ctx.slots["qualifier"]
            ctx.parentCtx.slots["qualifierFilter"]["op"] = ctx.slots["op"]
            ctx.parentCtx.slots["qualifierFilter"]["value"] = ctx.slots["value"]
            ctx.parentCtx.slots["qualifierFilter"]["valueType"] = ctx.slots["valueType"]
        else:
            if ctx.slots["valueType"] == "string":
                ctx.parentCtx.slots["qualifierFilter"] = self.func["FilterQualifierStr"].format(ctx.slots["qualifier"], ctx.slots["value"])
            elif ctx.slots["valueType"] == "quantity":
                ctx.parentCtx.slots["qualifierFilter"] = self.func["FilterQualifierNum"].format(ctx.slots["qualifier"], ctx.slots["value"], ctx.slots["op"])
            elif ctx.slots["valueType"] == "year":
                ctx.parentCtx.slots["qualifierFilter"] = self.func["FilterQualifierYear"].format(ctx.slots["qualifier"], ctx.slots["value"], ctx.slots["op"])
            elif ctx.slots["valueType"] == "date":
                ctx.parentCtx.slots["qualifierFilter"] = self.func["FilterQualifierDate"].format(ctx.slots["qualifier"], ctx.slots["value"], ctx.slots["op"])
            else:
                raise Exception("Unexpected value type")
        return super().exitFilterByQualifier(ctx)
    
    def enterEntitySetByConcept(self, ctx: UnifiedIRParser.EntitySetByConceptContext):
        ctx.slots = strictDict({"entitySet": "", "concept": ""})
        return super().enterEntitySetByConcept(ctx)
    
    def exitEntitySetByConcept(self, ctx: UnifiedIRParser.EntitySetByConceptContext):
        if ctx.slots["entitySet"] == "":
            insert(ctx.parentCtx, self.func["Population"] + self.SEP + self.func["FilterConcept"].format(ctx.slots["concept"]))
        else:
            insert(ctx.parentCtx, ctx.slots["entitySet"] + self.SEP + self.func["FilterConcept"].format(ctx.slots["concept"]))
        return super().exitEntitySetByConcept(ctx)
    
    def enterEntitySetByRank(self, ctx: UnifiedIRParser.EntitySetByRankContext):
        ctx.slots = strictDict({"entitySet": "", "rankFilter": ""})
        return super().enterEntitySetByRank(ctx)
    
    def exitEntitySetByRank(self, ctx: UnifiedIRParser.EntitySetByRankContext):
        assert ctx.slots["rankFilter"] != ""
        insert(ctx.parentCtx, ctx.slots["entitySet"] + self.SEP + ctx.slots["rankFilter"])
        return super().exitEntitySetByRank(ctx)
    
    def enterFilterByRank(self, ctx: UnifiedIRParser.FilterByRankContext):
        ctx.slots = strictDict({"attribute": "", "stringOP": "", "number": 1})
        return super().enterFilterByRank(ctx)
    
    def exitFilterByRank(self, ctx: UnifiedIRParser.FilterByRankContext):
        ctx.parentCtx.slots["rankFilter"] = self.func["FilterRank"].format(ctx.slots["attribute"], ctx.slots["stringOP"], ctx.slots["number"], 0)
        return super().exitFilterByRank(ctx)
    
    def enterValueAtom(self, ctx: UnifiedIRParser.ValueAtomContext):
        ctx.slots = strictDict({"valueType": "", "value": ""})
        return super().enterValueAtom(ctx)
    
    def exitValueAtom(self, ctx: UnifiedIRParser.ValueAtomContext):
        ctx.parentCtx.slots["valueType"] = ctx.slots["valueType"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        return super().exitValueAtom(ctx)

    def enterEntity(self, ctx: UnifiedIRParser.EntityContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterEntity(ctx)
    
    def exitEntity(self, ctx: UnifiedIRParser.EntityContext):
        ctx.parentCtx.slots["entity"] = ctx.slots["string"]
        return super().exitEntity(ctx)
    
    def enterAttribute(self, ctx: UnifiedIRParser.AttributeContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterAttribute(ctx)
    
    def exitAttribute(self, ctx: UnifiedIRParser.AttributeContext):
        ctx.parentCtx.slots["attribute"] = ctx.slots["string"]
        return super().exitAttribute(ctx)
    
    def enterConcept(self, ctx: UnifiedIRParser.ConceptContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterConcept(ctx)
    
    def exitConcept(self, ctx: UnifiedIRParser.ConceptContext):
        ctx.parentCtx.slots["concept"] = ctx.slots["string"]
        return super().exitConcept(ctx)
    
    def enterPredicate(self, ctx: UnifiedIRParser.PredicateContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterPredicate(ctx)
    
    def exitPredicate(self, ctx: UnifiedIRParser.PredicateContext):
        ctx.parentCtx.slots["predicate"] = ctx.slots["string"]
        return super().exitPredicate(ctx)
    
    def enterQualifier(self, ctx: UnifiedIRParser.QualifierContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterQualifier(ctx)
    
    def exitQualifier(self, ctx: UnifiedIRParser.QualifierContext):
        ctx.parentCtx.slots["qualifier"] = ctx.slots["string"]
        return super().exitQualifier(ctx)
    
    def enterValue(self, ctx: UnifiedIRParser.ValueContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterValue(ctx)
    
    def exitValue(self, ctx: UnifiedIRParser.ValueContext):
        ctx.parentCtx.slots["value"] = ctx.slots["string"]
        return super().exitValue(ctx)
    

    def exitForward(self, ctx: UnifiedIRParser.ForwardContext):
        ctx.parentCtx.slots["direction"] = "forward"
        return super().exitForward(ctx)
    
    def exitBackward(self, ctx: UnifiedIRParser.BackwardContext):
        ctx.parentCtx.slots["direction"] = "backward"
        return super().exitBackward(ctx)
    
    def exitAnd(self, ctx: UnifiedIRParser.AndContext):
        ctx.parentCtx.slots["setOP"] = "and"
        return super().exitAnd(ctx)
    
    def exitOr(self, ctx: UnifiedIRParser.OrContext):
        ctx.parentCtx.slots["setOP"] = "or"
        return super().exitOr(ctx)

    def exitEqual(self, ctx: UnifiedIRParser.EqualContext):
        ctx.parentCtx.slots["op"] = "="
        return super().exitEqual(ctx)
    
    def exitNotEqual(self, ctx: UnifiedIRParser.NotEqualContext):
        ctx.parentCtx.slots["op"] = "!="
        return super().exitNotEqual(ctx)
    
    def exitLarger(self, ctx: UnifiedIRParser.LargerContext):
        ctx.parentCtx.slots["op"] = ">"
        return super().exitLarger(ctx)
    
    def exitSmaller(self, ctx: UnifiedIRParser.SmallerContext):
        ctx.parentCtx.slots["op"] = "<"
        return super().exitSmaller(ctx)
    
    def exitLargerEqual(self, ctx: UnifiedIRParser.LargerEqualContext):
        ctx.parentCtx.slots["op"] = ">="
        return super().exitLargerEqual(ctx)
    
    def exitSmallerEqual(self, ctx: UnifiedIRParser.SmallerEqualContext):
        ctx.parentCtx.slots["op"] = "<="
        return super().exitSmallerEqual(ctx)
    
    def exitText(self, ctx: UnifiedIRParser.TextContext):
        ctx.parentCtx.slots["valueType"] = "string"
        return super().exitText(ctx)
    
    def exitQuantity(self, ctx: UnifiedIRParser.QuantityContext):
        ctx.parentCtx.slots["valueType"] = "quantity"
        return super().exitQuantity(ctx)

    def exitDate(self, ctx: UnifiedIRParser.DateContext):
        ctx.parentCtx.slots["valueType"] = "date"
        return super().exitDate(ctx)
    
    def exitYear(self, ctx: UnifiedIRParser.YearContext):
        ctx.parentCtx.slots["valueType"] = "year"
        return super().exitYear(ctx)
    
    def exitLargest(self, ctx: UnifiedIRParser.LargestContext):
        ctx.parentCtx.slots["stringOP"] = self.stringOP_vocab["largest"]
        return super().enterLargest(ctx)
    
    def exitSmallest(self, ctx: UnifiedIRParser.SmallestContext):
        ctx.parentCtx.slots["stringOP"] = self.stringOP_vocab["smallest"]
        return super().exitSmallest(ctx)

    # def enterTopK(self, ctx: UnifiedIRParser.TopKContext):
    #     ctx.slots = strictDict({"number": 1})
    #     return super().enterTopK(ctx)

    # def exitTopK(self, ctx: UnifiedIRParser.TopKContext):
    #     ctx.parentCtx.parentCtx.slots["limit"] = ctx.slots["number"]
    #     return super().exitTopK(ctx)    

    def enterString(self, ctx: UnifiedIRParser.StringContext):
        if not isinstance(ctx.parentCtx, UnifiedIRParser.StringContext):
            ctx.parentCtx.slots["string"] = str(ctx.getText())

    def enterNumber(self, ctx: UnifiedIRParser.NumberContext):
        if not isinstance(ctx.parentCtx, UnifiedIRParser.NumberContext):
            ctx.parentCtx.slots["number"] = str(ctx.getText())
