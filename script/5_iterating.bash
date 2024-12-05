CURDIR=$(dirname "$(realpath "$0")")
source "$CURDIR/config.env"

python dataset_build/5_iterating.py \
    --langs "$LANGS" \
    --tmp 0.8 \
    --model_name "$MODEL_NAME" \
    --model_dir ./model \
    --max_iter 50 \
    --tot_data_num 800 \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --right_dir ./datasets/cruxeval_generated_repaired \
    --python_dir ./datasets/cruxeval \
    --output_dir ./datasets/cruxeval_iterated
