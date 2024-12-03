CURDIR=$(dirname "$(realpath "$0")")
source "$CURDIR/config.env"

python dataset_build/6_repair_iterating.py \
    --langs "$LANGS" \
    --tmp 0 \
    --model_name deepseek-coder-33b-instruct \
    --model_dir ./model \
    --tot_data_num 800 \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --right_dir ./datasets/cruxeval_iterated \
    --python_dir ./datasets/cruxeval \
    --output_dir ./datasets/cruxeval_iterated_repaired \
