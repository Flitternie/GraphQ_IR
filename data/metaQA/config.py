import os
import json
import numpy as np
# from neo4j import GraphDatabase, basic_auth

def load_metaqa(args):
    print('Build kb vocabulary')
    vocab = {
        'answer_token_to_idx': {}
    }

    print('Load questions')
    train_set = json.load(open(os.path.join(args.input_dir, 'train.json')))
    val_set = json.load(open(os.path.join(args.input_dir, 'val.json')))
    test_set = json.load(open(os.path.join(args.input_dir, 'test.json')))
    
    return train_set, val_set, test_set, vocab

def evaluate(args, outputs, targets, *xargs):
    """     
    scores = []
    driver = GraphDatabase.driver(
            "bolt://34.205.75.182:7687",
            auth=basic_auth("neo4j", "computer-tractor-distortions"))

    for output, target, answer in tqdm(zip(outputs, targets, given_answer)):
        if output == target:
            scores.append(1)
        else:
            try:   
                with driver.session(database="neo4j") as session:
                    results = session.read_transaction(lambda tx: tx.run(output).data())
                    results = [record.values() for record in results]
            except:
                results = []    
            if ";".join(results) == answer:
                scores.append(1)
            else:
                scores.append(0) 
    """
    assert len(outputs) == len(targets)
    return np.mean([1 if p.strip().lower() == g.strip().lower() else 0 for p, g in zip(outputs, targets)])


def translate(args, outputs, targets):
    if args.ir_mode == 'graphq':
        translated_outputs = []
        translated_targets = []
        from graphq_ir.ir.translator import Translator
        translator = Translator()
        for output, target in zip(outputs, targets):
            try:
                translated_outputs.append(translator.to_cypher(output))
            except:
                translated_outputs.append("")
            translated_targets.append(translator.to_cypher(target))
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)
    return translated_outputs, translated_targets
