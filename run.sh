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
    echo "Training $val"
    
    # python -m IR_template.preprocess_overnight --input_dir ../sempre/lib/data/overnight/ --output_dir ./exp_files_new/TIR/overnight/$val/ --model_name_or_path ./bart-base/ --domain $val
    # srun -A priority -p Big -n 1 --gres=gpu:1 --job-name=d_$val bash -c "python -m torch.distributed.launch --nproc_per_node=1 -m train --input_dir ./exp_files_new/TIR/overnight/$val/ --output_dir ./exp_results_new/TIR/overnight/$val/ --save_dir ./exp_results_new/TIR/overnight/$val/ --model_name_or_path ./bart-base/ --batch_size 32 --port 12375 --num_train_epochs 50 --mode ir --early_stopping 15" 1> ./logging/$val.log 2>/dev/null &
    # python -m bart2query.lamb.preprocess --input_dir ./data/overnight/dataset/ --output_dir ./exp_files_new/baseline/overnight/$val/ --model_name_or_path ./bart-base/ --domain $val
    # srun -A priority -p Big -n 1 --gres=gpu:1 --job-name=d_$val bash -c "python -m torch.distributed.launch --nproc_per_node=1 -m train --input_dir ./exp_files_new/baseline/overnight/$val --output_dir ./exp_results_new/baseline/overnight/$val --save_dir ./exp_results_new/baseline/overnight/$val --model_name_or_path ./bart-base/ --batch_size 32 --num_train_epochs 50 --mode lambda --early_stopping 15" 1> ./logging/$val.log 2>/dev/null &

    # python -m IR_unified.preprocess --input_dir ./data/overnight/dataset/ --output_dir ./exp_files_new/UIR/overnight/$val/ --model_name_or_path ./bart-base/ --mode overnight --domain $val --cross_domain
    # srun -A priority -p Big -n 1 --gres=gpu:1 --job-name=d_$val bash -c "python -m torch.distributed.launch --nproc_per_node=1 -m train --input_dir ./exp_files_new/UIR/overnight/$val/ --output_dir ./exp_results_new/UIR/overnight/$val/ --save_dir ./exp_results_new/UIR/overnight/$val/ --model_name_or_path ./bart-base/ --batch_size 32 --port 12375 --num_train_epochs 50 --mode overnight --early_stopping 10" 1> ./logging/$val.log 2>/dev/null &
    

done
wait

for val in ${domains[@]}; do
#     echo "Training end2end $val"
    
    # python -m inference --input_dir ./exp_files_new/TIR/overnight/$val/ --save_dir ./exp_results_new/TIR/overnight/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/TIR/overnight/$val/checkpoint-best/ --mode ir --batch_size 256
    # python -m inference --input_dir ./exp_files_new/baseline/overnight/$val/ --save_dir ./exp_results_new/baseline/overnight/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/baseline/overnight/$val/checkpoint-best/ --mode lambda --batch_size 128 2>/dev/null 
    python -m inference --input_dir ./exp_files_new/UIR/overnight/$val/ --save_dir ./exp_results_new/UIR/overnight/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/UIR/overnight/$val/checkpoint-best/ --mode overnight --batch_size 128 2>/dev/null 
    
#     python -m IR_unified.postprocess_overnight --data_dir ./data/overnight/dataset/ --input_dir ./exp_files_new/UIR/overnight/$val/ --output_dir ./exp_files_new/UIR/overnight/end2end/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/UIR/overnight/$val/checkpoint-best/ --domain $val
#     srun -A priority -p Big -n 1 --gres=gpu:1 --job-name=d_$val bash -c "python -m torch.distributed.launch --nproc_per_node=1 -m train --input_dir ./exp_files_new/UIR/overnight/end2end/$val/ --output_dir ./exp_results_new/UIR/overnight/end2end/$val/ --save_dir ./exp_results_new/UIR/overnight/end2end/$val/ --model_name_or_path ./bart-base/ --batch_size 32 --port 12375 --num_train_epochs 50 --mode ir --early_stopping 10" 1> ./logging/$val_end2end.log 2>/dev/null &
done
wait

# for val in ${domains[@]}; do
#     echo "Inferencing $val"
#     # python -m inference --input_dir ./exp_files_new/TIR/overnight/$val/ --save_dir ./exp_results_new/TIR/overnight/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/TIR/overnight/$val/checkpoint-best/ --mode ir --batch_size 256
#     # python -m inference --input_dir ./exp_files_new/baseline/overnight/$val/ --save_dir ./exp_results_new/baseline/overnight/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/baseline/overnight/$val/checkpoint-best/ --mode lambda --batch_size 128 2>/dev/null 
    
#     python -m inference --input_dir ./exp_files_new/UIR/overnight/end2end/$val/ --save_dir ./exp_results_new/UIR/overnight/end2end/$val/ --model_name_or_path ./bart-base/ --ckpt ./exp_results_new/UIR/overnight/end2end/$val/checkpoint-best/ --mode overnight --batch_size 128 2>/dev/null
# done