import os
import sys
import json
from datetime import date
from collections import defaultdict, Counter

def whether_equal(answer, pred):
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



def main():
    gt_folder, pred_fn = sys.argv[1], sys.argv[2]

    gt_fn = os.path.join(gt_folder, 'test.json')
    gt = json.load(open(gt_fn))
    pred = [x.strip() for x in open(pred_fn).readlines()] # one prediction per line
    gold_answer = [x.strip() for x in open(sys.argv[3]).readlines()]

    # to compute zero-shot accuracy
    train_set = json.load(open(os.path.join(gt_folder, 'train.json')))
    train_answer_set = set(x['answer'] for x in train_set)

    labels = ['overall', 'multihop', 'qualifier', 'comparison', 'logical', 'count', 'verify', 'zero-shot']
    total = {k:0 for k in labels}
    correct = {k:0 for k in labels}
    for i in range(len(pred)):
        cur_labels = ['overall']
        functions = [f['function'] for f in gt[i]['program']]

        for f in functions:
            if f in {'Relate'} or f.startswith('Filter'):
                cur_labels.append('multihop')
                break
        for f in functions:
            if f in {'QFilterStr', 'QFilterNum', 'QFilterYear', 'QFilterDate', 'QueryAttrUnderCondition', 'QueryAttrQualifier', 'QueryRelationQualifier'}:
                cur_labels.append('qualifier')
                break
        for f in functions:
            if f in {'Select','SelectBetween','SelectAmong'}:
                cur_labels.append('comparison')
                break
        for f in functions:
            if f in {'And', 'Or'}:
                cur_labels.append('logical')
                break
        for f in functions:
            if f in {'Count'}:
                cur_labels.append('count')
                break
        for f in functions:
            if f in {'VerifyStr','VerifyNum','VerifyYear','VerifyDate'}:
                cur_labels.append('verify')
                break

        answer = gt[i]['answer']
        # answer = gold_answer[i]
        if answer not in train_answer_set:
            cur_labels.append('zero-shot')

        if whether_equal(answer, pred[i]):
            for k in cur_labels:
                correct[k] += 1
        else:
            # print(i)
            pass
        for k in cur_labels:
            total[k] += 1

    for k in labels:
        print('{}: {:.2f}% ({}/{})'.format(k, correct[k]/total[k]*100, correct[k], total[k]))
    if len(pred) < len(gt):
        print('WARNING: there are only {} predictions (need {})'.format(len(pred), len(gt)))


def acc_by_length():
    gt_folder, pred_fn = sys.argv[1], sys.argv[2]

    gt_fn = os.path.join(gt_folder, 'test.json')
    gt = json.load(open(gt_fn))
    pred = [x.strip() for x in open(pred_fn).readlines()] # one prediction per line

    labels = ['2-3', '4-5', '6-7', '8-9', '10-14']
    mapping = {
        2: '2-3',
    #    3: '2-3',
        4: '4-5',
        5: '4-5',
        6: '6-7',
        7: '6-7',
        8: '8-9',
        9: '8-9',
    }
    correct = defaultdict(int)
    total = defaultdict(int)

    for i in range(len(pred)):
        answer = gt[i]['answer']
        length = len(gt[i]['program'])
        label = mapping.get(length, '10-')

        if whether_equal(answer, pred[i]):
            correct[label] += 1
        total[label] += 1

    for k in labels:
        print('{}: {:.2f}% ({}/{})'.format(k, correct[k]/total[k]*100, correct[k], total[k])) if total[k] > 0 else print('{}: {:.2f}% ({}/{})'.format(k, 0 , correct[k], total[k]))

if __name__ == '__main__':
    main()
    acc_by_length()