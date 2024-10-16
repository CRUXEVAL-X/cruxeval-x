python inference/infer_vllm.py \
    --langs "['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']" \
    --model_name your model name \
    --model_dir ./model \
    --tot_data_num 800 \
    --data_root ./datasets/cruxeval-x \
    --data_input_output ./datasets/cruxeval_preprocessed \
    --example_root ./datasets/examples \
    --example_input_output ./datasets/examples_preprocessed \
    --output_dir ./infer_results