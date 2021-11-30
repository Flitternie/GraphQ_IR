import os
import torch
import pickle
from tqdm import tqdm
from datetime import date
from .sparql_engine import get_sparql_answer
import logging
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query

def whether_equal(answer, pred):
    """
    check whether the two arguments are equal as attribute value
    """
    def truncate_float(x):
        # convert answer from '100.0 meters' to '100 meters'
        try:
            v, *u = x.split()
            v = float(v)
            if v - int(v) < 1e-5:
                v = int(v)
            if len(u) == 0:
                x = str(v)
            else:
                x = '{} {}'.format(str(v), ' '.join(u))
        except:
            pass
        return x

    def equal_as_date(x, y):
        # check whether x and y are equal as type of date or year
        try:
            x_split = x.split('-')
            y_split = y.split('-')
            if len(x_split) == 3:
                x = date(int(x_split[0]), int(x_split[1]), int(x_split[2]))
            else:
                x = int(x)
            if len(y_split) == 3:
                y = date(int(y_split[0]), int(y_split[1]), int(y_split[2]))
            else:
                y = int(y)
            if isinstance(x, date) and isinstance(y, date):
                return x == y
            else:
                x = x.year if isinstance(x, date) else x
                y = y.year if isinstance(y, date) else y
                return x == y
        except:
            return False

    answer = truncate_float(answer)
    pred = truncate_float(pred)
    if equal_as_date(answer, pred):
        return True
    else:
        return answer == pred

def post_process(text):
    pattern = re.compile(r'".*?"')
    nes = []
    for item in pattern.finditer(text):
        nes.append((item.group(), item.span()))
    pos = [0]
    for name, span in nes:
        pos += [span[0], span[1]]
    pos.append(len(text))
    assert len(pos) % 2 == 0
    assert len(pos) / 2 == len(nes) + 1
    chunks = [text[pos[i]: pos[i+1]] for i in range(0, len(pos), 2)]
    for i in range(len(chunks)):
        chunks[i] = chunks[i].replace('?', ' ?').replace('.', ' .')
    bingo = ''
    for i in range(len(chunks) - 1):
        bingo += chunks[i] + nes[i][0]
    bingo += chunks[-1]
    return bingo

def vis(args, kb, model, data, device, tokenizer):
    model = model.module if hasattr(model, "module") else model
    while True:
        # text = 'Who is the father of Tony?'
        # text = 'Donald Trump married Tony, where is the place?'
        text = input('Input your question:')
        with torch.no_grad():
            input_ids = tokenizer.batch_encode_plus([text], max_length = 512, pad_to_max_length = True, return_tensors="pt", truncation = True)
            source_ids = input_ids['input_ids'].to(device)
            outputs = model.generate(
                input_ids=source_ids,
                max_length = 500,
            )
            outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for output_id in outputs]
            outputs = [post_process(output) for output in outputs]
            print(outputs[0])

def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    model = model.module if hasattr(model, "module") else model
    
    try:
        with open(args.parser, 'rb') as f:
            parser = pickle.load(f)
        if args.local_rank in [-1, 0]:
            logging.info("IR Parser Loaded")
        ir_mode = args.ir_mode
    except:
        parser = None  
        ir_mode = None
    
    count, correct = 0, 0
    with torch.no_grad():
        all_outputs = []
        all_answers = []
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, choices, target_ids, answer = [x.to(device) for x in batch]
            outputs = model.generate(
                input_ids=source_ids,
                max_length = 500,
            )

            all_outputs.extend(outputs.cpu().numpy())
            all_answers.extend(answer.cpu().numpy())
            
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for output_id in all_outputs]
        pred_sparql = [post_process(output) for output in outputs]
            
        if ir_mode == 'rir':
            pred_sparql = [parser.f_reversible_inverse(sparql) for sparql in pred_sparql]
            
        given_answer = [data.vocab['answer_idx_to_token'][a] for a in all_answers]
        
        with open(os.path.join(args.save_dir, 'predict.txt'), 'w') as f:
            for a, s in tqdm(zip(given_answer, pred_sparql)):
                pred_answer = get_sparql_answer(s, kb)
                
                if pred_answer == None:
                    pred_answer = 'no'
                is_match = whether_equal(a, pred_answer)
                if is_match:
                    correct += 1

                f.write(pred_answer + '\n')
                count += 1

    acc = correct / count
    logging.info('acc: {}'.format(acc))
    return acc, pred_sparql

def predict(args, kb, model, data, device, tokenizer):
    model.eval()
    model = model.module if hasattr(model, "module") else model
    
    if args.parser and args.ir_mode:
        with open(args.parser, 'rb') as f:
            parser = pickle.load(f)
        if args.local_rank in [-1, 0]:
            logging.info("IR Parser Loaded")
    else:
        parser = None  
        ir_mode = None

    with torch.no_grad():
        all_outputs = []
        for batch in tqdm(data, total=len(data)):
            batch = batch[:3]
            source_ids, source_mask, choices = [x.to(device) for x in batch]
            outputs = model.generate(
                input_ids=source_ids,
                max_length = 500,
            )

            all_outputs.extend(outputs.cpu().numpy())
            
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for output_id in all_outputs]
        pred_sparql = [post_process(output) for output in outputs]
        
        if ir_mode == 'rir':
            pred_sparql = [parser.f_reversible_inverse(sparql) for sparql in pred_sparql]

        with open(os.path.join(args.save_dir, 'predict.txt'), 'w') as f:
            for sparql in tqdm(pred_sparql):
                pred_answer = get_sparql_answer(sparql, kb)

                if pred_answer == None:
                    pred_answer = 'None'
                f.write(pred_answer + '\n')

