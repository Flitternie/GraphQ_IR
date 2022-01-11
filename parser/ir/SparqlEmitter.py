import os
import re
from antlr4 import *

from .UnifiedIRLexer import UnifiedIRLexer
from .UnifiedIRParser import UnifiedIRParser
from .UnifiedIRParserListener import UnifiedIRParserListener

from bart2query.program.executor_rule_new import RuleExecutor

from .misc import *

class strictDict(dict):
    def __setitem__(self, key, value):
        if key not in self:
            raise KeyError("{} is not a legal key of this strictDict".format(repr(key)))
        dict.__setitem__(self, key, value)

class entitySet():
    def __init__(self, value="", concept=""):
        self.value = str(value)
        self.concept = concept
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
    
    def __len__(self):
        return len(self.value)

# class entitySet(str):
#     def __new__(self, value="", concept=""):
#         self.concept = concept
#         return str.__new__(self, value)

class SparqlEmitter(UnifiedIRParserListener):
    def __init__(self):
        self.sparql = ""
        self.rule_executor = RuleExecutor(os.path.join("./data/kqapro/dataset_new/", 'kb.json'))
        self.vars = {  
            "e": [],
            "c": [],
            "pv": [],
            "v": []
        }
        self.ambiguous_qualifiers = [
            "point in time", 
            "inception", 
            "start time",
            "end time",
            "dissolved, abolished or demolished",
            "work period (start)",
            "public domain date", 
            "publication date",
            "date of birth",
            "date of death"
        ]

        self.skeleton = {
            "entityQuery": "SELECT DISTINCT ?e WHERE {{ {} }}",
            "attributeQuery": "SELECT DISTINCT ?pv WHERE {{ {} }}",
            "predicateQuery": "SELECT DISTINCT ?p WHERE {{ {} }}",
            "qualifierQuery": "SELECT DISTINCT ?qpv WHERE {{ {} }}",
            "countQuery": "SELECT (COUNT(DISTINCT ?e) AS ?count) WHERE {{ {} }}",
            "verifyQuery": "ASK {{ {} }}",
            "selectQuery": "SELECT ?e WHERE {{ {} }} ORDER BY {} LIMIT {}"
        }

    
    def initialize(self):
        self.sparql = ""
        self.vars = {}.fromkeys(self.vars, 0)

    def getSPARQL(self, ctx):
        return self.sparql

    def insertEntitySet(self, ctx, value, concept=None):
        if isinstance(ctx.slots["entitySet"], list):
            ctx.slots["entitySet"].append(entitySet(value, concept))
        else: 
            ctx.slots["entitySet"] = entitySet(value, concept)
    
    def getValueType(self, key, value=None):
        try:
            v_type = self.rule_executor.key_type[key]
            if key in self.ambiguous_qualifiers and v_type == "date" and re.match(r"-?[0-9]{3,4}(?!.)", value):
                return "year"
            return v_type
        except:
            return "string"
    
    def getValueUnit(self, value, value_type):
        if value_type == "quantity":
            if ' ' in value:
                vs = value.split()
                value = vs[0]
                unit = ' '.join(vs[1:])
            else:
                unit = '1'
        else:
            unit = None
        return value, unit

    # def mergeSubqueries(self, subqueries):
    #     subqueries = [" ".join(i) for i in subqueries]
    #     return " . ".join(subqueries)

    
    def enterQuery(self, ctx:UnifiedIRParser.QueryContext):
        self.initialize()
        ctx.slots = strictDict({"sparql": ""})
        return super().enterQuery(ctx)
    
    def exitQuery(self, ctx: UnifiedIRParser.QueryContext):
        self.sparql = ctx.slots["sparql"]
        return super().exitQuery(ctx)
    
    def enterEntityQuery(self, ctx: UnifiedIRParser.EntityQueryContext):
        ctx.slots = strictDict({"entitySet": entitySet()})
        return super().enterEntityQuery(ctx)
    
    def exitEntityQuery(self, ctx: UnifiedIRParser.EntityQueryContext):
        subqueries = ctx.slots["entitySet"]
        ctx.parentCtx.slots["sparql"] = self.skeleton["entityQuery"].format(subqueries)
        return super().exitEntityQuery(ctx)
    
    def enterAttributeQuery(self, ctx: UnifiedIRParser.AttributeQueryContext):
        ctx.slots = strictDict({"attribute": "", "entitySet": entitySet()})
        return super().enterAttributeQuery(ctx)
    
    def exitAttributeQuery(self, ctx: UnifiedIRParser.AttributeQueryContext):
        subqueries = append_attribute_value_query(ctx.slots["entitySet"], ctx.slots["attribute"])
        ctx.parentCtx.slots["sparql"] = self.skeleton["attributeQuery"].format(subqueries)
        return super().exitAttributeQuery(ctx)
    
    def enterPredicateQuery(self, ctx: UnifiedIRParser.PredicateQueryContext):
        ctx.slots = strictDict({"entitySet": []})
        return super().enterPredicateQuery(ctx)
    
    def exitPredicateQuery(self, ctx: UnifiedIRParser.PredicateQueryContext):
        # ctx.slots["entitySet"][0], ctx.slots["entitySet"][1] = replace_duplicate_variables(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1], same_sub=False)
        # subqueries = ctx.slots["entitySet"][0] + ctx.slots["entitySet"][1] + '?e_1 ?p ?e_2 . '
        subqueries = gen_relation_query(sbj_sparql=ctx.slots["entitySet"][0], sbj_variable='?e_1', obj_sparql=ctx.slots["entitySet"][1], obj_variable='?e_2')
        ctx.parentCtx.slots["sparql"] = self.skeleton["predicateQuery"].format(subqueries)
        return super().exitPredicateQuery(ctx)
    
    def enterQualifierQuery(self, ctx: UnifiedIRParser.QualifierQueryContext):
        ctx.slots = strictDict({"qualifier": "", "verify": "", "factNode": ""})
        return super().enterQualifierQuery(ctx)
    
    def exitQualifierQuery(self, ctx: UnifiedIRParser.QualifierQueryContext):
        subqueries = append_attribute_value_query(ctx.slots["verify"], ctx.slots["qualifier"], e=ctx.slots["factNode"], in_qualifier=True)
        ctx.parentCtx.slots["sparql"] = self.skeleton["qualifierQuery"].format(subqueries)
        return super().exitQualifierQuery(ctx)
    
    def enterCountQuery(self, ctx: UnifiedIRParser.CountQueryContext):
        ctx.slots = strictDict({"entitySet": entitySet()})
        return super().enterCountQuery(ctx)
    
    def exitCountQuery(self, ctx: UnifiedIRParser.CountQueryContext):
        subqueries = ctx.slots["entitySet"]
        ctx.parentCtx.slots["sparql"] = self.skeleton["countQuery"].format(subqueries)
        return super().exitCountQuery(ctx)
    
    def enterVerifyQuery(self, ctx: UnifiedIRParser.VerifyQueryContext):
        ctx.slots = strictDict({"verify": ""})
        return super().enterVerifyQuery(ctx)
    
    def exitVerifyQuery(self, ctx: UnifiedIRParser.VerifyQueryContext):
        subqueries = ctx.slots["verify"]
        ctx.parentCtx.slots["sparql"] = self.skeleton["verifyQuery"].format(subqueries)
        return super().exitVerifyQuery(ctx)
    
    def enterSelectQuery(self, ctx: UnifiedIRParser.SelectQueryContext):
        ctx.slots = strictDict({"entitySet": entitySet(), "attribute": "", "orderBy": "", "number": ""})
        return super().enterSelectQuery(ctx)
    
    def exitSelectQuery(self, ctx: UnifiedIRParser.SelectQueryContext):
        subqueries = append_attribute_value_query(ctx.slots["entitySet"], ctx.slots["attribute"], 'quantity')
        ctx.parentCtx.slots["sparql"] = self.skeleton["selectQuery"].format(subqueries, ctx.slots["orderBy"].format('?v'), ctx.slots["number"])
        return super().exitSelectQuery(ctx)

    

    def enterVerifyByAttribute(self, ctx: UnifiedIRParser.VerifyByAttributeContext):
        ctx.slots = strictDict({"entitySet": entitySet(), "attribute": "", "op": "=", "valueType": "", "value": "", "qualifierFilter": {}})
        return super().enterVerifyByAttribute(ctx)
    
    def exitVerifyByAttribute(self, ctx: UnifiedIRParser.VerifyByAttributeContext):
        ctx.slots["valueType"] = ctx.slots["valueType"] if ctx.slots["valueType"] != "" else self.getValueType(ctx.slots["attribute"], ctx.slots["value"])
        ctx.slots["value"], v_unit = self.getValueUnit(ctx.slots["value"], ctx.slots["valueType"])

        subqueries = ctx.slots["entitySet"]
        subqueries, _ = replace_variable(subqueries, '?pv')
        subqueries, _ = replace_variable(subqueries, '?v')
        
        subqueries += gen_attribute_query(ctx.slots["attribute"], ctx.slots["value"], ctx.slots["valueType"], v_unit, ctx.slots["op"])
        fact_node = gen_attr_fact_node(ctx.slots["attribute"])
        
        if isinstance(ctx.parentCtx, UnifiedIRParser.QualifierQueryContext):
            ctx.parentCtx.slots["verify"] = subqueries
            ctx.parentCtx.slots["factNode"] = fact_node
        elif isinstance(ctx.parentCtx, UnifiedIRParser.VerifyQueryContext):
            if ctx.slots["qualifierFilter"] != {}:
                subqueries, _ = replace_variable(subqueries, '?qpv')
                subqueries, _ = replace_variable(subqueries, '?qv')
                ctx.slots["qualifierFilter"]["valueType"] = ctx.slots["qualifierFilter"]["valueType"] if ctx.slots["qualifierFilter"]["valueType"] != "" else self.getValueType(ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"])
                ctx.slots["qualifierFilter"]["value"], qv_unit = self.getValueUnit(ctx.slots["qualifierFilter"]["value"], ctx.slots["qualifierFilter"]["valueType"])
                subqueries += gen_attribute_query(ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"], ctx.slots["qualifierFilter"]["valueType"], qv_unit, ctx.slots["qualifierFilter"]["op"], e=fact_node, in_qualifier=True)
            ctx.parentCtx.slots["verify"] = subqueries
        else:
            raise Exception("Unexpected context")
        
        return super().exitVerifyByAttribute(ctx)

    def enterVerifyByPredicate(self, ctx: UnifiedIRParser.VerifyByPredicateContext):
        ctx.slots = strictDict({"entitySet": [], "predicate": "", "direction": "", "qualifierFilter": {}})
        return super().enterVerifyByPredicate(ctx)

    def exitVerifyByPredicate(self, ctx: UnifiedIRParser.VerifyByPredicateContext):
        ctx.slots["direction"] = reverse_dir(ctx.slots["direction"]) if ctx.slots["direction"] != "" else "forward"

        # ctx.slots["entitySet"][0], ctx.slots["entitySet"][1] = replace_duplicate_variables(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1], same_sub=False)
        # ctx.parentCtx.slots["verify"] = ctx.slots["entitySet"][0] + ctx.slots["entitySet"][1] + '?e_1 <{}> ?e_2 . '.format(legal(ctx.slots["predicate"]))
        subqueries = gen_relation_query(sbj_sparql=ctx.slots["entitySet"][0], sbj_variable='?e_1', obj_sparql=ctx.slots["entitySet"][1], obj_variable='?e_2', pred=ctx.slots["predicate"], direction=ctx.slots["direction"])
        fact_node = gen_rel_fact_node(ctx.slots["predicate"], ctx.slots["direction"], '?e_1', '?e_2')
        
        if isinstance(ctx.parentCtx, UnifiedIRParser.QualifierQueryContext):
            ctx.parentCtx.slots["verify"] = subqueries
            ctx.parentCtx.slots["factNode"] = fact_node
        elif isinstance(ctx.parentCtx, UnifiedIRParser.VerifyQueryContext):
            if ctx.slots["qualifierFilter"] != {}:
                subqueries, _ = replace_variable(subqueries, '?qpv')
                subqueries, _ = replace_variable(subqueries, '?qv')
                ctx.slots["qualifierFilter"]["valueType"] = ctx.slots["qualifierFilter"]["valueType"] if ctx.slots["qualifierFilter"]["valueType"] != "" else self.getValueType(ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"])        
                ctx.slots["qualifierFilter"]["value"], qv_unit = self.getValueUnit(ctx.slots["qualifierFilter"]["value"], ctx.slots["qualifierFilter"]["valueType"])
                subqueries += gen_attribute_query(ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"], ctx.slots["qualifierFilter"]["valueType"], qv_unit, ctx.slots["qualifierFilter"]["op"], e=fact_node, in_qualifier=True)
            ctx.parentCtx.slots["verify"] = subqueries
        else:
            raise Exception("Unexpected context")
        
        return super().exitVerifyByPredicate(ctx)


    def enterEntitySetGroup(self, ctx: UnifiedIRParser.EntitySetGroupContext):
        ctx.slots = strictDict({"entitySet": [], "setOP": ""})
        return super().enterEntitySetGroup(ctx)
    
    def exitEntitySetGroup(self, ctx: UnifiedIRParser.EntitySetGroupContext):
        assert isinstance(ctx.slots["entitySet"], list) and len(ctx.slots["entitySet"]) == 2
        if ctx.slots["setOP"] == "and":
            self.insertEntitySet(ctx.parentCtx, and_two_descriptions(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1], same_concept(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1])))
        elif ctx.slots["setOP"] == "or":
            self.insertEntitySet(ctx.parentCtx, or_two_descriptions(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1], same_concept(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1])))
        else:
            raise Exception("Unexpected set operator")
        return super().exitEntitySetGroup(ctx)
    
    def enterEntitySetIntersect(self, ctx: UnifiedIRParser.EntitySetIntersectContext):
        ctx.slots = strictDict({"entitySet": []})
        return super().enterEntitySetIntersect(ctx)
    
    def exitEntitySetIntersect(self, ctx: UnifiedIRParser.EntitySetIntersectContext):
        assert isinstance(ctx.slots["entitySet"], list) and len(ctx.slots["entitySet"]) == 2
        self.insertEntitySet(ctx.parentCtx, and_two_descriptions(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1], same_concept(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1])))
        return super().exitEntitySetIntersect(ctx)
    
    def enterEntitySetFilter(self, ctx: UnifiedIRParser.EntitySetFilterContext):
        ctx.slots = strictDict({"entitySet": entitySet()})
        return super().enterEntitySetFilter(ctx)
    
    def exitEntitySetFilter(self, ctx: UnifiedIRParser.EntitySetFilterContext):
        self.insertEntitySet(ctx.parentCtx, ctx.slots["entitySet"], ctx.slots["entitySet"].concept)
        return super().exitEntitySetFilter(ctx)
    
    def enterEntitySetPlaceholder(self, ctx: UnifiedIRParser.EntitySetPlaceholderContext):
        return super().enterEntitySetPlaceholder(ctx)
    
    def exitEntitySetPlaceholder(self, ctx: UnifiedIRParser.EntitySetPlaceholderContext):
        return super().exitEntitySetPlaceholder(ctx)

    def enterEntitySetAtom(self, ctx: UnifiedIRParser.EntitySetAtomContext):
        ctx.slots = strictDict({"entity": ""})
        return super().enterEntitySetAtom(ctx)
    
    def exitEntitySetAtom(self, ctx: UnifiedIRParser.EntitySetAtomContext):
        self.insertEntitySet(ctx.parentCtx, gen_name_query(ctx.slots["entity"]))
        return super().exitEntitySetAtom(ctx)


    
    def enterEntitySetByAttribute(self, ctx: UnifiedIRParser.EntitySetByAttributeContext):
        ctx.slots = strictDict({"concept": "", "entitySet": entitySet(), "attribute": "", "op": "", "valueType": "", "value": "", "qualifierFilter": {}})
        return super().enterEntitySetByAttribute(ctx)
    
    def exitEntitySetByAttribute(self, ctx: UnifiedIRParser.EntitySetByAttributeContext):
        ctx.slots["valueType"] = ctx.slots["valueType"] if ctx.slots["valueType"] != "" else self.getValueType(ctx.slots["attribute"], ctx.slots["value"])
        ctx.slots["value"], v_unit = self.getValueUnit(ctx.slots["value"], ctx.slots["valueType"])

        subqueries = gen_concept_query(ctx.slots["concept"]) if ctx.slots["concept"] != "" else ""
        subqueries += gen_attribute_query(ctx.slots["attribute"], ctx.slots["value"], ctx.slots["valueType"], v_unit, ctx.slots["op"])

        if ctx.slots["qualifierFilter"] != {}:
            fact_node = gen_attr_fact_node(ctx.slots["attribute"])
            ctx.slots["qualifierFilter"]["valueType"] = ctx.slots["qualifierFilter"]["valueType"] if ctx.slots["qualifierFilter"]["valueType"] != "" else self.getValueType(ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"])       
            ctx.slots["qualifierFilter"]["value"], qv_unit = self.getValueUnit(ctx.slots["qualifierFilter"]["value"], ctx.slots["qualifierFilter"]["valueType"])
            subqueries += gen_attribute_query(ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"], ctx.slots["qualifierFilter"]["valueType"], qv_unit, ctx.slots["qualifierFilter"]["op"], e=fact_node, in_qualifier=True)

        if ctx.slots["entitySet"]:
            self.insertEntitySet(ctx.parentCtx, and_two_descriptions(ctx.slots["entitySet"], subqueries, same_concept(ctx.slots["concept"], ctx.slots["entitySet"])), ctx.slots["concept"])
        else:
            self.insertEntitySet(ctx.parentCtx, subqueries, ctx.slots["concept"])
        return super().exitEntitySetByAttribute(ctx)
    
    def enterEntitySetByPredicate(self, ctx: UnifiedIRParser.EntitySetByPredicateContext):
        ctx.slots = strictDict({"concept": "", "entitySet": [], "predicate": "", "direction": "", "qualifierFilter": {}})
        return super().enterEntitySetByPredicate(ctx)
    
    def exitEntitySetByPredicate(self, ctx: UnifiedIRParser.EntitySetByPredicateContext):
        ctx.slots["direction"] = reverse_dir(ctx.slots["direction"]) if ctx.slots["direction"] != "" else "forward"        
        subqueries = gen_concept_query(ctx.slots["concept"]) if ctx.slots["concept"] != "" else ""
        
        if len(ctx.slots["entitySet"]) == 2:
            if diff_concept(ctx.slots["entitySet"][0], ctx.slots["entitySet"][1]):
                ctx.slots["entitySet"][1] = replace_variable(ctx.slots["entitySet"][1], "?c")
            sbj_variable, obj_variable = '?e_1', '?e_2'
            # ctx.slots["entitySet"][1], obj_variable = replace_variable(ctx.slots["entitySet"][1], "?e")
            subqueries += gen_relation_query(sbj_sparql=ctx.slots["entitySet"][0], sbj_variable=sbj_variable, obj_sparql=ctx.slots["entitySet"][1], obj_variable=obj_variable, pred=ctx.slots["predicate"], direction=ctx.slots["direction"])
        elif len(ctx.slots["entitySet"]) == 1:
            if diff_concept(ctx.slots["concept"], ctx.slots["entitySet"][0]):
                ctx.slots["entitySet"][0], _ = replace_variable(ctx.slots["entitySet"][0], "?c")
            sbj_variable = '?e'
            ctx.slots["entitySet"][0], obj_variable = replace_variable(ctx.slots["entitySet"][0], "?e")
            subqueries += gen_relation_query(sbj_sparql=None, sbj_variable=sbj_variable, obj_sparql=ctx.slots["entitySet"][0], obj_variable=obj_variable, pred=ctx.slots["predicate"], direction=ctx.slots["direction"])
        else:
            raise Exception("Unexpected number of entitySet")
        
        if ctx.slots["qualifierFilter"] != {}:
            fact_node = gen_rel_fact_node(ctx.slots["predicate"], ctx.slots["direction"], sbj_variable, obj_variable)
            ctx.slots["qualifierFilter"]["valueType"] = ctx.slots["qualifierFilter"]["valueType"] if ctx.slots["qualifierFilter"]["valueType"] != "" else self.getValueType(ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"])
            ctx.slots["qualifierFilter"]["value"], qv_unit = self.getValueUnit(ctx.slots["qualifierFilter"]["value"], ctx.slots["qualifierFilter"]["valueType"])
            subqueries += gen_attribute_query(ctx.slots["qualifierFilter"]["qualifier"], ctx.slots["qualifierFilter"]["value"], ctx.slots["qualifierFilter"]["valueType"], qv_unit, ctx.slots["qualifierFilter"]["op"], e=fact_node, in_qualifier=True)

        self.insertEntitySet(ctx.parentCtx, subqueries, ctx.slots["concept"])
        return super().exitEntitySetByPredicate(ctx)
    
    def enterEntitySetByConcept(self, ctx: UnifiedIRParser.EntitySetByConceptContext):
        ctx.slots = strictDict({"concept": "", "entitySet": entitySet()})
        return super().enterEntitySetByConcept(ctx)
    
    def exitEntitySetByConcept(self, ctx: UnifiedIRParser.EntitySetByConceptContext):
        subqueries = gen_concept_query(ctx.slots["concept"]) if ctx.slots["concept"] != "" else ""
        
        if ctx.slots["entitySet"]:
            self.insertEntitySet(ctx.parentCtx, and_two_descriptions(ctx.slots["entitySet"], subqueries, same_concept(ctx.slots["concept"], ctx.slots["entitySet"])), ctx.slots["concept"])
        else:
            self.insertEntitySet(ctx.parentCtx, subqueries, ctx.slots["concept"])
        return super().exitEntitySetByConcept(ctx)
    


    def enterFilterByRank(self, ctx: UnifiedIRParser.FilterByRankContext):
        ctx.slots = strictDict({"number": "1", "attribute": ""})
        return super().enterFilterByRank(ctx)
    
    def exitFilterByRank(self, ctx: UnifiedIRParser.FilterByRankContext):
        ctx.parentCtx.slots["number"] = ctx.slots["number"]
        ctx.parentCtx.slots["attribute"] = ctx.slots["attribute"]
        return super().exitFilterByRank(ctx)

    def enterFilterByAttribute(self, ctx: UnifiedIRParser.FilterByAttributeContext):
        ctx.slots = strictDict({"attribute": "", "op": "=", "valueType":"", "value": ""})
        return super().enterFilterByAttribute(ctx)
    
    def exitFilterByAttribute(self, ctx: UnifiedIRParser.FilterByAttributeContext):
        ctx.parentCtx.slots["attribute"] = ctx.slots["attribute"]
        ctx.parentCtx.slots["op"] = ctx.slots["op"]
        ctx.parentCtx.slots["valueType"] = ctx.slots["valueType"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        return super().exitFilterByAttribute(ctx)

    def enterFilterByPredicate(self, ctx: UnifiedIRParser.FilterByPredicateContext):
        ctx.slots = strictDict({"predicate": "", "direction": ""})
        return super().enterFilterByPredicate(ctx)
    
    def exitFilterByPredicate(self, ctx: UnifiedIRParser.FilterByPredicateContext):
        ctx.parentCtx.slots["predicate"] = ctx.slots["predicate"]
        ctx.parentCtx.slots["direction"] = ctx.slots["direction"]
        return super().exitFilterByPredicate(ctx)

    def enterFilterByQualifier(self, ctx: UnifiedIRParser.FilterByQualifierContext):
        ctx.slots = strictDict({"qualifier": "", "op": "=", "valueType":"", "value": ""})
        return super().enterFilterByQualifier(ctx)
    
    def exitFilterByQualifier(self, ctx: UnifiedIRParser.FilterByQualifierContext):
        ctx.parentCtx.slots["qualifierFilter"]["qualifier"] = ctx.slots["qualifier"]
        ctx.parentCtx.slots["qualifierFilter"]["op"] = ctx.slots["op"]
        ctx.parentCtx.slots["qualifierFilter"]["valueType"] = ctx.slots["valueType"]
        ctx.parentCtx.slots["qualifierFilter"]["value"] = ctx.slots["value"]
        return super().exitFilterByQualifier(ctx)



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
        ctx.parentCtx.parentCtx.slots["orderBy"] = "DESC({})"
        return super().enterLargest(ctx)
    
    def exitSmallest(self, ctx: UnifiedIRParser.SmallestContext):
        ctx.parentCtx.parentCtx.slots["orderBy"] = "{}"
        return super().exitSmallest(ctx)


    
    # def enterTopK(self, ctx: UnifiedIRParser.TopKContext):
    #     ctx.slots = strictDict({"number": ""})
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