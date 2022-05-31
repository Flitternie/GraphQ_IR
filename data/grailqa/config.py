import os
import re
import json
import pickle

import numpy as np
from itertools import chain

from data.grailqa.utils.sparql_executer import *

special_tokens = []
domains = []
path = str(Path(__file__).parent.absolute())

uri2abbr = {
    "<http://www.w3.org/2001/XMLSchema#float>": "xsd:float",
    "<http://www.w3.org/2001/XMLSchema#double>": "xsd:double",
    "<http://www.w3.org/2001/XMLSchema#integer>": "xsd:int",
    "<http://www.w3.org/2001/XMLSchema#gYear>": "xsd:year",
    "<http://www.w3.org/2001/XMLSchema#gYearMonth>": "xsd:gYearMonth",
    "<http://www.w3.org/2001/XMLSchema#date>": "xsd:date",
    "<http://www.w3.org/2001/XMLSchema#dateTime>": "xsd:time"
}

abbr2uri = {
    "xsd:float": "<http://www.w3.org/2001/XMLSchema#float>",
    "xsd:double": "<http://www.w3.org/2001/XMLSchema#float>",
    "xsd:int": "<http://www.w3.org/2001/XMLSchema#integer>",
    "xsd:year": "<http://www.w3.org/2001/XMLSchema#gYear>",
    "xsd:date": "<http://www.w3.org/2001/XMLSchema#date>",
    "xsd:gYearMonth": "<http://www.w3.org/2001/XMLSchema#gYearMonth>",
    "xsd:time": "<http://www.w3.org/2001/XMLSchema#dateTime>"
}

def unpack(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    types, relations = set(), set()
    for line in lines:
        try:
            h, r, t = line.split()
        except ValueError:
            h, r, t = line.split()[:3]
            continue
        types.add(h)
        types.add(t)
        relations.add(r)

    return types, relations
    
with open(path + '/data/ontology/domain_dict', 'r') as f:
    domains = json.load(f)

types, relations = unpack(path + '/data/ontology/fb_roles')

disambig = {
    "types": types,
    "relations": relations
}

confusing_labels = set()
with open(path + "/data/ontology/secondary_domain_disambiguation.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        for t in line.split():
            confusing_labels.add(t) 

def load_data(args):
    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }
    print('Load questions')
    train_set = json.load(open(os.path.join(args.input_dir, 'train.json')))
    val_set = json.load(open(os.path.join(args.input_dir, 'val.json')))
    test_set = json.load(open(os.path.join(args.input_dir, 'val.json')))

    # all_sparqls = []

    for question in chain(train_set, val_set, test_set):
        question['input'] = question.pop('question')
        question['target'] = preprocess_sparql(question, normalize=False, name=True)
    
    if args.ir_mode is None:
        return  train_set, val_set, test_set, vocab
    
    if args.ir_mode == 'graphq':
        from graphq_ir.sparql.translator import Translator
        translator = Translator()
        for question in chain(train_set, val_set, test_set):
            question['target'] = translator.to_ir(preprocess_sparql(question, normalize=True, name=True))
    elif args.ir_mode == 'cfq':
        from cfq_ir import KqaParser
        translator = KqaParser(all_sparqls)
        parser_path = os.path.join(args.output_dir, 'parser.pkl')
        print('Dump CFQ translator to {}'.format(parser_path))
        with open(parser_path, 'wb') as f:
            pickle.dump(translator, f)
        for question in chain(train_set, val_set, test_set):
            question['target'] = translator.f_reversible(question['target'])
    elif args.ir_mode == 'canonical':
        for question in chain(train_set, val_set, test_set):
            question['target'] = preprocess_lisp(question['s_expression'])
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)
        
    return train_set, val_set, test_set, vocab

def preprocess_lisp(item):
    s_expression = item['s_expression']
    for node in item['graph_query']['nodes']:
        if node['id'][1] == "." and node['id'] in s_expression:
            s_expression = s_expression.replace(node['id'], "\"{}\"".format(node['friendly_name']))
    return s_expression

def preprocess_sparql(item, prune=True, normalize=True, name=True):
    sparql = item['sparql_query']

    def pruning(logical_form):
        """
        Eliminates redundant structure in the logical form such as FILTER(?x != ?x_1), etc.
        """
        result = logical_form

        # Match (and substitute if existed) the third SELECT-WHERE chunk
        match = re.search(r'\{\nSELECT \((MAX|MIN)\(\?y\d\) AS \?x\d\)  WHERE \{ \n[\s\S]*\}\n\}(?=\n(\?|.))', result)
        if match is not None:
            order = re.search(r'(?<=SELECT \()(MIN|MAX)(?=\(\?)', result).group(0)
            v = re.search(r'(?<={}\(\?y\d\) AS )(\?x\d)'.format(order), result).group(0)
            result = re.sub(r'\{\nSELECT \((MAX|MIN)\(\?y\d\) AS \?x\d\)  WHERE \{ \n[\s\S]*\}\n\}(?=\n(\?|.))', '',
                            result)

        result = result.replace("SELECT (?x0 AS ?value) WHERE {",
                                "SELECT DISTINCT ?x0 WHERE {")
        result = result.replace("SELECT (COUNT(?x0) AS ?value) WHERE {",
                                "SELECT (COUNT(DISTINCT ?x0) AS ?count) WHERE {")
        result = result.replace("SELECT DISTINCT ?x0  WHERE { \n", "")

        result = re.sub(r'PREFIX [a-zA-Z]*: \<.*\> \n', '', result)
        result = result[:-2] # Remove the redundant \} at the last

        if match is not None:
            query_var = re.search(r'(?<=DISTINCT )\?[a-z](_)?\d?', result).group(0)
            result = re.sub(r'(?<=DISTINCT )\?[a-z](_)?\d?', "{},{}".format(query_var, v), result)

            if order == 'MIN':
                result = result + ' ORDER BY {} LIMIT 1'.format(v)
            else:
                result = result + ' ORDER BY DESC({}) LIMIT 1'.format(v)

        return result

    def normalizing(logical_form):
        result = logical_form
        pv_count, cls_count, v_count = 0, 0, 0
        var_mapping, cls_mapping = {}, {}

        # deleate extra filter
        result = re.sub(r'FILTER \( \?x\d \!\= \?.*\n', '', result)

        # delete extra variables
        qvar = re.search(r'(?<=DISTINCT\s)[^\s]*(?=\s)', result).group(0)
        new_qvar = qvar.split(',')[0]
        result = result.replace(qvar, new_qvar)

        # normalizing Class triples
        result = result.replace(":type.object.type", "<pred:instance_of>")
        cls_labels = set(re.findall(r'(?<=\<pred:instance_of\> ):[a-zA-Z\._\d]*(?= \.)', result))
        for label in cls_labels:
            if label not in cls_mapping.keys():
                cls_var = "?c_{}".format(cls_count).replace("_0", "")
                cls_mapping[label] = cls_var
                cls_count += 1
            else:
                cls_var = cls_mapping[label]
            result = re.sub(r'{}(?= \.)'.format(label), cls_var, result)
            result = re.subn(r'(?<={}\s\.\s)\n'.format(cls_var.strip('?')),
                             '\n{} <pred:name> {} . \n'.format(cls_var, label),
                             result, 1)[0]

        # normalizing VALUE
        values = re.findall(r'VALUES\s.*\n', result)
        for value in values:
            _, head, _, tail, _ = value.split()
            replaced = False
            for key in uri2abbr.keys():
                if key in tail:
                    tail = tail.replace(key, uri2abbr[key])
                    replaced = uri2abbr[key][4:] # striping "xsd:"

            if replaced:
                result = re.sub(re.escape(value), '{} <pred:{}> {} . \n'.format(head, replaced, tail), result)
                result = re.sub(re.escape(head), "?pv_{}".format(pv_count).replace("_0", ""), result)
                pv_count += 1
            else:
                result = re.sub(re.escape(value), "{} <pred:name> {} . \n".format(head, tail), result)

        # normalizing variable names
        variables = set(re.findall(r'\?x\d', result))
        for var in variables:
            new_var = var.replace("x", "e_").replace("_0", "")
            result = re.sub(re.escape(var), new_var, result)

        # normalizing predicates
        for node in item['graph_query']['edges']:
            if f" :{node['relation']} " in result:
                result = result.replace(f" :{node['relation']} ", " <{}> ".format(
                    re.sub(r'[\"\:\n]', '', node['relation'].split('.', 1)[-1].replace('.', '_'))
                ))
        # preds = set(re.findall(r':[a-zA-Z\._]*(?= \?)', result))
        # for pred in preds:
        #     new_pred = pred.split('.')[-2] + "_" + pred.split('.')[-1]
        #     new_pred = "<{}>".format(new_pred)
        #     result = result.replace(pred, new_pred)

        # normalizing ORDERBY entity
        if "ORDER BY" in result:
            restricted_var = re.search(r'\?e(_)\d(?=(\))? LIMIT 1)', result).group(0)
            pv_var = '?pv_{}'.format(pv_count).replace('_0', '')
            v_var = '?v_{}'.format(pv_count).replace('_0', '')
            v_triple = "\n{} <pred:value> {} . \n".format(pv_var, v_var)
            result = re.sub(r'\?e(_)\d(?=(\))? LIMIT 1)', v_var, result)
            result = result.replace(restricted_var, pv_var)
            result = re.subn(r'(?<={} \. )\n'.format(re.escape(pv_var)), v_triple, result, 1)[0]
            pv_count += 1
            v_count += 1
        
        # normalizing FILTER
        for key in uri2abbr.keys():
            if key in result:
                result = result.replace(key, uri2abbr[key])
        
        filt_var = re.search(r'(?<=FILTER \()\?[a-z](_)?\d?', result)
        if filt_var is not None:
            filt_var = filt_var.group(0)
            pv_var = '?pv_{}'.format(pv_count).replace('_0', '')
            v_var = '?v_{}'.format(pv_count).replace('_0', '')
            v_triple = "\n{} <pred:value> {} . \n".format(pv_var, v_var)
            result = re.sub(r'(?<=FILTER \()\?[a-z](_)?\d?', v_var, result)
            result = result.replace(filt_var, pv_var)
            result = re.subn(r'(?<={} \. )\n'.format(re.escape(pv_var)), v_triple, result, 1)[0]

        return result.replace("\n", " ")

    def naming(logical_form):
        result = logical_form
        if normalize:
            for node in item['graph_query']['nodes']:
                if f" :{node['id']} " in result and node['node_type'] == 'entity':
                    result = result.replace(f" :{node['id']} ", " \"{}\" ".format(
                        re.sub(r'[\"\:\n]', '', node['friendly_name'])))
                elif f" :{node['id']} " in result and node['node_type'] == 'class':
                    if node["id"] in confusing_labels:
                        result = result.replace(f" :{node['id']} ", " \"{}\" ".format(
                            re.sub(r'[\"\:\n]', '', node['id'].replace('_', ' '))
                            # re.sub(r'[\"\:\n]', '', node['friendly_name'])))
                        ))
                    else:
                        result = result.replace(f" :{node['id']} ", " \"{}\" ".format(
                            re.sub(r'[\"\:\n]', '', node['id'].split('.', 1)[-1].replace('_', ' '))
                            # re.sub(r'[\"\:\n]', '', node['friendly_name'])))
                        ))
        else:
            result = re.sub(r'VALUES (\?.*?) \{ :(.*?)\}', r'\1 :type.object.name \2 .', result)
            for node in item['graph_query']['nodes']:
                if f" {node['id']} " in result and node['node_type'] == 'entity':
                    result = result.replace(f" {node['id']} ", " \"{}\"@en ".format(
                        re.sub(r'[\"\:\n]', '', node['friendly_name'])
                    ))
            
        return result

    sparql = pruning(sparql) if prune else sparql
    sparql = normalizing(sparql) if normalize else sparql
    sparql = naming(sparql) if name else sparql
    return sparql.replace("\n", "")


def postprocess_sparql(sparql: str, domains: dict, disambiguate: dict):
    assert "types", "relations" in domains.keys()

    def find_id(s: str, k: str):
        assert k in ["types", "relations"]
        ids = []
        s = s.replace('.', '_')
        for key in domains.keys():
            for ent_id in domains[key]:
                if ent_id.split('.', 1)[1].replace(".", "_") == s:
                    ids.append(ent_id)
                if ent_id.replace(".", "_") == s:
                    ids.append(ent_id)

        if len(ids) != 1:
            for eid in ids:
                if eid in disambiguate[k]:
                    return eid
        try:
            return ids[0]
        except IndexError:
            raise IndexError

    def get_pv_var(v: str, query: str):
        pv_var = re.search(r"\?pv_?\d?(?=\s<pred:value>\s{})".format(re.escape(v)), query)
        return pv_var.group(0) if pv_var else ""

    # Adding prefix
    prefix = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX : <http://rdf.freebase.com/ns/> "
    sparql = prefix + sparql

    # postprocess naming conventions
    sparql = sparql.replace("<pred:instance_of>", ":type.object.type")
    sparql = sparql.replace("<pred:name>", ":type.object.name")

    # postprocess concept
    cls_vars = set(re.findall(r'(?<=:type\.object\.type\s)\?c_?\d?', sparql))
    for cls_var in cls_vars:
        cls_label = re.search(r'(?<={}\s:type\.object\.name\s\")[^\"]*(?=\")'.format(re.escape(cls_var)), sparql)
        assert cls_label is not None
        cls_label = cls_label.group(0)
        try:
            cls_id = ":" + find_id(cls_label.replace(" ", "_"), "types")
        except TypeError:
            print(cls_label)
            raise Exception
        sparql = re.sub(r"\s*\.\s*{}\s*:type\.object\.name\s*\"{}\"".format(re.escape(cls_var), cls_label), "", sparql)
        sparql = re.sub(r"{}(?=\s|\.)".format(re.escape(cls_var)), cls_id, sparql)

    # postprocess relation
    rel_labels = re.findall(r'(?<=\<)[a-zA-Z\_\d]*(?=>)', sparql)
    for rel_label in rel_labels:
        rel_id = ":" + find_id(rel_label, "relations")
        sparql = sparql.replace("<{}>".format(rel_label), rel_id)

    # postprocess entity name
    ent_labels = re.findall(r':type\.object\.name\s*\"[^\"]*\"', sparql)
    for ent_label in ent_labels:
        sparql = sparql.replace(ent_label, ent_label + "@en")

    # postprocess pv-v pattern
    val_vars = set(re.findall(r"\?v_?\d?", sparql))
    for val_var in val_vars:
        pv_var = get_pv_var(val_var, sparql)
        if "ORDER BY" in sparql:
            sparql = re.sub("(?<=ORDER BY ){}".format(re.escape(val_var)), pv_var, sparql)
            sparql = re.sub("(?<=ORDER BY DESC\(){}".format(re.escape(val_var)), pv_var, sparql)
        sparql = re.sub(r"\.\s*{}\s*\<pred:value\>\s*{}\s*(?=\.)".format(re.escape(pv_var), re.escape(val_var)),
                        "", sparql)
        sparql = re.sub(r"{}(?=\s|\<|\>|\!|\=|\.)".format(re.escape(val_var)), pv_var, sparql)

    # postprocess VALUES
    val_trips = re.findall(r"\?[a-z]*_?\d?\s*\<pred:[a-zA-Z]*\>\s*\"[^\"]*\"\^\^xsd:[a-zA-Z]*\s*\.", sparql)
    for val_trip in val_trips:
        for key in abbr2uri.keys():
            if key in val_trip:
                new_val_trip = val_trip.replace(key, abbr2uri[key])
                var, _, val, _ = new_val_trip.split()
                new_val_trip = f"VALUES {var}" + " { " + val + " }"
                sparql = sparql.replace(val_trip, new_val_trip)
                break

    # postprocess FILTER
    filters = re.findall(r"FILTER\s*\([^\)]*\)", sparql)
    for ft in filters:
        for key in abbr2uri.keys():
            if key in ft:
                new_ft = ft.replace(key, abbr2uri[key])
                sparql = sparql.replace(ft, new_ft)
                break

    # remove the unit "1"
    sparql = re.sub(r"\s*\?[a-z]*_?\d?\s*\<pred:unit\>\s*\"1\"\s*\.", "", sparql)

    # postprocess disjoint filter
    variables = set(re.findall(r'\?[a-z]*_?\d?', sparql))
    if "?count" in variables:
        variables.remove("?count")
    if "?" in variables:
        variables.remove("?")
    
    vpairs = []
    fil = ""
    for v1 in variables:
        for v2 in variables:
            if v1 != v2 and (v1, v2) not in vpairs and (v2, v1) not in vpairs:
                vpairs.append((v1, v2))

    for v1, v2 in vpairs:
        fil = fil + "{} != {}".format(v1, v2) + " && "

    fil = fil[:-3] # remove the extra &&\s
    fil = "FILTER ( {} )".format(fil)
    # EOT = re.search(r"(?<=\.)[^\.]*$", sparql).group(0)
    sparql = re.sub(r"\.(?=\s)", ". {} ".format(fil), sparql, count=1)

    # postprocess query chain
    if "ORDER BY" in sparql:
        if "DESC" in sparql:
            query_var = re.search(r"(?<=ORDER BY DESC\()\?[a-z]*_?\d?", sparql).group(0)
        else:
            query_var = re.search(r"(?<=ORDER BY )\?[a-z]*_?\d?", sparql).group(0)

        sparql = re.sub(r'(SELECT DISTINCT|SELECT) ?(\?[a-z]_?\d?)', r'\1 \2,{}'.format(query_var), sparql)
        


    return sparql


def evaluate(args, outputs, targets, *xargs):
    assert len(outputs) == len(targets)
    correct = 0
    category_correct = {'i.i.d.': 0, 'zero-shot': 0, 'compositional': 0}
    category_count = {'i.i.d.': 0, 'zero-shot': 0, 'compositional': 0}
    categories = [item['level'] for item in json.load(open("./data/grailqa/data/val.json"))]
    for pred, gold, category in zip(outputs, targets, categories):
        if args.ir_mode == 'graphq':
            if pred == gold:
                correct += 1
                category_correct[category] += 1
            category_count[category] += 1
        else:
            try:
                pred = execute_query(('''PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX : <http://rdf.freebase.com/ns/> {}'''.format(pred)))
            except:
                continue
            gold = execute_query(('''PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX : <http://rdf.freebase.com/ns/> {}'''.format(gold)))
            pred.sort()
            gold.sort()
            if set(pred) == set(gold):
                correct += 1
                category_correct[category] += 1
            category_count[category] += 1
    for key in category_correct.keys():
        print(f"{key} accuracy: {category_correct[key] / category_count[key]}")
    return correct / len(outputs)
    
