echo change_data_format

python dataset_build/0_change_data_format.py \
    --input_path ./datasets/cruxeval.jsonl \
    --output_dir ./datasets/cruxeval_untyped \

echo change_data_format done

echo 1_type_annotate

python dataset_build/1_type_annotate.py \
    --datasets ./datasets/cruxeval_untyped \
    --output ./datasets/cruxeval_auto_typed \

echo 1_type_annotate done

echo 2_preprocess

python dataset_build/2_preprocess.py \
    --langs "['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']" \
    --input_dir ./datasets/cruxeval \
    --output_dir ./datasets/cruxeval_preprocessed \

echo 2_preprocess done

echo 3_generating

python dataset_build/3_generating.py \
    --langs "['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']" \
    --tmp 0.2 \
    --sample_num 5 \
    --api_key your api key \
    --base_url your base url \
    --model_name your model name \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --python_dir ./datasets/cruxeval \
    --example_dir ./MutiPL-E/evaluation/test_inputs \
    --output_dir ./datasets/cruxeval_generated \

echo 3_generating done

echo 4_repair_generating

python dataset_build/4_repair_generating.py \
    --langs "['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']" \
    --tmp 0 \
    --api_key your api key \
    --base_url your base url \
    --model_name your model name \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --python_dir ./datasets/cruxeval \
    --example_dir ./MutiPL-E/evaluation/test_inputs \
    --pre_dir ./datasets/cruxeval_generated \
    --output_dir ./datasets/cruxeval_generated \

echo 4_repair_generating done

echo 5_iterating

python dataset_build/5_iterating.py \
    --langs "['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']" \
    --tmp 0.8 \
    --model_name deepseek-coder-33b-instruct \
    --model_dir ./model \
    --max_iter 50 \
    --tot_data_num 800 \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --right_dir ./datasets/cruxeval_generated_repaired \
    --python_dir ./datasets/cruxeval \
    --output_dir ./datasets/cruxeval_iterated \

echo 5_iterating done

echo 6_repair_iterating

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

echo 6_repair_iterating done

echo 7_mutiturn_repair

python dataset_build/7_mutiturn_repair.py \
    --langs "['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']" \
    --tmp 0 \
    --api_key your api key \
    --base_url your base url \
    --model_name your model name \
    --tot_data_num 800 \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --right_dir ./datasets/cruxeval_iterated_repaired \
    --example_tests_dir ./datasets/examples_preprocessed \
    --example_right_dir ./datasets/examples \
    --python_dir ./datasets/cruxeval \
    --error_num 2 \
    --repair_num 3 \
    --output_dir ./datasets/cruxeval_final \

echo 7_mutiturn_repair done