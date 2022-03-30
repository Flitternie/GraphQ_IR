import os
import re
from collections import OrderedDict
from antlr4 import *

from .UnifiedIRLexer import UnifiedIRLexer
from .UnifiedIRParser import UnifiedIRParser
from .UnifiedIRParserListener import UnifiedIRParserListener

from ..utils import *

overnight_domains = ['basketball', 'blocks', 'calendar', 'housing', 'publications', 'recipes', 'restaurants', 'socialnetwork']

def read_grammar(file_path):
    grammar = {}
    for domain in overnight_domains:
        domain_grammar = {}
        with open(os.path.join(file_path, domain + '.grammar'), 'r') as f:
            for line in f:
                if line.strip().startswith('#') or line == '\n':
                    continue
                # elif re.match(r'.*for \@x \((.*?)\)', line):
                #     iter_element = re.match(r'.*for \@x \((.*?)\)', line).group(1).split()
                rule = re.findall(r'\(rule \$(.*?) \((.*?)\) \(ConstantFn (.*)\)\)', line)
                if rule:
                    type = re.sub(r'[0-9]', '', rule[0][0]).replace("/", "")
                    abbr = rule[0][1]
                    full = rule[0][2]
                    if type in domain_grammar.keys():
                        # domain_grammar[type][abbr] = full
                        domain_grammar[type].append(full)
                    else:
                        # domain_grammar[type] = {abbr: full}
                        domain_grammar[type] = [full]
            for type in domain_grammar.keys():
                # domain_grammar[type] = dict(sorted(domain_grammar[type].items()))
                domain_grammar[type] = sorted(sorted(domain_grammar[type]), key=len, reverse=False)
            grammar[domain] = domain_grammar
    return grammar



class OvernightEmitter(UnifiedIRParserListener):
    def __init__(self):
        self.logical_form = ""
        self.domain = ""
        
        PREFIX = "call SW"
        self.func = {
            "listValue":                PREFIX + ".listValue",
            "size":                     "call .size",
            "domain":                   PREFIX + ".domain",
            "singleton":                PREFIX + ".singleton",
            "filter":                   PREFIX + ".filter",
            "getProperty":              PREFIX + ".getProperty",
            "superlative":              PREFIX + ".superlative",
            "countSuperlative":         PREFIX + ".countSuperlative",
            "countComparative":         PREFIX + ".countComparative",
            "aggregate":                PREFIX + ".aggregate",
            "concat":                   PREFIX + ".concat",
            "reverse":                  PREFIX + ".reverse",
            "ensureNumericProperty":    PREFIX + ".ensureNumericProperty",
            "ensureNumericEntity":      PREFIX + ".ensureNumericEntity",
        }
        self.grammar = read_grammar("./data/overnight/grammar/")
    
    def initialize(self):
        self.logical_form = ""
    
    def set_domain(self, domain):
        self.domain = domain

    def get_logical_form(self, ctx):
        return self.logical_form

    def get_full_name(self, abbr, datatype, domain):
        datatype = [datatype] if isinstance(datatype, str) else datatype
        if domain:
            domain_datatype = [i for i in datatype if i in self.grammar[domain].keys()]
            for i in domain_datatype:
                # for name in self.grammar[domain][i].values():
                for name in self.grammar[domain][i]:
                    if abbr in name or abbr.replace(" ", "_") in name:
                        return name
        else:
            for domain in self.grammar.keys():
                domain_datatype = [i for i in datatype if i in self.grammar[domain].keys()]
                for i in domain_datatype:
                    # for name in self.grammar[domain][i].values():
                    for name in self.grammar[domain][i]:
                        if abbr in name or abbr.replace(" ", "_") in name:
                            return name
        return None
    
    def get_full_name_and_type(self, abbr, domain):
        results = {}
        if domain:
            for datatype in self.grammar[domain].keys():
                # for name in self.grammar[domain][datatype].values():
                for name in self.grammar[domain][datatype]:
                    if abbr in name or abbr.replace(" ", "_") in name:
                        results[datatype] = name
                        break
        else:
            for domain in self.grammar.keys():
                for datatype in self.grammar[domain].keys():
                    # for name in self.grammar[domain][datatype].values():
                    for name in self.grammar[domain][datatype]:
                        if abbr in name or abbr.replace(" ", "_") in name:
                            results[datatype] = name
                            break
        return results
    
    def process_value(self, value_type, value):
        value = value.replace(" : ", " ") if value_type == "time" else value
        return "( {} {} )".format(value_type, value) if value_type != "" else value



    def enterRoot(self, ctx: UnifiedIRParser.RootContext):
        self.initialize()
        ctx.slots = strictDict({"LF": ""})
        return super().enterRoot(ctx)

    def exitRoot(self, ctx: UnifiedIRParser.RootContext):
        self.logical_form = ctx.slots["LF"]
        return super().exitRoot(ctx)    
    
    def enterEntityQuery(self, ctx: UnifiedIRParser.EntityQueryContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterEntityQuery(ctx)
    
    def exitEntityQuery(self, ctx: UnifiedIRParser.EntityQueryContext):
        ctx.parentCtx.slots["LF"] = "( {} {} )".format(self.func["listValue"], ctx.slots["entitySet"])
        return super().exitEntityQuery(ctx)
    
    def enterAttributeQuery(self, ctx: UnifiedIRParser.AttributeQueryContext):
        ctx.slots = strictDict({"entitySet": "", "attribute": ""})
        return super().enterAttributeQuery(ctx)
    
    def exitAttributeQuery(self, ctx: UnifiedIRParser.AttributeQueryContext):
        subquery = "( {} {} {} )".format(self.func["getProperty"], ctx.slots["entitySet"], ctx.slots["attribute"])
        ctx.parentCtx.slots["LF"] = "( {} {} )".format(self.func["listValue"], subquery)
        return super().exitAttributeQuery(ctx)
    
    def enterCountQuery(self, ctx: UnifiedIRParser.CountQueryContext):
        ctx.slots = strictDict({"entitySet": ""})
        return super().enterCountQuery(ctx)
    
    def exitCountQuery(self, ctx: UnifiedIRParser.CountQueryContext):
        subquery = "( {} {} )".format(self.func["size"], ctx.slots["entitySet"])
        ctx.parentCtx.slots["LF"] = "( {} {} )".format(self.func["listValue"], subquery)
        return super().exitCountQuery(ctx)

    def enterValueQuery(self, ctx: UnifiedIRParser.ValueQueryContext):
        ctx.slots = strictDict({"value": ""})
        return super().enterValueQuery(ctx)
    
    def exitValueQuery(self, ctx: UnifiedIRParser.ValueQueryContext):
        ctx.parentCtx.slots["LF"] = "( {} {} )".format(self.func["listValue"], ctx.slots["value"])
        return super().exitValueQuery(ctx)
    
    def enterEntitySetGroup(self, ctx: UnifiedIRParser.EntitySetGroupContext):
        ctx.slots = strictDict({"entitySet": [], "setOP": ""})
        return super().enterEntitySetGroup(ctx)
    
    def exitEntitySetGroup(self, ctx: UnifiedIRParser.EntitySetGroupContext):
        assert ctx.slots["setOP"] == "or" and isinstance(ctx.slots["entitySet"], list) and len(ctx.slots["entitySet"]) == 2
        insert(ctx.parentCtx, "( {} {} {} )".format(self.func["concat"], ctx.slots["entitySet"][0], ctx.slots["entitySet"][1]))
        return super().exitEntitySetGroup(ctx)

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
        insert(ctx.parentCtx, ctx.slots["entity"], is_atom=True)
        return super().exitEntitySetAtom(ctx)
    
    def exitEntitySetPlaceholder(self, ctx: UnifiedIRParser.EntitySetPlaceholderContext):
        insert(ctx.parentCtx, "", is_pop=True)
        return super().exitEntitySetPlaceholder(ctx)
    
    def enterEntitySetByAttribute(self, ctx: UnifiedIRParser.EntitySetByAttributeContext):
        ctx.slots = strictDict({"concept":"", "entitySet": "", "attribute": "", "op": "", "value": ""})
        return super().enterEntitySetByAttribute(ctx)
    
    def exitEntitySetByAttribute(self, ctx: UnifiedIRParser.EntitySetByAttributeContext):
        if ctx.slots["entitySet"].is_pop:
            assert ctx.slots["concept"] == ""
            subquery = "( lambda s ( {} ( var s ) {} {} {} ) )".format(self.func["filter"], ctx.slots["attribute"], ctx.slots["op"], ctx.slots["value"])
        else:
            subquery = "( {} {} {} {} {} )".format(self.func["filter"], ctx.slots["entitySet"], ctx.slots["attribute"], ctx.slots["op"], ctx.slots["value"])
        # if ctx.slots["conceptType"] == "TypeNP":
        #     subquery_constraint = "( {} ( getProperty ( singleton {} ) ( string ! type ) ) {} {} {} )".format(self.func["filter"], ctx.slots["concept"], ctx.slots["attribute"], ctx.slots["op"], value)
        insert(ctx.parentCtx, subquery)
        return super().exitEntitySetByAttribute(ctx)
    
    def enterFilterByAttribute(self, ctx: UnifiedIRParser.FilterByAttributeContext):
        ctx.slots = strictDict({"attribute": "", "op": "", "value": ""})
        return super().enterFilterByAttribute(ctx)
    
    def exitFilterByAttribute(self, ctx: UnifiedIRParser.FilterByAttributeContext):
        ctx.parentCtx.slots["attribute"] = ctx.slots["attribute"]
        ctx.parentCtx.slots["op"] = ctx.slots["op"]
        # can be further restricted by ( call SW.ensureNumericProperty {} )
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        return super().exitFilterByAttribute(ctx)
    

    
    def enterEntitySetByRank(self, ctx: UnifiedIRParser.EntitySetByRankContext):
        ctx.slots = strictDict({"entitySet": "", "op": "", "attribute": ""})
        return super().enterEntitySetByRank(ctx)
    
    def exitEntitySetByRank(self, ctx: UnifiedIRParser.EntitySetByRankContext):
        if ctx.slots["entitySet"].is_pop:
            subquery = "( lambda s ( {} ( var s ) {} {} ) )".format(self.func["superlative"], ctx.slots["op"], ctx.slots["attribute"])
        else:
            subquery = "( {} {} {} {} )".format(self.func["superlative"], ctx.slots["entitySet"], ctx.slots["op"], ctx.slots["attribute"])
        insert(ctx.parentCtx, subquery)
        return super().exitEntitySetByRank(ctx)
    
    def enterFilterByRank(self, ctx: UnifiedIRParser.FilterByRankContext):
        ctx.slots = strictDict({"op": "", "attribute": ""})
        return super().enterFilterByRank(ctx)
    
    def exitFilterByRank(self, ctx: UnifiedIRParser.FilterByRankContext):
        ctx.parentCtx.slots["op"] = ctx.slots["op"]
        ctx.parentCtx.slots["attribute"] = ctx.slots["attribute"]
        return super().exitFilterByRank(ctx)
    


    def enterEntitySetByPredicate(self, ctx: UnifiedIRParser.EntitySetByPredicateContext):
        ctx.slots = strictDict({"concept": "", "entitySet": [], "gate": True, "predicate": "", "op": "", "value": ""})
        return super().enterEntitySetByPredicate(ctx)
    
    def exitEntitySetByPredicate(self, ctx: UnifiedIRParser.EntitySetByPredicateContext):
        if ctx.slots["entitySet"][0].is_pop:
            ctx.slots["entitySet"][0] = ctx.slots["entitySet"][0].reassign("( var s )")

        if ctx.slots["op"] == "" and ctx.slots["value"] == "":
            ctx.slots["gate"] = "=" if ctx.slots["gate"] else "! ="
            if len(ctx.slots["entitySet"]) == 1:
                # LB filterFunc constraintNP predicate RB
                subquery = "( {} {} {} )".format(self.func["filter"], ctx.slots["entitySet"][0], ctx.slots["predicate"])
            else:
                # LB filterFunc constraintNP predicate op np RB
                # LB filterFunc constraintNP reversePredicate op np RB
                if ctx.slots["entitySet"][1].is_pop:
                    subquery = "( {} {} {} )".format(self.func["filter"], ctx.slots["entitySet"][0], ctx.slots["predicate"])
                else:
                    subquery = "( {} {} {} ( string {} ) {} )".format(self.func["filter"], ctx.slots["entitySet"][0], ctx.slots["predicate"], ctx.slots["gate"], ctx.slots["entitySet"][1])
        
        elif "min" in ctx.slots["op"] or "max" in ctx.slots["op"] and ctx.slots["value"] == "":
            if len(ctx.slots["entitySet"]) == 1:
                # LB countSuperlative constraintNP op relNP RB
                subquery = "( {} {} {} {} )".format(self.func["countSuperlative"], ctx.slots["entitySet"][0], ctx.slots["op"], ctx.slots["predicate"])
            else:
                # LB countSuperlative constraintNP op predicate np RB
                if ctx.slots["entitySet"][1].is_pop:
                    subquery = "( {} {} {} {} )".format(self.func["countSuperlative"], ctx.slots["entitySet"][0], ctx.slots["op"], ctx.slots["predicate"])
                else:
                    subquery = "( {} {} {} {} {} )".format(self.func["countSuperlative"], ctx.slots["entitySet"][0], ctx.slots["op"], ctx.slots["predicate"], ctx.slots["entitySet"][1])
               
        elif ctx.slots["value"] != "":
            ctx.slots["op"] = "( string = )" if ctx.slots["op"] == "" else ctx.slots["op"]
            if len(ctx.slots["entitySet"]) == 1:
                # LB countComparative constraintNP relNP op value RB
                subquery = "( {} {} {} {} {} )".format(self.func["countComparative"], ctx.slots["entitySet"][0], ctx.slots["predicate"], ctx.slots["op"], ctx.slots["value"])
            else:
                # LB countComparative constraintNP predicate op value np RB
                # LB countComparative constraintNP reversePredicate op value np RB
                if ctx.slots["entitySet"][1].is_pop:
                    subquery = "( {} {} {} {} {} )".format(self.func["countComparative"], ctx.slots["entitySet"][0], ctx.slots["predicate"], ctx.slots["op"], ctx.slots["value"])
                else:
                    subquery = "( {} {} {} {} {} {} )".format(self.func["countComparative"], ctx.slots["entitySet"][0], ctx.slots["predicate"], ctx.slots["op"], ctx.slots["value"], ctx.slots["entitySet"][1])
        else:
            raise NotImplementedError()
        
        if ctx.slots["entitySet"][0].is_pop:
            subquery = "( lambda s {} )".format(subquery)
        
        insert(ctx.parentCtx, subquery)
        return super().exitEntitySetByPredicate(ctx)
    
    def enterFilterByPredicate(self, ctx: UnifiedIRParser.FilterByPredicateContext):
        ctx.slots = strictDict({"gate": True, "predicate": "", "direction": "", "op": "", "value": ""})
        return super().enterFilterByPredicate(ctx)
    
    def exitFilterByPredicate(self, ctx: UnifiedIRParser.FilterByPredicateContext):
        ctx.parentCtx.slots["gate"] = ctx.slots["gate"] 
        ctx.parentCtx.slots["predicate"] = ctx.slots["predicate"] if ctx.slots["direction"] == "forward" else "( {} {} )".format(self.func["reverse"], ctx.slots["predicate"])
        ctx.parentCtx.slots["op"] = ctx.slots["op"]
        ctx.parentCtx.slots["value"] = ctx.slots["value"]
        return super().exitFilterByPredicate(ctx)



    def enterEntitySetByConcept(self, ctx: UnifiedIRParser.EntitySetByConceptContext):
        ctx.slots = strictDict({"concept":"", "entitySet": ""})
        return super().enterEntitySetByConcept(ctx)

    def exitEntitySetByConcept(self, ctx: UnifiedIRParser.EntitySetByConceptContext):
        concept = self.get_full_name_and_type(ctx.slots["concept"], domain=self.domain)
        if ctx.slots["entitySet"] == "":
                # type + CP (through typeConstraintNP)
                assert "TypeNP" in concept.keys()
                subquery = "( {} ( {} {} ) ( string ! type ) )".format(self.func["getProperty"], self.func["singleton"], concept["TypeNP"])
        else:
            assert "RelNP" in concept.keys()
            if ctx.slots["entitySet"].is_atom:
                subquery = "( {} {} ( {} {} ) )".format(self.func["getProperty"], ctx.slots["entitySet"], self.func["reverse"], concept["RelNP"])
            elif isinstance(ctx.parentCtx.parentCtx, (UnifiedIRParser.AttributeQueryContext, UnifiedIRParser.EntitySetByAttributeContext, UnifiedIRParser.ValueByAttributeContext)):
                # reversePredicate + CP (through eventConstraintNP)
                subquery = "( {} {} ( {} {} ) )".format(self.func["getProperty"], ctx.slots["entitySet"], self.func["reverse"], concept["RelNP"])
            elif isinstance(ctx.parentCtx, UnifiedIRParser.EntitySetByPredicateContext):
                if ctx.parentCtx.slots["entitySet"][0] != "":
                    # reversePredicate + CP (through eventConstraintNP)
                    subquery = "( {} {} ( {} {} ) )".format(self.func["getProperty"], ctx.slots["entitySet"], self.func["reverse"], concept["RelNP"])
                else:
                    # relNP + CP (through domainCPNP)
                    subquery = "( {} ( {} ( {} {} ) ) {} )".format(self.func["getProperty"], ctx.slots["entitySet"], self.func["domain"], concept["RelNP"], concept["RelNP"])
            else:
                # relNP + CP (through domainCPNP)
                subquery = "( {} ( {} ( {} {} ) ) {} )".format(self.func["getProperty"], ctx.slots["entitySet"], self.func["domain"], concept["RelNP"], concept["RelNP"])
        insert(ctx.parentCtx, subquery)
        return super().exitEntitySetByConcept(ctx)

    
    def enterFilterByQualifier(self, ctx: UnifiedIRParser.FilterByQualifierContext):
        raise NotImplementedError()



    def enterValueByAttribute(self, ctx: UnifiedIRParser.ValueByAttributeContext):
        ctx.slots = strictDict({"attribute": "", "entitySet": ""})
        return super().enterValueByAttribute(ctx)
    
    def exitValueByAttribute(self, ctx: UnifiedIRParser.ValueByAttributeContext):
        # can be further restricted by ( call SW.ensureNumericEntity {} )
        ctx.parentCtx.slots["value"] = "( {} {} {} )".format(self.func["getProperty"], ctx.slots["entitySet"], ctx.slots["attribute"])
        return super().exitValueByAttribute(ctx)
    
    def enterValueByAggregate(self, ctx: UnifiedIRParser.ValueByAggregateContext):
        ctx.slots = strictDict({"aggregate": "", "value": ""})
        return super().enterValueByAggregate(ctx)
    
    def exitValueByAggregate(self, ctx: UnifiedIRParser.ValueByAggregateContext):
        ctx.parentCtx.slots["value"] = "( {} {} {} )".format(self.func["aggregate"], ctx.slots["aggregate"], ctx.slots["value"])
        return super().exitValueByAggregate(ctx)
    
    def enterValueByUnion(self, ctx: UnifiedIRParser.ValueByUnionContext):
        ctx.slots = strictDict({"valueType": "", "value": []})
        return super().enterValueByUnion(ctx)
    
    def exitValueByUnion(self, ctx: UnifiedIRParser.ValueByUnionContext):
        assert isinstance(ctx.slots["value"], list) and len(ctx.slots["value"]) == 2
        for i in range(len(ctx.slots["value"])):
            ctx.slots["value"][i] = self.process_value(ctx.slots["valueType"], ctx.slots["value"][i])
        ctx.parentCtx.slots["value"] = "( {} {} {} )".format(self.func["concat"], ctx.slots["value"][0], ctx.slots["value"][1])
        return super().exitValueByUnion(ctx)

    def enterValueAtom(self, ctx: UnifiedIRParser.ValueAtomContext):
        ctx.slots = strictDict({"valueType": "", "value": ""})
        return super().enterValueAtom(ctx)
    
    def exitValueAtom(self, ctx: UnifiedIRParser.ValueAtomContext):
        if len(ctx.slots["value"].split()) > 1:
            if len(ctx.slots["value"].split()) == 2:
                processed_value = " en.".join(ctx.slots["value"].split())
            else: 
                processed_value = ctx.slots["value"].split(maxsplit=1)
                processed_value = [processed_value[0], processed_value[1].replace(" ", "_")]
                processed_value = " en.".join(processed_value)
            full_value = self.get_full_name(processed_value, datatype=("EntityNP", "Value"), domain=self.domain) 
            ctx.slots["value"] = re.findall(r"\(.* ([0-9]* .*)\)", full_value)[0] if full_value else ctx.slots["value"]

        value = self.process_value(ctx.slots["valueType"], ctx.slots["value"])
        if isinstance(ctx.parentCtx.slots["value"], list):
            ctx.parentCtx.slots["value"].append(value)
        else:
            ctx.parentCtx.slots["value"] = value
        return super().exitValueAtom(ctx)



    def enterEntity(self, ctx: UnifiedIRParser.EntityContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterEntity(ctx)
    
    def exitEntity(self, ctx: UnifiedIRParser.EntityContext):
        ctx.parentCtx.slots["entity"] = self.get_full_name(ctx.slots["string"], datatype="EntityNP", domain=self.domain)
        return super().exitEntity(ctx)
    
    def enterAttribute(self, ctx: UnifiedIRParser.AttributeContext):
        ctx.slots = strictDict({"string": ""})
        return super().enterAttribute(ctx)
    
    def exitAttribute(self, ctx: UnifiedIRParser.AttributeContext):
        ctx.parentCtx.slots["attribute"] = self.get_full_name(ctx.slots["string"], datatype="RelNP", domain=self.domain)
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
        ctx.parentCtx.slots["predicate"] = self.get_full_name(ctx.slots["string"], datatype=("VP", "VPNP", "RelNP"), domain=self.domain)
        return super().exitPredicate(ctx)
    
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
    
    def exitNot(self, ctx: UnifiedIRParser.NotContext):
        ctx.parentCtx.slots["gate"] = False
        return super().exitNot(ctx)
    
    def exitSum(self, ctx: UnifiedIRParser.SumContext):
        ctx.parentCtx.slots["aggregate"] = "( string sum )"
        return super().exitSum(ctx)
    
    def exitAverage(self, ctx: UnifiedIRParser.AverageContext):
        ctx.parentCtx.slots["aggregate"] = "( string avg )"
        return super().exitAverage(ctx)
    
    def exitLargest(self, ctx: UnifiedIRParser.LargestContext):
        ctx.parentCtx.slots["op"] = "( string max )"
        return super().exitLargest(ctx)
    
    def exitSmallest(self, ctx: UnifiedIRParser.SmallestContext):
        ctx.parentCtx.slots["op"] = "( string min )"
        return super().exitSmallest(ctx)

    def exitEqual(self, ctx: UnifiedIRParser.EqualContext):
        ctx.parentCtx.slots["op"] = "( string = )"
        return super().exitEqual(ctx)
    
    def exitNotEqual(self, ctx: UnifiedIRParser.NotEqualContext):
        ctx.parentCtx.slots["op"] = "( string ! = )"
        return super().exitNotEqual(ctx)
    
    def exitLarger(self, ctx: UnifiedIRParser.LargerContext):
        ctx.parentCtx.slots["op"] = "( string > )"
        return super().exitLarger(ctx)
    
    def exitSmaller(self, ctx: UnifiedIRParser.SmallerContext):
        ctx.parentCtx.slots["op"] = "( string < )"
        return super().exitSmaller(ctx)
    
    def exitLargerEqual(self, ctx: UnifiedIRParser.LargerEqualContext):
        ctx.parentCtx.slots["op"] = "( string >= )"
        return super().exitLargerEqual(ctx)
    
    def exitSmallerEqual(self, ctx: UnifiedIRParser.SmallerEqualContext):
        ctx.parentCtx.slots["op"] = "( string <= )"
        return super().exitSmallerEqual(ctx)
    
    def exitText(self, ctx: UnifiedIRParser.TextContext):
        ctx.parentCtx.slots["valueType"] = "string"
        return super().exitText(ctx)
    
    def exitQuantity(self, ctx: UnifiedIRParser.QuantityContext):
        ctx.parentCtx.slots["valueType"] = "number"
        return super().exitQuantity(ctx)

    def exitDate(self, ctx: UnifiedIRParser.DateContext):
        ctx.parentCtx.slots["valueType"] = "date"
        return super().exitDate(ctx)
    
    def exitYear(self, ctx: UnifiedIRParser.YearContext):
        ctx.parentCtx.slots["valueType"] = "year"
        return super().exitYear(ctx)
    
    def exitTime(self, ctx: UnifiedIRParser.TimeContext):
        ctx.parentCtx.slots["valueType"] = "time"
        return super().exitTime(ctx)
    

    def enterString(self, ctx: UnifiedIRParser.StringContext):
        if not isinstance(ctx.parentCtx, UnifiedIRParser.StringContext):
            ctx.parentCtx.slots["string"] = str(ctx.getText()).strip()

    def enterNumber(self, ctx: UnifiedIRParser.NumberContext):
        if not isinstance(ctx.parentCtx, UnifiedIRParser.NumberContext):
            ctx.parentCtx.slots["number"] = str(ctx.getText()).strip()