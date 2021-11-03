#!/bin/bash
python -m torch.distributed.launch --nproc_per_node=4 -m bart2sparql.train \
--input_dir ./exp_files_new/UIR/full/end2end/sparql/ --output_dir ./exp_results_new/UIR/full/end2end/sparql/ --save_dir ./exp_results_new/UIR/full/end2end/sparql/ \
--model_name_or_path ./bart-base/ --batch_size 128 --port 12335