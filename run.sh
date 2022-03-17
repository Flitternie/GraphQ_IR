#!/bin/bash
#
#SBATCH -A priority
#SBATCH -p Big 
#SBATCH --job-name=lambda_job
#SBATCH --output=./logging/sbatch.out
#SBATCH --error=./logging/sbatch.err
#SBATCH --nodes=1
#SBATCH --gres=gpu:8

declare -a domains=('basketball' 'blocks' 'calendar' 'housing' 'publications' 'recipes' 'restaurants' 'socialnetwork')

for val in ${domains[@]}; do
    echo "$val"
    python -m inference --input_dir ./exp_files_new/UIR/overnight/$val/ --output_dir ./exp_results_new/UIR/overnight/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/UIR/overnight/$val/checkpoint-best/ --batch_size 256 --mode overnight --ir_mode UIR
    # python -m IR_unified.preprocess --input_dir ./data/overnight/dataset/ --output_dir ./exp_files_new/UIR/overnight/$val/ --model_name_or_path ./bart-base/ --mode overnight --domain $val 
    # srun -A priority -p Big -n 1 --gres=gpu:1 --job-name=d_$val bash -c "python -m torch.distributed.launch --nproc_per_node=1 -m train --input_dir ./exp_files_new/UIR/overnight/$val/ --output_dir ./exp_results_new/UIR/overnight/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/UIR/overnight/checkpoint-tmp/ --batch_size 64 --port 12375 --num_train_epochs 50 --mode overnight --early_stopping 10 --ir_mode UIR" 1> ./logging/$val.log 2>./logging/$val.err &
done
wait

# for val in ${domains[@]}; do
#     echo "Training $val cross domain"
#     python -m IR_unified.preprocess --input_dir ./data/overnight/dataset/ --output_dir ./exp_files_new/UIR/overnight/cross_domain/$val/ --model_name_or_path ./bart-base/ --mode overnight --domain $val
#     srun -A priority -p Big -n 1 --gres=gpu:1 --job-name=d_$val bash -c "python -m torch.distributed.launch --nproc_per_node=1 -m train --input_dir ./exp_files_new/UIR/overnight/cross_domain/$val/ --output_dir ./exp_results_new/UIR/overnight/cross_domain/$val/ --model_name_or_path ./bart-base/ --batch_size 32 --num_train_epochs 50 --mode overnight --ir_mode rir --early_stopping 10" 1> ./logging/$val.UIR.log 2>./logging/$val.UIR.err &
# done
# wait
