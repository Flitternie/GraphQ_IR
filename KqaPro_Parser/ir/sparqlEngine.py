import rdflib
from rdflib import URIRef, BNode, Literal, XSD
from rdflib.plugins.stores import sparqlstore
from itertools import chain
from tqdm import tqdm
import re
import os

def legal(s):
    # convert predicate and attribute keys to legal format
    return s.replace(' ', '_')

def esc_escape(s):
    '''
    Why we need this:
    If there is an escape in Literal, such as '\EUR', the query string will be something like '?pv <pred:value> "\\EUR"'.
    However, in virtuoso engine, \\ is connected with E, and \\E forms a bad escape sequence.
    So we must repeat \\, and virtuoso will consider "\\\\EUR" as "\EUR".

    Note this must be applied before esc_quot, as esc_quot will introduce extra escapes.
    '''
    return s.replace('\\', '\\\\')

def esc_quot(s):
    '''
    Why we need this:
    We use "<value>" to represent a literal value in the sparql query.
    If the <value> has a double quotation mark itself, we must escape it to make sure the query is valid for the virtuoso engine.
    '''
    return s.replace('"', '\\"')

class SparqlEngine():
    gs1 = None
    PRED_INSTANCE = 'pred:instance_of'
    PRED_NAME = 'pred:name'

    PRED_VALUE = 'pred:value'       # link packed value node to its literal value
    PRED_UNIT = 'pred:unit'         # link packed value node to its unit

    PRED_YEAR = 'pred:year'         # link packed value node to its year value, which is an integer
    PRED_DATE = 'pred:date'         # link packed value node to its date value, which is a date

    PRED_FACT_H = 'pred:fact_h'     # link qualifier node to its head
    PRED_FACT_R = 'pred:fact_r'
    PRED_FACT_T = 'pred:fact_t'

    SPECIAL_PREDICATES = (PRED_INSTANCE, PRED_NAME, PRED_VALUE, PRED_UNIT, PRED_YEAR, PRED_DATE, PRED_FACT_H, PRED_FACT_R, PRED_FACT_T)
    def __init__(self, data, ttl_file=''):
        self.nodes = nodes = {}
        for i in chain(data.concepts, data.entities):
            nodes[i] = URIRef(i)
        for p in chain(data.predicates, data.attribute_keys, SparqlEngine.SPECIAL_PREDICATES):
            nodes[p] = URIRef(legal(p))
        
        self.graph = graph = rdflib.Graph()

        for i in chain(data.concepts, data.entities):
            name = data.get_name(i)
            graph.add((nodes[i], nodes[SparqlEngine.PRED_NAME], Literal(name)))

        for ent_id in tqdm(data.entities, desc='Establishing rdf graph'):
            for con_id in data.get_all_concepts(ent_id):
                graph.add((nodes[ent_id], nodes[SparqlEngine.PRED_INSTANCE], nodes[con_id]))
            for (k, v, qualifiers) in data.get_attribute_facts(ent_id):
                h, r = nodes[ent_id], nodes[k]
                t = self._get_value_node(v)
                graph.add((h, r, t))
                fact_node = self._new_fact_node(h, r, t)

                for qk, qvs in qualifiers.items():
                    for qv in qvs:
                        h, r = fact_node, nodes[qk]
                        t = self._get_value_node(qv)
                        if len(list(graph[t])) == 0:
                            print(t)
                        graph.add((h, r, t))

            for (pred, obj_id, direction, qualifiers) in data.get_relation_facts(ent_id):
                if direction == 'backward':
                    if data.is_concept(obj_id):
                        h, r, t = nodes[obj_id], nodes[pred], nodes[ent_id]
                    else:
                        continue
                else:
                    h, r, t = nodes[ent_id], nodes[pred], nodes[obj_id]
                graph.add((h, r, t))
                fact_node = self._new_fact_node(h, r, t)
                for qk, qvs in qualifiers.items():
                    for qv in qvs:
                        h, r = fact_node, nodes[qk]
                        t = self._get_value_node(qv)
                        graph.add((h, r, t))

        if ttl_file:
            print('Save graph to {}'.format(ttl_file))
            graph.serialize(ttl_file, format='turtle')


    def _get_value_node(self, v):
        # we use a URIRef node, because we need its reference in query results, which is not supported by BNode
        if v.type == 'string':
            node = BNode()
            self.graph.add((node, self.nodes[SparqlEngine.PRED_VALUE], Literal(v.value)))
            return node
        elif v.type == 'quantity': 
            # we use a node to pack value and unit
            node = BNode()
            self.graph.add((node, self.nodes[SparqlEngine.PRED_VALUE], Literal(v.value, datatype=XSD.double)))
            self.graph.add((node, self.nodes[SparqlEngine.PRED_UNIT], Literal(v.unit)))
            return node
        elif v.type == 'year':
            node = BNode()
            self.graph.add((node, self.nodes[SparqlEngine.PRED_YEAR], Literal(v.value)))
            return node
        elif v.type == 'date':
            # use a node to pack year and date
            node = BNode()
            self.graph.add((node, self.nodes[SparqlEngine.PRED_YEAR], Literal(v.value.year)))
            self.graph.add((node, self.nodes[SparqlEngine.PRED_DATE], Literal(v.value, datatype=XSD.date)))
            return node

    def _new_fact_node(self, h, r, t):
        node = BNode()
        self.graph.add((node, self.nodes[SparqlEngine.PRED_FACT_H], h))
        self.graph.add((node, self.nodes[SparqlEngine.PRED_FACT_R], r))
        self.graph.add((node, self.nodes[SparqlEngine.PRED_FACT_T], t))
        return node

    def query(self, q):
        return list(self.graph.query(q))

    def get_sparql_answers(sparql, data):
        """
        return all answers
        - data: DataForSPARQL object, we need the key_type
        """
        try:
            # infer the parse_type based on sparql
            if sparql.startswith('SELECT DISTINCT ?e') or sparql.startswith('SELECT ?e'):
                parse_type = 'name'
            elif sparql.startswith('SELECT (COUNT(DISTINCT ?e)'):
                parse_type = 'count'
            elif sparql.startswith('SELECT DISTINCT ?p '):
                parse_type = 'pred'
            elif sparql.startswith('ASK'):
                parse_type = 'bool'
            else:
                tokens = sparql.split()
                tgt = tokens[2]
                for i in range(len(tokens)-1, 1, -1):
                    if tokens[i]=='.' and tokens[i-1]==tgt:
                        key = tokens[i-2]
                        break
                key = key[1:-1].replace('_', ' ')
                t = data.key_type[key]
                parse_type = 'attr_{}'.format(t)

            res = SparqlEngine.query_virtuoso(sparql)
            if res.vars:
                res = [[binding[v] for v in res.vars] for binding in res.bindings]
            else:
                res = [res.askAnswer]
                assert parse_type == 'bool'
            
            parsed_answers = []
            for i in range(len(res)): # the i-th answer
                if parse_type == 'name':
                    node = res[i][0]
                    sp = 'SELECT DISTINCT ?v WHERE {{ <{}> <{}> ?v .  }}'.format(node, SparqlEngine.PRED_NAME)
                    sec_res = SparqlEngine.query_virtuoso(sp)
                    sec_res = [[binding[v] for v in sec_res.vars] for binding in sec_res.bindings]
                    name = sec_res[0][0].value
                    parsed_answer = name
                elif parse_type == 'count':
                    count = res[i][0].value
                    parsed_answer = str(count)
                elif parse_type.startswith('attr_'):
                    node = res[i][0]
                    v_type = parse_type.split('_')[1]
                    unit = None
                    if v_type == 'string':
                        sp = 'SELECT DISTINCT ?v WHERE {{ <{}> <{}> ?v .  }}'.format(node, SparqlEngine.PRED_VALUE)
                    elif v_type == 'quantity':
                        # Note: For those large number, ?v is truncated by virtuoso (e.g., 14756087 to 1.47561e+07)
                        # To obtain the accurate ?v, we need to cast it to str
                        sp = 'SELECT DISTINCT ?v,?u,(str(?v) as ?sv) WHERE {{ <{}> <{}> ?v ; <{}> ?u .  }}'.format(node, SparqlEngine.PRED_VALUE, SparqlEngine.PRED_UNIT)
                    elif v_type == 'year':
                        sp = 'SELECT DISTINCT ?v WHERE {{ <{}> <{}> ?v .  }}'.format(node, SparqlEngine.PRED_YEAR)
                    elif v_type == 'date':
                        sp = 'SELECT DISTINCT ?v WHERE {{ <{}> <{}> ?v .  }}'.format(node, SparqlEngine.PRED_DATE)
                    else:
                        raise Exception('unsupported parse type')
                    sec_res = SparqlEngine.query_virtuoso(sp)
                    sec_res = [[binding[v] for v in sec_res.vars] for binding in sec_res.bindings]
                    # if there is no specific date, then convert the type to year
                    if len(sec_res)==0 and v_type == 'date':
                        v_type = 'year'
                        sp = 'SELECT DISTINCT ?v WHERE {{ <{}> <{}> ?v .  }}'.format(node, SparqlEngine.PRED_YEAR)
                        sec_res = SparqlEngine.query_virtuoso(sp)
                        sec_res = [[binding[v] for v in sec_res.vars] for binding in sec_res.bindings]
                    if v_type == 'quantity':
                        value = float(sec_res[0][2].value)
                        unit = sec_res[0][1].value
                    else:
                        value = sec_res[0][0].value
                    value = ValueClass(v_type, value, unit)
                    parsed_answer = str(value)
                elif parse_type == 'bool':
                    parsed_answer = 'yes' if res[i] else 'no'
                elif parse_type == 'pred':
                    parsed_answer = str(res[i][0])
                    parsed_answer = parsed_answer.replace('_', ' ')

                parsed_answers.append(parsed_answer)
            return parsed_answers
        except Exception:
            return None


    # NOTE: there must be a space before and after each .
    def gen_name_query(ent_name):
        return '?e <{}> "{}" . '.format(SparqlEngine.PRED_NAME, esc_quot(ent_name))

    def gen_concept_query(concept_name):
        return '?e <{}> ?c . ?c <{}> "{}" . '.format(SparqlEngine.PRED_INSTANCE, SparqlEngine.PRED_NAME, esc_quot(concept_name))

    def gen_attribute_query(k, v, op='=', e='?e', in_qualifier=False):
        k = legal(k)
        if v.type == 'string':
            query = '?e <{}> ?pv . ?pv <{}> "{}" . '.format(
                k, 
                SparqlEngine.PRED_VALUE, esc_quot(esc_escape(v.value))
                )
        elif v.type == 'quantity':
            # it is necessary to always cast value as xsd:double, because these is something wrong when comparing different types (e.g., int with double)
            if op == '=':
                query = '?e <{}> ?pv . ?pv <{}> "{}" . ?pv <{}> "{}"^^xsd:double . '.format(
                    k,
                    SparqlEngine.PRED_UNIT, esc_quot(v.unit),
                    SparqlEngine.PRED_VALUE, v.value
                    )
            else:
                query = '?e <{}> ?pv . ?pv <{}> "{}" . ?pv <{}> ?v . FILTER ( ?v {} "{}"^^xsd:double ) . '.format(
                    k,
                    SparqlEngine.PRED_UNIT, esc_quot(v.unit),
                    SparqlEngine.PRED_VALUE, 
                    op, v.value
                    )
        elif v.type == 'year':
            if op == '=':
                query = '?e <{}> ?pv . ?pv <{}> {} . '.format(
                    k,
                    SparqlEngine.PRED_YEAR, v.value
                    )
            else:
                query = '?e <{}> ?pv . ?pv <{}> ?v . FILTER ( ?v {} {} ) . '.format(
                    k,
                    SparqlEngine.PRED_YEAR,
                    op, v.value
                    )
        elif v.type == 'date':
            if op == '=':
                query = '?e <{}> ?pv . ?pv <{}> "{}"^^xsd:date . '.format(
                    k,
                    SparqlEngine.PRED_DATE, v.value
                    )
            else:
                query = '?e <{}> ?pv . ?pv <{}> ?v . FILTER ( ?v {} "{}"^^xsd:date ) . '.format(
                    k,
                    SparqlEngine.PRED_DATE,
                    op, v.value
                    )
        if in_qualifier:
            query = query.replace('?pv', '?qpv').replace('?v', '?qv')
        if e != '?e': # variables in e must not be replaced
            query = query.replace('?e', e)
        return query

    def gen_attr_fact_node(k, e='?e'):
        k = legal(k)
        return '[ <{}> {} ; <{}> <{}> ; <{}> ?pv ]'.format(
            SparqlEngine.PRED_FACT_H, e,
            SparqlEngine.PRED_FACT_R, k,
            SparqlEngine.PRED_FACT_T
            )

    def contain_variable(query, variable):
        return variable in query.split()

    def get_all_variables(query):
        return list(set([w for w in query.split() if w.startswith('?')]))

    def get_all_clauses(query):
        return [s.strip() for s in query.split(' . ') if s.strip()]

    def ensemble_clauses(clauses):
        return ' . '.join(clauses) + ' . '

    def replace_variable(query, variable):
        """
        replace variable in query, and return new query and new variable
        e.g., query='?e <parent> ?e_1', variable='?e', then results should be '?e_1 <parent> ?e_2' and '?e_1'
        """
        if SparqlEngine.contain_variable(query, variable):
            if '_' in variable:
                prefix, idx = variable.split('_')
                idx = int(idx)
            else:
                prefix = variable
                idx = 0
            new_variable = '{}_{}'.format(prefix, idx+1)
            if SparqlEngine.contain_variable(query, new_variable):
                query, _ = SparqlEngine.replace_variable(query, new_variable)
            query = ' '.join([new_variable if w == variable else w for w in query.split()]) + ' ' # DONT forget the space
            return query, new_variable
        else:
            return query, variable

    def gen_relation_query(pred, direction, obj_sparql, obj_variable):
        assert obj_variable != '?e'
        pred = legal(pred)
        if direction == 'forward':
            query = '?e <{}> {} . '.format(pred, obj_variable)
        else:
            query = '{} <{}> ?e . '.format(obj_variable, pred)
        return query + obj_sparql + ' '

    def gen_rel_fact_node(pred, direction, obj_variable, e='?e'):
        pred = legal(pred)
        if direction == 'forward':
            return '[ <{}> {} ; <{}> <{}> ; <{}> {} ]'.format(
                SparqlEngine.PRED_FACT_H, e,
                SparqlEngine.PRED_FACT_R, pred,
                SparqlEngine.PRED_FACT_T, obj_variable
                )
        else:
            return '[ <{}> {} ; <{}> <{}> ; <{}> {} ]'.format(
                SparqlEngine.PRED_FACT_H, obj_variable,
                SparqlEngine.PRED_FACT_R, pred,
                SparqlEngine.PRED_FACT_T, e
                )

    def append_attribute_value_query(query, k, v_type, e='?e', in_qualifier=False):
        """
        Given a query about entity ?e, we query its attribute value of k,
        and denote the value by variable ?v
        """
        k = legal(k)
        if v_type == 'string' or v_type == 'quantity':
            s = '?e <{}> ?pv . ?pv <{}> ?v . '.format(
                k, SparqlEngine.PRED_VALUE
            )
        elif v_type == 'year':
            s = '?e <{}> ?pv . ?pv <{}> ?v . '.format(
                k, SparqlEngine.PRED_YEAR
            )
        elif v_type == 'date':
            s = '?e <{}> ?pv . ?pv <{}> ?v . '.format(
                k, SparqlEngine.PRED_DATE
            )
        elif v_type == '':
            s = '?e <{}> ?pv . '.format(k)

        if in_qualifier:
            s = s.replace('?pv', '?qpv').replace('?v', '?qv')
            query, _ = SparqlEngine.replace_variable(query, '?qpv')
            query, _ = SparqlEngine.replace_variable(query, '?qv')
        else:
            query, _ = SparqlEngine.replace_variable(query, '?pv')
            query, _ = SparqlEngine.replace_variable(query, '?v')

        if e != '?e':
            s = s.replace('?e', e)
        query = query + s
        return query


if __name__ == '__main__':
    from data import Data
    data = Data()
    ttl_file = './results/kg.ttl'
    engine = SparqlEngine(data, ttl_file)
