import os
import json
from datasets import load_dataset
import sys
import copy
from tqdm import tqdm
from untils import gpt_response, extract_code, eval_code, extract_python_code, stop_tokens, output_gpt_prompt
from prompt import repair_generating_prompt
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--langs", type=str, default="['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']")
    parser.add_argument("--tmp", type=float, default=0)
    parser.add_argument("--api_key", type=str, default="")
    parser.add_argument("--base_url", type=str, default="")
    parser.add_argument("--model_name", type=str, default="")
    parser.add_argument("--tests_dir", type=str, default="./datasets/cruxeval_preprocessed")
    parser.add_argument("--python_dir", type=str, default="./datasets/cruxeval")
    parser.add_argument("--example_dir", type=str, default="./MutiPL-E/evaluation/test_inputs")
    parser.add_argument("--pre_dir", type=str, default="./datasets/cruxeval_generated")
    parser.add_argument("--output_dir", type=str, default="./datasets/cruxeval_generated_repaired")
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    langs = eval(args.langs)
    # Iterate over each language in the list of languages
    for lang in langs:
        print("current lang:",lang)
        # Load the correct dataset for the current language
        with open(f"{args.pre_dir}/{lang}.json", 'r', encoding="utf-8") as f:
            ds_right = json.load(f)
        # Load the test dataset for the current language
        ds_test = load_dataset("json", data_files=f"{args.tests_dir}/{lang}.jsonl")["train"]
        test_dic = {i["id"]:i for i in ds_test}
        ds_python = args.python_dir
        tot_result = []
        # Iterate over each item in the correct dataset
        for i in tqdm(range(len(ds_right)),total=len(ds_right)):
            cur_data = ds_right[i]
            data_id = cur_data["id"]
            # Skip items that do not have errors
            if "error" not in cur_data:
                tot_result.append(cur_data)
                continue
            # Read the Python file corresponding to the current data item
            file_python = f"{ds_python}/sample_{data_id}_f.py"
            with open(file_python, 'r',encoding='utf-8') as f:
                python_input = f.read()
            # Extract Python code from the input
            py_code = extract_python_code(python_input)
            # Iterate over each error in the current data item
            for error_data in cur_data["error"]:
                code = error_data["code"] 
                message = [
                    {"role": "system", "content": "You are an expert programming assistant."},
                    {"role": "user", "content": f"Please translate the language of the function from python to {lang}\n\n```python\n{py_code}\n```\n"},
                    {"role": "assistant", "content": f"```{lang}\n{code}\n```\n"},
                    {"role": "user", "content": repair_generating_prompt(error_data,lang)}
                ]
                print(output_gpt_prompt(message))
                if error_data['error'] == "SyntaxError":
                    gpt_res = gpt_response(message,
                                        tmp=args.tmp,
                                        base_url=args.base_url,
                                        api_key=args.api_key,
                                        model_name=args.model_name)
                    cur_code = extract_code(gpt_res,lang,-1)
                     # Remove stop tokens if necessary
                    if stop_tokens[lang][-1] != "\n```":
                        cur_code = cur_code.split(stop_tokens[lang][-1])[0]
                    cur_code = cur_code.rstrip() + "\n" + test_dic[data_id]["tests"]
                    exec_output = eval_code(lang,cur_code)
                    # If the execution status is OK, add the repaired code to the results
                    if exec_output["status"] == "OK":
                        tot_result.append({"id": data_id, "code": cur_code})
                        break
        # Save the final results to a JSON file
        with open(f"{args.output_dir}/{lang}.json", "w", encoding="utf-8") as f:
            json.dump(tot_result, f, indent=4,ensure_ascii=False)

