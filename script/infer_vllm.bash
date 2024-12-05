CURDIR=$(dirname "$(realpath "$0")")
source "$CURDIR/config.env"

python inference/infer_vllm.py \
    --langs "$LANGS" \
    --model_name "$MODEL_NAME" \
    --model_dir ./model \
    --tot_data_num 800 \
    --data_root ./datasets/cruxeval-x \
    --data_input_output ./datasets/cruxeval_preprocessed \
    --example_root ./datasets/examples \
    --example_input_output ./datasets/examples_preprocessed \
    --output_dir ./infer_results