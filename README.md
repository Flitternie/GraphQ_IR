# GraphQ IR: Unified Intermediate Representation for the Semantic Parsing of Graph Query Languages

This repository contains source code for the EMNLP 2022 Long Paper "GraphQ IR: Unifying the Semantic Parsing of Graph Query Languages with One Intermediate Representation".

## Setup

**General Setup**

All required packages and versions can be found in the environment configuration file `environment.yml`, or you may simply build an identical conda environment like this:

```
conda env create -f environment.yml
conda activate graphqir
```

As for our implemented source-to-source compiler, please refer to [GraphQ Trans](https://github.com/Flitternie/GraphQ_Trans) for its setup and usage.

**Pretrained Model**

In our experiments, we used the BART-base pretrained model for implementing the neural semantic parser. To reproduce, you may download the model checkpoint [here](https://worksheets.codalab.org/rest/bundles/0x5e4369d9bf8548a78124529b02a054f6/contents/blob/).

**Dataset-Specific Setup**

For KQA Pro, you may follow their [documentation](https://github.com/shijx12/KQAPro_Baselines/tree/master/Bart_SPARQL) to set up the database backend. After starting the service, replace the url in `data/kqapro/utils/sparql_engine.py` with your own.

For GrailQA, you may follow [Freebase Setup](https://github.com/dki-lab/Freebase-Setup) to set up the database backend. After starting the service, replace the url in `data/grailqa/utils/sparql_executer.py` with your own.

## Dataset

Experiments are conducted on 4 semantic parsing benchmarks KQA Pro, Overnight, GrailQA and MetaQA-Cypher. 

**KQA Pro**

This dataset contains the parallel data of natural language questions and the corresponding logical forms in **SPARQL** and **KoPL**. It can be downloaded via the [official website](http://thukeg.gitee.io/kqa-pro/) as provided by [Cao et al. (2022)](https://aclanthology.org/2022.acl-long.422/).

**Overnight**

This dataset contains the parallel data of natural language questions and the corresponding logical forms in **Lambda-DCS** in 8 sub-domains as prepared by [Wang et al. (2015)](https://aclanthology.org/P15-1129/). The data and the evaluator can be accessed [here](https://github.com/rhythmcao/semantic-parsing-dual) as provided by [Cao et al. (2019)](https://www.aclweb.org/anthology/P19-1007.pdf).

To pull the dependencies for running the Overnight experiments, please run:

```sh
./pull_dependency_overnight.sh
```

**GrailQA**

This dataset contains the parallel data of natural language questions and the corresponding logical forms in **SPARQL**. It can be downloaded via the [offical website](https://dki-lab.github.io/GrailQA/) as provided by [Gu et al. (2020)](https://dl.acm.org/doi/abs/10.1145/3442381.3449992). To focus on the sole task of semantic parsing, we replace the entity IDs (e.g. `m.06mn7`) with their respective names (e.g. `Stanley Kubrick`) in the logical forms, thus eliminating the need for an explicit entity linking module. 

Please note that such replacement can cause inequivalent execution results.  Thus, the performance reported in our paper may not be directly comparable to the other works. 

To pull the dependencies for running the GrailQA experiments, please run:

```sh
./pull_dependency_grailqa.sh
```

**MetaQA-Cypher**

This dataset contains the parallel data of natural language questions and the corresponding logical forms in **Cypher**. The original data is available [here](https://github.com/yuyuz/MetaQA) as prepared by [Zhang et al. (2017)](https://dl.acm.org/doi/abs/10.5555/3504035.3504780). We used a rule-based method to create its Cypher annotation for low-resource evaluation.

To pull the dependencies for running the MetaQA-Cypher experiments, please run:

```sh
./pull_dependency_metaqa.sh
```



**Throughout the experiments, we suggest to structure the files as follows:**


```
GraphQ_IR/
└── data/
    ├── kqapro/
    │   ├── data/
    │   │   ├── kb.json
    │   │   ├── train.json
    │   │   ├── val.json
    │   │   └── test.json
    │   ├── utils/
    │   ├── config_kopl.py
    │   ├── config_sparql.py
    │   └── evaluate.py
    ├── overnight/
    │   ├── data/
    │   │   ├── *_train.tsv
    │   │   └── *_test.tsv
    │   ├── evaluator/
    │   └── config.py
    ├── grailqa/
    │   ├── data/
    │   │   ├── ontology/
    │   │   ├── train.json
    │   │   ├── val.json
    │   │   └── test.json
    │   ├── utils/
    │   └── config.py
    ├── metaqa/
    │   ├── data/
    │   │   └── *shot/
    │   │       ├── train.json
    │   │       ├── val.json
    │   │       └── test.json
    │   └── config.py
    ├── bart-base/
    ├── utils/
    ├── preprocess.py
    ├── train.py
    ├── inference.py
    ├── corrector.py
    ├── cfq_ir.py
    └── module-classes.txt
```

## Experiments

To simplify, here we take the NL-to-SPARQL semantic parsing task over the KQA Pro dataset as an example.

For other datasets or different target languages, you may simply modify the arguments `--input_dir`, `--output_dir` , and `--config` accordingly.

For running the BART baseline experiments, remove the argument `--ir_mode`.

For running the experiments with CFQ IR ([Herzig et al., 2021](https://arxiv.org/abs/2104.07478)), set `--ir_mode` to  `cfq`.

### Preprocessing

```bash
python -m preprocess \
--input_dir ./data/kqapro/data/ \ 			# path to raw data
--output_dir ./exp_files/kqapro/ \			# path for saving preprocessed data
--model_name_or_path ./bart-base/ \			# path to pretrained model
--config ./data/kqapro/config_sparql.py \	# path to data-specific configuration file
--ir_mode graphq # or "cfq" (only applicable to SPARQL)/ may be removed for running baseline 
```

### Training

```bash
python -m torch.distributed.launch --nproc_per_node=8 -m train \ 
--input_dir ./exp_files/kqapro/ \ 			# path to preprocessed data
--output_dir ./exp_results/kqapro/ \		# path for saving experiment logs & checkpoints
--model_name_or_path ./bart-base/ \			# path to pretrained model
--config ./data/kqapro/config_sparql.py \	# path to data-specific configuration file
--batch_size 128 \ # 128 for KQA Pro; 64 for Overnight & GrailQA & MetaQA-Cypher 
--ir_mode graphq # or "cfq" (only applicable to SPARQL)/ may be removed for running baseline 
```

### Inference

```bash
python -m inference \
--input_dir ./exp_files/kqapro/ \ 				# path to preprocessed data
--output_dir ./exp_results/kqapro/ \			# path for saving inference results
--model_name_or_path ./bart-base/ \				# path to pretrained model
--ckpt ./exp_results/kqapro/checkpoint-best/ \	# path to saved checkpoint
--config ./data/kqapro/config_sparql.py \		# path to data-specific configuration file
--ir_mode graphq # or "cfq" (only applicable to SPARQL)/ may be removed for running baseline 
```

