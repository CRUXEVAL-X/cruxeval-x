CURDIR=$(dirname "$(realpath "$0")")
source "$CURDIR/config.env"

python inference/infer_openai.bash \
    --langs "$LANGS" \
    --tmp 0 \
    --api_key "$API_KEY" \
    --base_url "$API_BASE_URL" \
    --model_name "$MODEL_NAME" \
    --tot_data_num 800 \
    --data_root ./datasets/cruxeval-x \
    --data_input_output ./datasets/cruxeval_preprocessed \
    --example_root ./datasets/examples \
    --example_input_output ./datasets/examples_preprocessed \
    --output_dir ./infer_results