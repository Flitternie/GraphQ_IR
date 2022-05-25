from enum import auto
import os
import re
import json
import pickle

import numpy as np
from itertools import chain

from data.grailqa.utils.sparql_executer import *

special_tokens = []
domains = []

dtype = {
        "<http://www.w3.org/2001/XMLSchema#float>": "xsd:float",
        "<http://www.w3.org/2001/XMLSchema#integer>": "xsd:int",
        "<http://www.w3.org/2001/XMLSchema#gYear>": "xsd:year",
        "<http://www.w3.org/2001/XMLSchema#gYearMonth>": "xsd:date",
        "<http://www.w3.org/2001/XMLSchema#date>": "xsd:date",
        "<http://www.w3.org/2001/XMLSchema#dateTime>": "xsd:time"
    }


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
        pv_count = 0

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
            v_chain = []
            edge = re.search(r'(?<=\n)\?.* [a-zA-Z\_\:\.]* {}(?= \. \n)'.format(re.escape(v)), result)
            while edge is not None:
                edge = edge.group(0)
                hop_var = edge.split()[0]
                v_chain.append(hop_var)
                edge = re.search(r'(?<=\n)\?.* [a-zA-Z\_\:\.]* {}(?= \. \n)'.format(re.escape(hop_var)), result)

            v_chain.reverse()
            new_query = ','.join(v_chain)
            result = re.sub(r'(?<=DISTINCT )\?[a-z](_)?\d?', new_query, result)

            if order == 'MIN':
                result = result + ' ORDER BY {} LIMIT 1'.format(v)
            else:
                result = result + ' ORDER BY DESC({}) LIMIT 1'.format(v)

        return result

    def normalizing(logical_form):
        result = logical_form
        pv_count, cls_count = 0, 0
        var_mapping, cls_mapping = {}, {}

        # deleate extra filter
        result = re.sub(r'FILTER \( \?x\d \!\= \?.*\n', '', result)

        # delete extra variables
        qvar = re.search(r'(?<=DISTINCT\s)[^\s]*(?=\s)', result).group(0)
        new_qvar = qvar.split(',')[0]
        result = result.replace(qvar, new_qvar)

        # normalizing Class triples
        result = result.replace(":type.object.type", "<pred:instance_of>")
        cls_labels = re.findall(r'(?<=\<pred:instance_of\> ):[a-zA-Z\._]*(?= \.)', result)
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
            for key in dtype.keys():
                if key in tail:
                    tail = tail.replace(key, dtype[key])
                    replaced = dtype[key][4:] # striping "xsd:"

            if replaced:
                result = re.sub(re.escape(value), '{} <pred:{}> {} . \n'.format(head, replaced, tail), result)
                result = re.sub(re.escape(head), "?pv_{}".format(pv_count).replace("_0", ""), result)
                pv_count += 1
            else:
                result = re.sub(re.escape(value), "{} <pred:name> {} . \n".format(head, tail), result)

        # normalizing FILTER
        for key in dtype.keys():
            if key in result:
                result = result.replace(key, dtype[key])

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
            v_triple = "\n{} <pred:value> ?v . \n".format(pv_var)
            result = re.sub(r'\?e(_)\d(?=(\))? LIMIT 1)', '?v', result)
            result = result.replace(restricted_var, pv_var)
            result = re.subn(r'(?<={} \. )\n'.format(re.escape(pv_var)), v_triple, result, 1)[0]
            pv_count += 1

        return result

    def naming(logical_form):
        result = logical_form
        if normalize:
            for node in item['graph_query']['nodes']:
                if f" :{node['id']} " in result and node['node_type'] == 'entity':
                    result = result.replace(f" :{node['id']} ", " \"{}\" ".format(
                        re.sub(r'[\"\:\n]', '', node['friendly_name'])))
                elif f" :{node['id']} " in result and node['node_type'] == 'class':
                    result = result.replace(f" :{node['id']} ", " \"{}\" ".format(
                        re.sub(r'[\"\:\n]', '', node['id'].split('.', 1)[-1].replace('_', ' '))
                        # re.sub(r'[\"\:\n]', '', node['friendly_name'])))
                    ))
        else:
            for node in item['graph_query']['nodes']:
                if f" :{node['id']} " in result and node['node_type'] == 'entity':
                    result = result.replace(f" :{node['id']} ", " \"{}\"@en ".format(
                        re.sub(r'[\"\:\n]', '', node['friendly_name'])
                    ))

            result = re.sub(r'VALUES (\?.*?) \{(.*?)\}', r'\1 :type.object.name \2 .', result)
        return result

    sparql = pruning(sparql) if prune else sparql
    sparql = normalizing(sparql) if normalize else sparql
    sparql = naming(sparql) if name else sparql
    return sparql.replace("\n", "")

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
    