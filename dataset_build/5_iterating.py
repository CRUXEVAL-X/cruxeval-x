from vllm import LLM, SamplingParams
import json
from transformers import AutoTokenizer
from pathlib import Path
import argparse
import sys
from datasets import load_dataset
from prompt import gen_prompt_openai
from untils import extract_python_code_with_test,get_examples,output_gpt_prompt,eval_code
from untils import lang_map, iterating_stops
import json
from tqdm import tqdm

def gen_result(examples, tokenizer, llm, lang, tmp, model: str):
    stop = iterating_stops[lang]
    if "chat" in model:
        prompts = [
            tokenizer.apply_chat_template(ex["prompt"], tokenize=False, add_generation_prompt=True)
            for ex in examples
        ]

    else:
        raise NotImplementedError()

    # Create a sampling params object.
    sampling_params = SamplingParams(
        temperature=tmp,
        max_tokens=512,
        stop=stop
    )
    print(type(prompts[0]))
    print("Sample prompt: {}".format(prompts[0]))
    outputs = llm.generate(prompts, sampling_params)
    for i in range(len(examples)):
        examples[i]['generation'] = outputs[i].outputs[0].text
    return examples

def eval_iterating_code(lang, code, tests):
    code = code + tests
    exec_output = eval_code(lang_map[lang], code)
    if exec_output["status"] != "OK":
        return {"error": exec_output["status"], "error_message": exec_output["stderr"],"error_output": exec_output["stdout"]}
    return {}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--langs', type=str, default="['cpp']")
    parser.add_argument('--model_name', type=str, default='deepseek-coder-33b-instruct')
    parser.add_argument('--model_dir', type=str, default='./model')
    parser.add_argument('--tmp', type=int, default=0.8)
    parser.add_argument('--shot_num', type=int, default=3)
    parser.add_argument('--max_iter', type=int, default=50)
    parser.add_argument('--tot_data_num', type=int, default=800)
    parser.add_argument('--tests_dir', type=str, default='./datasets/cruxeval_preprocessed')
    parser.add_argument('--right_dir', type=str, default='./datasets/cruxeval_generated_repaired')
    parser.add_argument('--python_dir', type=str, default=f'./datasets/cruxeval')
    parser.add_argument('--python_new_test_dir', type=str, default=f'./datasets/cruxeval')
    parser.add_argument('--output_dir', type=str, default='./datasets/cruxeval_iterated')
    args = parser.parse_args()

    model_name_or_path = f"{args.model_dir}/{args.model_name}"

    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, trust_remote_code=True)

    # Create an LLM.
    llm = LLM(
        model=model_name_or_path,
        pipeline_parallel_size=1,
        tensor_parallel_size=1,
        max_num_seqs=10,
        max_num_batched_tokens=2048,
        max_model_len=2048,
        gpu_memory_utilization=0.85,
        trust_remote_code=True
    )

    langs = eval(args.langs)
    for lang in langs:
        num_right_id = []

        # the right data from the previous step
        ds_right = load_dataset("json", data_files=f"{args.right_dir}/{lang}.json")["train"]

        # origin data and new test data
        ds_python = []
        ds_python_new_test = []
        for i in range(args.tot_data_num):
            with open(f"{args.python_dir}/sample_{i}_f.py","r",encoding="utf-8") as f:
                ds_python.append({"code":extract_python_code_with_test(f.read())})
            with open(f"{args.python_new_test_dir}/sample_{i}_f.py","r",encoding="utf-8") as f:
                ds_python_new_test.append({"code":f.read()})

        # prompt and test case
        ds_test = load_dataset("json",data_files=f"{args.tests_dir}/{lang}.jsonl")["train"]

        # change to dict format
        test_dic = {i["id"]:i for i in ds_test}

        # right id
        right_id = list(set(ds_right['id']))

        # choose the examples
        examples,example_id = get_examples(ds_right,ds_python,args.shot_num)
        examples_python = [
            ds_python[i]["code"]
            for i in example_id
        ]
        examples_inputs = [test_dic[i]["prompt"] for i in example_id]

        max_iter = args.max_iter
        # if res is correct
        # {"id": XX, "code": XX}
        # else
        # {"id": XX, "error": [{"error": XX, "error_message": XX, "stdout": XX, "code": XX}]}
        final_res = [{"id":i,"error":[]} for i in range(len(ds_python_new_test))]
        for sample in ds_right:
            final_res[sample["id"]] = sample

        # iterate generating
        for cur_iter in range(max_iter):
            # generate prompt
            prompts = []
            print(f"* {lang} {cur_iter} : {len(right_id)}")
            num_right_id.append(len(right_id))
            if cur_iter > 10 and len(right_id) == num_right_id[-5]:
                break
        
            for index,sample in enumerate(ds_python_new_test):
                if index in right_id: continue # if already correct, skip
                if index not in test_dic: continue # if not in test_dic, skip

                python_code = ds_python_new_test[index]["code"]
                inputs_code = test_dic[index]["prompt"]
                prompt_gen = gen_prompt_openai(examples, examples_python, examples_inputs,python_code, inputs_code,lang)
                prompts.append({"prompt":prompt_gen,"task_id":index})
            # generate the code
            # {"task_id": XX, "generation": XX,"prompt": XX,"wholecode": XX}
            gen_res = gen_result(prompts,tokenizer,llm,lang,args.tmp,"chat")
            for cur_res in gen_res:
                cur_res["generation"] = cur_res["generation"].split(f"```{lang}")[-1]
            # 判断对错
            for index,cur_res in tqdm(enumerate(gen_res),total=len(gen_res)):
                code = cur_res["generation"]
                cur_id = cur_res["task_id"]
                code_status = eval_iterating_code(lang, code, test_dic[cur_id]["tests"])
                # if error
                # {"error": XX "error_message": XX "error_output": XX}
                # if correct
                # {}
                if "error" in code_status:
                    code_status["code"] = code
                    final_res[cur_id]["error"].append(code_status)
                else:
                    code_status["code"] = code + test_dic[cur_id]["tests"]
                    code_status["id"] = cur_id
                    final_res[cur_id] = code_status
                    right_id.append(cur_id)
            
            # save the result
            with open(f"{args.output_dir}/{lang}.json", "w", encoding="utf-8") as f:
                json.dump(final_res, f, ensure_ascii=False, indent=4)
        print(f"tot {lang} {cur_iter} : {len(right_id)}")
