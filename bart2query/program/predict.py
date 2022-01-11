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

def validate(args, kb, model, data, device, tokenizer):
    model.eval()
    model = model.module if hasattr(model, "module") else model

    if "new" in args.input_dir:
        from .executor_rule_new import RuleExecutor 
        executor = RuleExecutor(os.path.join("./data/kqapro/dataset_new/", 'kb.json'))
    else:
        from .executor_rule import RuleExecutor 
        executor = RuleExecutor(os.path.join("./data/kqapro/dataset_full/", 'kb.json'))

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
        given_answer = [data.vocab['answer_idx_to_token'][a] for a in all_answers]
        
        for a, output in tqdm(zip(given_answer, outputs)):
            func_list, inputs_list = sequence_to_program(output)
            ans = executor.forward(func_list, inputs_list, ignore_error = True)
            if ans == None:
                ans = 'no'
            if ans == a:
                correct += 1
            count += 1
        
        acc = correct / count
        logging.info('acc: {}'.format(acc))
        return acc, outputs

def predict(args, kb, model, data, device, tokenizer):
    model.eval()
    model = model.module if hasattr(model, "module") else model

    if "new" in args.input_dir:
        from .executor_rule_new import RuleExecutor 
        executor = RuleExecutor(os.path.join("./data/kqapro/dataset_new/", 'kb.json'))
    else:
        from .executor_rule import RuleExecutor 
        executor = RuleExecutor(os.path.join("./data/kqapro/dataset_full/", 'kb.json'))

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
        with open(os.path.join(args.save_dir, 'predict.txt'), 'w') as f:
            for output in tqdm(outputs):
                func_list, inputs_list = sequence_to_program(output)
                ans = executor.forward(func_list, inputs_list, ignore_error = True)
                if ans == None:
                    ans = 'no'
                f.write(ans + '\n')
