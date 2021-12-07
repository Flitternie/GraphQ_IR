import os
import torch
import json
from tqdm import tqdm
from utils.data import DataLoader
from transformers import BartConfig, BartForConditionalGeneration, BartTokenizer
import logging

from nltk.translate.bleu_score import sentence_bleu

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query

def post_process_ir(ir):
    for token in ["<E>","</E>","<ES>","</ES>","<A>","</A>","<R>","</R>","<V>","</V>","<Q>","</Q>","<C>","</C>"]:
        ir = ir.replace(" {}".format(token), token)
        ir = ir.replace("{} ".format(token), token)
    return ir

def cal_performance(pred, gold, tokenizer):
    batch_bleu = 0.0
    batch_correct = 0
    for x, y in zip(pred, gold):
        y = tokenizer.decode(y, skip_special_tokens = True, clean_up_tokenization_spaces = True)
        x = tokenizer.decode(x, skip_special_tokens = True, clean_up_tokenization_spaces = True)
        batch_bleu += sentence_bleu([y], x)
        batch_correct += x==y
    return batch_bleu, batch_correct

def exec_performance(pred_irs, kb):
    from parser.ir.SparqlTranslator import Sparql_translator
    from bart2query.sparql.sparql_engine import get_sparql_answer
    from bart2query.sparql.predict import whether_equal, post_process
    
    gold_data = json.load(open("./data/kqapro/dataset_new/test.json"))
    pred_irs = [post_process_ir(ir) for ir in pred_irs]
    
    assert len(pred_irs) == len(gold_data)
    translator = Sparql_translator()
    pred_sparqls = [translator.ir_to_sparql(ir) for ir in pred_irs]
    
    count, correct = 0, 0
    for s, d in tqdm(zip(pred_sparqls, gold_data)):
        pred_answer = get_sparql_answer(s, kb)
        gold_answer = get_sparql_answer(d["sparql"], kb)
        is_match = whether_equal(gold_answer, pred_answer)
        if is_match:
            correct += 1
        count += 1

    acc = correct / count
    print('acc: {}'.format(acc))
    return acc


def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    all_outputs = []
    all_targets = []
    with torch.no_grad():
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, choices, target_ids, answer = [x.to(device) for x in batch]
            outputs = model.module.generate(
                input_ids=source_ids,
                max_length = 500,
            ) if hasattr(model, "module") else model.generate(
                input_ids=source_ids,
                max_length = 500,
            ) 

            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            
        assert len(all_outputs) == len(all_targets) 
        all_bleu, all_correct = cal_performance(all_outputs, all_targets, tokenizer)
        acc = all_correct/len(all_outputs)
        avg_bleu = all_bleu/len(all_outputs)
        logging.info('accuracy: {}, bleu: {}'.format(acc, avg_bleu))

        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for output_id in all_outputs]
        # targets = [tokenizer.decode(target_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for target_id in all_targets]
        # exec_acc = exec_performance(outputs, kb)
        # logging.info('execution accuracy: {}'.format(exec_acc))
    
    return acc, outputs


def predict(args, kb, model, data, device, tokenizer):
    all_outputs = []
    all_targets = []
    with torch.no_grad():
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, choices, target_ids, answer = [x.to(device) for x in batch]
            outputs = model.module.generate(
                input_ids=source_ids,
                max_length = 500,
            ) if hasattr(model, "module") else model.generate(
                input_ids=source_ids,
                max_length = 500,
            ) 

            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            
        assert len(all_outputs) == len(all_targets) 
        all_bleu, all_correct = cal_performance(all_outputs, all_targets, tokenizer)
        acc = all_correct/len(all_outputs)
        avg_bleu = all_bleu/len(all_outputs)
        logging.info('accuracy: {}, bleu: {}'.format(acc, avg_bleu))

        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for output_id in all_outputs]
    
    with open(os.path.join(args.save_dir, 'predict.txt'), 'w') as f:
        for output in tqdm(outputs):
            f.write(output + '\n')
    
def prepare(dataset, args):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    print("Preparing %s data........." % dataset)
    vocab_json = os.path.join(args.input_dir, 'vocab.json')
    val_pt = os.path.join(args.input_dir, '%s.pt' % dataset)
    val_loader = DataLoader(vocab_json, val_pt, args.batch_size)
    
    config_class, model_class, tokenizer_class = (BartConfig, BartForConditionalGeneration, BartTokenizer)
    tokenizer = tokenizer_class.from_pretrained(args.model_name_or_path)
    model = model_class.from_pretrained(args.ckpt)
    model.resize_token_embeddings(len(tokenizer))
    model = model.to(device)
    
    _, outputs = validate(args, None, model, val_loader, device, tokenizer)

    return outputs

