import json
from untils import stop_tokens,lang_map,output_gpt_prompt
from untils import gpt_response,replace_mark,extract_python_code,eval_code
import os
from prompt import generating_python_example,generating_input_prompt,generating_output_prompt
from datasets import load_dataset
from tqdm import tqdm
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--langs", type=str, default="['cpp']")
    parser.add_argument("--tmp", type=float, default=0.2)
    parser.add_argument("--sample_num", type=int, default=5)
    parser.add_argument("--api_key", type=str, default="")
    parser.add_argument("--base_url", type=str, default="")
    parser.add_argument("--model_name", type=str, default="")
    parser.add_argument("--tests_dir", type=str, default="./datasets/cruxeval_preprocessed")
    parser.add_argument("--python_dir", type=str, default="./datasets/cruxeval")
    parser.add_argument("--example_dir", type=str, default="./MutiPL-E/evaluation/test_inputs")
    parser.add_argument("--output_dir", type=str, default="./datasets/cruxeval_generated")
        
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    langs = eval(args.langs)
    res = []
    # Iterate over each language in the list of languages
    for lang in langs:
        # Print the current language being processed
        print("current lang:",lang)
        # read the examples
        test_path = f"{args.example_dir}/{lang}-davinci-0.2-keep-HumanEval53.json"
        with open(test_path, 'r',encoding='utf-8') as f:
            sample = json.load(f)
            example_input = sample['prompt_no_intentions']
            example_output = sample['completions'][0]
            # Append stop token if not already present
            if "\n```" not in stop_tokens[lang][-1]:
                example_output += stop_tokens[lang][-1]
        
        # Number of samples to generate
        sample_num = args.sample_num
        
        # Load the dataset
        ds_tests = load_dataset("json", data_files=f"{args.tests_dir}/{lang}.jsonl")["train"]
        ds_python = args.python_dir
        
        tot_res = []
        # Iterate over the tests
        for i in tqdm(range(len(ds_tests)),total=len(ds_tests)):
            prompt = ds_tests[i]['prompt']
            file_python = f"{ds_python}/sample_{ds_tests[i]['id']}_f.py"
            with open(file_python, 'r',encoding='utf-8') as f:
                python_input = f.read()
            # Extract Python code from the file
            prompt_python = extract_python_code(python_input)
            message = [
                {"role": "system", "content": "You are a helpful programming assistant designed to translate code and complete code snippets."},
                {"role": "user", "content": generating_input_prompt(lang, generating_python_example, example_input)},
                {"role": "assistant", "content": generating_output_prompt(lang,example_input,example_output)},
                {"role": "user", "content": generating_input_prompt(lang,prompt_python,prompt)},
            ]
            # Initialize the current result dictionary
            cur_res = {"id":ds_tests[i]['id'],"error":[]}
            for j in range(sample_num):
                # Get response from GPT
                res = gpt_response(message,
                                tmp=args.tmp,
                                stop=stop_tokens[lang],
                                base_url=args.base_url,
                                api_key=args.api_key,
                                model_name=args.model_name)
                # Append stop token if needed
                if "\n```" in stop_tokens[lang][-1]:
                    res += stop_tokens[lang][-1]
                res = replace_mark(res,lang)
                res = res.rstrip() + "\n" + ds_tests[i]["tests"]
                # Evaluate the code
                exec_output = eval_code(lang_map[lang],res)
                # Update result if execution is successful
                if exec_output["status"] == "OK":
                    cur_res = {"id":ds_tests[i]['id'],"code":res}
                    break
                else:
                    # Append error details if execution fails
                    cur_res["error"].append({"id":ds_tests[i]['id'],
                                            "code": res,
                                            "error": exec_output["status"], 
                                            "error_message": exec_output["stderr"],
                                            "error_output": exec_output["stdout"]})
            # Append the current result to the total results list
            tot_res.append(cur_res)
        # Write the results to a JSON file
        with open(f"{args.output_dir}/{lang}.json", 'w',encoding='utf-8') as f:
            json.dump(tot_res, f, indent=4,ensure_ascii=False)
