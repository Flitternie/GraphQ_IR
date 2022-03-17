import os
import random
import torch
import numpy as np
from tqdm import tqdm
from utils.data import DataLoader
from transformers import BartConfig, BartForConditionalGeneration, BartTokenizer
import logging
from neo4j import GraphDatabase, basic_auth

from data.overnight.domain.domain_base import Domain

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") 


def evaluate(outputs, targets, given_answer):
    assert len(outputs) == len(targets)
    # scores = []
    # driver = GraphDatabase.driver(
    #         "bolt://34.205.75.182:7687",
    #         auth=basic_auth("neo4j", "computer-tractor-distortions"))

    # for output, target, answer in tqdm(zip(outputs, targets, given_answer)):
    #     if output == target:
    #         scores.append(1)
    #     else:
    #         try:   
    #             with driver.session(database="neo4j") as session:
    #                 results = session.read_transaction(lambda tx: tx.run(output).data())
    #                 results = [record.values() for record in results]
    #         except:
    #             results = []    
    #         if ";".join(results) == answer:
    #             scores.append(1)
    #         else:
    #             scores.append(0)

    return np.mean([1 if p.strip().lower() == g.strip().lower() else 0 for p, g in zip(outputs, targets)]), np.mean([1 if p.strip() == g.strip() else 0 for p, g in zip(outputs, targets)])


def translate(args, outputs, targets):
    if args.ir_mode == 'UIR':
        translated_outputs = []
        translated_targets = []
        from parser.ir.translator import Translator
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


def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    all_outputs = []
    all_targets = []
    all_answers = []
    with torch.no_grad():
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, _, target_ids, answers = [x.to(device) for x in batch]
            outputs = model.module.generate(
                input_ids=source_ids,
                max_length = 500,
            ) if hasattr(model, "module") else model.generate(
                input_ids=source_ids,
                max_length = 500,
            ) 

            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            all_answers.extend(answers.cpu().numpy())
            
        assert len(all_outputs) == len(all_targets) 
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for output_id in all_outputs]
        targets = [tokenizer.decode(target_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for target_id in all_targets]
        # given_answer = [data.vocab['answer_idx_to_token'][a] for a in all_answers]
        given_answer = None

    if args.ir_mode:
        outputs, targets = translate(args, outputs, targets)
    lf_matching, str_matching = evaluate(outputs, targets, given_answer)
    logging.info('Execution accuracy: {}, String matching accuracy: {}'.format(lf_matching, str_matching))

    with open("out.txt", "w") as f:
        for output, target in zip(outputs, targets):
            f.write("{}\t{}\n".format(output, target))

    return lf_matching, outputs
