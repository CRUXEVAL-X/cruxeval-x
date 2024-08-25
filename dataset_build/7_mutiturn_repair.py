import json
from transformers import AutoTokenizer
from pathlib import Path
import argparse
import sys
from datasets import load_dataset
from prompt import output_prompt,input_prompt_with_check,new_err_prompt
from prompt import d_19,swift_331,python_2
from untils import output_gpt_prompt, extract_python_code_with_test,extract_code,gpt_response,lang_map,eval_code,iterating_stops
import json
from tqdm import tqdm
import os
import numpy as np
import copy

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--langs', type=str, default="['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']")
    parser.add_argument('--model_name', type=str, default='')
    parser.add_argument("--api_key", type=str, default="")
    parser.add_argument("--base_url", type=str, default="")
    parser.add_argument('--tmp', type=int, default=0)
    parser.add_argument('--tot_data_num', type=int, default=800)

    parser.add_argument('--tests_dir', type=str, default='./datasets/cruxeval_preprocessed')
    parser.add_argument('--right_dir', type=str, default='./datasets/cruxeval_iterated_repaired') # pre generate right code
    parser.add_argument('--example_tests_dir', type=str, default='./datasets/examples_preprocessed')
    parser.add_argument('--example_right_dir', type=str, default='./datasets/examples') # pre generate right code
    parser.add_argument('--python_dir', type=str, default=f'./datasets/cruxeval')
    parser.add_argument('--python_new_test_dir', type=str, default=f'./datasets/cruxeval')

    parser.add_argument('--error_num', type=int, default=2)
    parser.add_argument('--repair_num', type=int, default=3)
    parser.add_argument('--output_dir', type=str, default='./datasets/cruxeval_final')

    args = parser.parse_args()
    langs = eval(args.langs)
    os.makedirs(args.output_dir,exist_ok=True)

    print("error num : ",args.error_num)
    # read data
    ds_python = []
    ds_test_all = {}
    ds_right_all = {}
    example_test_all = {}
    example_right_all = {}
    for i in range(800):
        with open(f"{args.python_dir}/sample_{i}_f.py","r",encoding="utf-8") as f:
            ds_python.append({"code":extract_python_code_with_test(f.read())})
    for lang in langs:
        ds_test = load_dataset("json",data_files=f"{args.tests_dir}/{lang}.jsonl")["train"]
        test_dic = {i["id"]:i for i in ds_test}
        ds_test_all[lang] = test_dic
        with open(f"{args.right_dir}/{lang}.json","r",encoding="utf-8") as f:
            ds_right = json.load(f)
        ds_right_all[lang] = ds_right
        example_test = load_dataset("json",data_files=f"{args.example_tests_dir}/{lang}.jsonl")["train"]
        example_test_dic = {i["id"]:i for i in example_test}
        example_test_all[lang] = example_test_dic
        with open(f"{args.example_right_dir}/{lang}.json","r",encoding="utf-8") as f:
            example_right = json.load(f)
        example_right_all[lang] = example_right
    
    # generate prompt
    prompts_head = {}
    for lang in langs:
        messages = []
        messages.append({"role": "system", "content": "You are a helpful programming assistant designed to translate code."})
        messages.append({"role": "user", "content": input_prompt_with_check(lang, ds_python[19]["code"],ds_test_all[lang][19]["prompt"],ds_test_all[lang][19]["tests"])})
        if "code" in ds_right_all[lang][19]:
            output_code = ds_right_all[lang][19]["code"]
        else:
            output_code = d_19+ds_test_all[lang][19]["tests"]
        messages.append({"role": "assistant", "content": output_prompt(lang,output_code)})
        messages.append({"role": "user", "content": input_prompt_with_check(lang, ds_python[331]["code"],ds_test_all[lang][331]["prompt"],ds_test_all[lang][331]["tests"])})
        if "code" in ds_right_all[lang][331]:
            output_code = ds_right_all[lang][331]["code"]
        else:
            output_code = swift_331+ds_test_all[lang][331]["tests"]
        messages.append({"role": "assistant", "content": output_prompt(lang,output_code)})
        messages.append({"role": "user", "content": input_prompt_with_check(lang, extract_python_code_with_test(python_2), example_test_all[lang][2]["prompt"], example_test_all[lang][2]["tests"])})
        messages.append({"role": "assistant", "content": output_prompt(lang,example_right_all[lang][2]["code"])})
        prompts_head[lang] = messages
    # generate
    error_lang = {i:[] for i in range(args.tot_data_num)}
    for lang in ds_right_all:
        for sample in ds_right_all[lang]:
            if "error" in sample:
                error_lang[sample["id"]].append(lang)
    error_num = args.error_num # the intersection number of error
    repair_num = args.repair_num # the repair number of each error
    with open(f"{args.output_dir}/error_{error_num}.jsonl", "w", encoding="utf-8") as f_error:
        with open(f"{args.output_dir}/repair_{error_num}.jsonl", "w", encoding="utf-8") as f:
            for i in tqdm(range(args.tot_data_num)):
                cur_lang = error_lang[i]
                if len(cur_lang) > error_num: continue
                if cur_lang == []: continue
                if i in [19,331]: continue
                flag = True
                output_res = {}
                for lang in cur_lang:
                    if flag == False: break
                    cur_messages = copy.deepcopy(prompts_head[lang])
                    if i not in ds_test_all[lang]:
                        flag = False
                        continue
                    cur_messages.append({"role": "user", "content": input_prompt_with_check(lang, ds_python[i]["code"], ds_test_all[lang][i]["prompt"], ds_test_all[lang][i]["tests"])})
                    res = gpt_response(cur_messages,api_key=args.api_key,base_url = args.base_url, model_name=args.model_name,tmp=args.tmp)
                    res_code = extract_code(res,lang,-1)
                    cur_messages.append({"role": "assistant", "content": res})
                    # iterative repair the result until the max iter or correct
                    for j in range(repair_num):
                        exec_output = eval_code(lang_map[lang], res_code)
                        if exec_output["status"] == "OK": break
                        cur_messages.append({"role": "user", "content": new_err_prompt(lang, exec_output, ds_test_all[lang][i]["tests"])})
                        res = gpt_response(cur_messages,api_key=args.api_key,base_url = args.base_url, model_name=args.model_name,tmp=args.tmp)
                        res_code = extract_code(res,lang,-1)
                        cur_messages.append({"role": "assistant", "content": res})
                    # depart the check function and replace it to the right one
                    for cur_stop in iterating_stops[lang]:
                        if cur_stop in res_code:
                            res_code = res_code.split(cur_stop)[0] + ds_test_all[lang][i]["tests"]
                    exec_output = eval_code(lang_map[lang], res_code)
                    if exec_output["status"] != "OK": flag = False

                    output_res[lang] = {"code":res_code,"prompt":cur_messages}
                    ds_right_all[lang][i] = {"code":res_code,"id":i}
                if flag:
                    final_data = {"id":i,"data":output_res}
                    json.dump(final_data,f)
                    f.write("\n")
                else:
                    json.dump({"id":i,"data":output_res},f_error)
                    f_error.write("\n")
    for lang in ds_right_all:
        with open(f"{args.output_dir}/{lang}.json", "w", encoding="utf-8") as f:
            json.dump(ds_right_all[lang],f)