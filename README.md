# Usage
## Environment

### build image
```bash
cd ./docker
docker build -t cruxeval_x .
```
### run container
```bash
cd ./docker
bash run_docker.bash
```

## Benchmark Construction
before run the benchmark construction, you need to download the deepseekcoder-33b-instruct model to ./model, and replace "your api key", "your base url" and "your model name" with your own.

if you want to run the full pipeline
```bash
cd ./cruxeval-x
bash ./script/benchmark_construction.sh
```
if you want to run only one step, find the script for the specific step in ./script and run it.

## Dataset
all the dataset is in ./data, data dir start with "example" is the examples used for few-shot inferences. The final data is in ./data/cruxeval-x.

the data is in the format of json, each line is a json object, the format is:
```json
{
    "id": "the id of the data",
    "code": "if the key exists, the code is correctly translated",
}
```
## Inference
The script for inference is in ./script

for open-source models, you can first download the model to ./model, and then run the script.
```bash
cd ./cruxeval-x
bash ./script/inference_vllm.bash
```

for close-source models, you need to provide the model name, api key and base url, and then run the script.
```bash
cd ./cruxeval-x
bash ./script/inference_openai.bash
```
## Submission

Now you have the results of your model on the dataset.

- `./cruxeval-x/infer_results/${model_name}/`: The Result of your LLM.

The next step is to submit a pull request for the project:

1. [Fork](https://help.github.com/articles/fork-a-repo/) the repository into your own GitHub account.
2. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repository to your local.
3. Checkout a new branch from main.
4. Make the results directories above (i.e. `./cruxeval-x/infer_results/${model_name}/`).
5. Submit the Pull Request.
6. The maintainers will review your Pull Request soon.

Once your pull request is accepted, we will update the [Leaderboard](https://cruxeval-x.github.io/leaderboard.html) with your results.