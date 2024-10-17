root_path=your path to cruxeval-x dir
model_dir=your path to model dir

docker run --gpus all -it \
    --name cruxeval_x_env \
    -v "${root_path}/cruxeval-x:/cruxeval-x" \
    -v "${model_dir}:/cruxeval-x/model" \
    -d \
    cruxeval_x \