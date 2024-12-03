CURDIR=$(dirname "$(realpath "$0")")
source "$CURDIR/config.env"

python dataset_build/7_mutiturn_repair.py \
    --langs "$LANGS" \
    --tmp 0 \
    --api_key "$API_KEY" \
    --base_url "$API_BASE_URL" \
    --model_name "$MODEL_NAME" \
    --tot_data_num 800 \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --right_dir ./datasets/cruxeval_iterated_repaired \
    --example_tests_dir ./datasets/examples_preprocessed \
    --example_right_dir ./datasets/examples \
    --python_dir ./datasets/cruxeval \
    --error_num 2 \
    --repair_num 3 \
    --output_dir ./datasets/cruxeval_final \