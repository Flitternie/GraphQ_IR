import os
import torch
import pickle
from tqdm import tqdm
from datetime import date
from .sparql_engine import get_sparql_answer
import logging
import re
import numpy as np

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

def evaluate(args, given_answer, outputs, kb):
    count, correct = 0, 0
    pred_answers = []
    for a, s in tqdm(zip(given_answer, outputs)):
        pred_answer = get_sparql_answer(s, kb)
        if pred_answer == None:
            pred_answer = 'no'
        is_match = whether_equal(a, pred_answer)
        if is_match:
            correct += 1
        count += 1
        pred_answers.append(pred_answer)

    with open(os.path.join(args.output_dir, 'pred_answers.txt'), 'w') as f:
        for a in pred_answers:
            f.write('{}\n'.format(a))
    return correct / count

def string_matching_evaluate(outputs, targets):
    return np.mean([1 if p.strip() == g.strip() else 0 for p, g in zip(outputs, targets)])

def translate(args, outputs):
    if args.ir_mode == 'UIR':
        from parser.ir.translator import Translator    
        translator = Translator()
        if args.self_correct:
            from IR_unified.corrector import Corrector
            corrector = Corrector()
        translated_outputs = []
        for output in outputs:
            try:
                output = corrector.correct(output) if args.self_correct else output
                output = translator.to_sparql(output).replace('  ?', ' ?')
                translated_outputs.append(output)
            except Exception as e:
                translated_outputs.append("")
    elif args.ir_mode == 'CFQ_IR':
        try:
            with open(os.path.join(args.input_dir, 'parser.pkl'), 'rb') as f:
                parser = pickle.load(f)
        except:
            raise Exception('Parser not found')
        translated_outputs = [parser.f_reversible_inverse(sparql) for sparql in outputs]
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)

    return translated_outputs

def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    model = model.module if hasattr(model, "module") else model
    
    count, correct = 0, 0
    with torch.no_grad():
        all_outputs = []
        all_targets = []
        all_answers = []
        for batch in tqdm(data, total=len(data)):
            source_ids, source_mask, choices, target_ids, answer = [x.to(device) for x in batch]
            outputs = model.generate(
                input_ids=source_ids,
                max_length = 500,
            )
            all_outputs.extend(outputs.cpu().numpy())
            all_targets.extend(target_ids.cpu().numpy())
            all_answers.extend(answer.cpu().numpy())
            
        outputs = [tokenizer.decode(output_id, skip_special_tokens = True, clean_up_tokenization_spaces = True) for output_id in all_outputs]
        targets = [tokenizer.decode(target_id, skip_special_tokens = True, clean_up_tokenization_spaces = False) for target_id in all_targets]
        if ( not args.ir_mode ) or args.ir_mode == 'CFQ_IR':
            outputs = [post_process(output) for output in outputs]
        if args.ir_mode:
            with open(os.path.join(args.output_dir, 'pred_ir.txt'), 'w') as f:
                for output in outputs:
                    f.write('{}\n'.format(output))
            outputs = translate(args, outputs)    
        given_answer = [data.vocab['answer_idx_to_token'][a] for a in all_answers]
        
    acc = evaluate(args, given_answer, outputs, kb) 
    # acc = string_matching_evaluate(outputs, targets)
    logging.info('acc: {}'.format(acc))
    
    return acc, outputs
