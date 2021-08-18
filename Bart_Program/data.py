import json
from logging import basicConfig
import pickle
import torch
from utils.misc import invert_dict

def load_vocab(path):
    vocab = json.load(open(path))
    vocab['answer_idx_to_token'] = invert_dict(vocab['answer_token_to_idx'])
    return vocab

def collate(batch):
    batch = list(zip(*batch))
    source_ids = torch.stack(batch[0])
    source_mask = torch.stack(batch[1])
    choices = torch.stack(batch[2])
    if batch[-1][0] is None:
        target_ids, answer = None, None
    else:
        target_ids = torch.stack(batch[3])
        answer = torch.cat(batch[4])
    return source_ids, source_mask, choices, target_ids, answer

def collate_pretrain(batch):
    batch = list(zip(*batch))
    source_ids = torch.stack(batch[0])
    source_mask = torch.stack(batch[1])
    if batch[-1][0] is None:
        target_ids = None
    else:
        target_ids = torch.stack(batch[2])
    return source_ids, source_mask, target_ids


class Dataset(torch.utils.data.Dataset):
    def __init__(self, inputs, pretrain=False):
        self.pretrain = pretrain
        if not self.pretrain:
            self.source_ids, self.source_mask, self.target_ids, self.choices, self.answers = inputs
            self.is_test = len(self.answers)==0
        else:
            self.source_ids, self.source_mask, self.target_ids = inputs
            self.is_test = False

    def __getitem__(self, index):
        source_ids = torch.LongTensor(self.source_ids[index])
        source_mask = torch.LongTensor(self.source_mask[index])
        if not self.pretrain:
            choices = torch.LongTensor(self.choices[index])
            if self.is_test:
                target_ids = None
                answer = None
            else:
                target_ids = torch.LongTensor(self.target_ids[index])
                answer = torch.LongTensor([self.answers[index]])
            return source_ids, source_mask, choices, target_ids, answer
        else:
            target_ids = torch.LongTensor(self.target_ids[index])
            return  source_ids, source_mask, target_ids

    def __len__(self):
        return len(self.source_ids)

class DataLoader(torch.utils.data.DataLoader):
    def __init__(self, vocab_json, question_pt, batch_size, training=False, pretrain=False):
        vocab = load_vocab(vocab_json)
        if training:
            print('#vocab of answer: %d' % (len(vocab['answer_token_to_idx'])))
        
        inputs = []
        input_len = 5 if not pretrain else 3
        with open(question_pt, 'rb') as f:
            for _ in range(input_len):
                inputs.append(pickle.load(f))
        dataset = Dataset(inputs, pretrain)
        # np.shuffle(dataset)
        # dataset = dataset[:(int)(len(dataset) / 10)]
        if not pretrain:
            super().__init__(
                dataset, 
                batch_size=batch_size,
                shuffle=training,
                collate_fn=collate, 
                )
        else:
            super().__init__(
                dataset, 
                batch_size=batch_size,
                shuffle=training,
                collate_fn=collate_pretrain, 
                )
        self.vocab = vocab


def prepare_dataset(vocab_json, question_pt, training=False, pretrain=False):
    vocab = load_vocab(vocab_json)
    if training:
        print('#vocab of answer: %d' % (len(vocab['answer_token_to_idx'])))
    
    inputs = []
    input_len = 5 if not pretrain else 3
    with open(question_pt, 'rb') as f:
        for _ in range(input_len):
            inputs.append(pickle.load(f))
    dataset = Dataset(inputs, pretrain)
    return dataset, vocab

class DistributedDataLoader(torch.utils.data.DataLoader):
    def __init__(self, dataset, vocab, batch_size, sampler, pretrain=False):
        self.vocab = vocab
        self.sampler = sampler
        if not pretrain:
            super().__init__(
                dataset, 
                batch_size=batch_size,
                sampler=self.sampler,
                pin_memory=True,
                collate_fn=collate, 
                )
        else:
            super().__init__(
                dataset, 
                batch_size=batch_size,
                sampler=self.sampler,
                pin_memory=True,
                collate_fn=collate_pretrain, 
                )
        