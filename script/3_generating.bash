CURDIR=$(dirname "$(realpath "$0")")
source "$CURDIR/config.env"

python dataset_build/3_generating.py \
    --langs "$LANGS" \
    --tmp 0.2 \
    --sample_num 5 \
    --api_key "$API_KEY" \
    --base_url "$API_BASE_URL" \
    --model_name "$MODEL_NAME" \
    --tests_dir ./datasets/cruxeval_preprocessed \
    --python_dir ./datasets/cruxeval \
    --example_dir ./MutiPL-E/evaluation/test_inputs \
    --output_dir ./datasets/cruxeval_generated