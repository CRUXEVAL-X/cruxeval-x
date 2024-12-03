CURDIR=$(dirname "$(realpath "$0")")
source "$CURDIR/config.env"

python dataset_build/2_preprocess.py \
    --langs "$LANGS" \
    --input_dir ./datasets/cruxeval \
    --output_dir ./datasets/cruxeval_preprocessed