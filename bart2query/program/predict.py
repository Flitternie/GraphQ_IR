import os
import torch
from tqdm import tqdm
import logging
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s')
logFormatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rootLogger = logging.getLogger()
import warnings
warnings.simplefilter("ignore") # hide warnings that caused by invalid sparql query


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

def sequence_to_program(input):
    chunks = input.split('<b>')
    func_list = []
    inputs_list = []
    pattern = re.compile(r'(.*?)\((.*?)\)')
    for chunk in chunks:
        res = pattern.findall(chunk)
        if len(res) == 0:
            continue
        res = res[0]
        func, inputs = res[0], res[1]
        if inputs == '':
            inputs = []
        else:
            inputs = inputs.split('<c>')
        
        func_list.append(func)
        inputs_list.append(inputs)
    return func_list, inputs_list

def evaluate(args, given_answer, outputs):
    from .executor_rule_new import RuleExecutor 
    executor = RuleExecutor(os.path.join("./data/kqapro/dataset_new/", 'kb.json'))
    count, correct = 0, 0

    for a, output in tqdm(zip(given_answer, outputs)):
        func_list, inputs_list = sequence_to_program(output)
        ans = executor.forward(func_list, inputs_list, ignore_error = True)
        if ans == None:
            ans = 'no'
        if ans == a:
            correct += 1
        count += 1
    acc = correct / count
    return acc

def translate(args, outputs):
    if args.mode == 'UIR':
        from parser.ir.translator import Translator
        translator = Translator()
        translated_outputs = []
        for output in outputs:
            try:
                translated_outputs.append(translator.to_program(output))
            except:
                translated_outputs.append("")
    else:
        raise NotImplementedError("%s not supported" % args.ir_mode)

    return translated_outputs

def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    model = model.module if hasattr(model, "module") else model    
    
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
        given_answer = [data.vocab['answer_idx_to_token'][a] for a in all_answers]
    
    if args.ir_mode:
        otuputs = translate(args, outputs)
    acc = evaluate(args, given_answer, outputs)
    logging.info('acc: {}'.format(acc))
    
    return acc, outputs
