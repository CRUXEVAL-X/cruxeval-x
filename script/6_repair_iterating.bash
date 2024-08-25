python dataset_build/6_repair_iterating.py \
    --langs "['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']" \
    --tmp 0 \
    --model_name deepseek-coder-33b-instruct \
    --model_dir ./model \
    --tot_data_num 800 \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --right_dir ./datasets/cruxeval_iterated \
    --python_dir ./datasets/cruxeval \
    --output_dir ./datasets/cruxeval_iterated_repaired \
