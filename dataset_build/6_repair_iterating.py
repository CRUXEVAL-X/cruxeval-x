from vllm import LLM, SamplingParams
import json
from transformers import AutoTokenizer
from pathlib import Path
import argparse
import sys
from datasets import load_dataset
from prompt import gen_prompt_openai, gen_repair_prompt_openai
from untils import lang_map,iterating_stops
from untils import eval_code, is_similar
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
    parser.add_argument('--model_dir', type=str, default='./models')
    parser.add_argument('--tmp', type=int, default=0)
    parser.add_argument('--tot_data_num', type=int, default=800)
    parser.add_argument('--tests_dir', type=str, default='./datasets/cruxeval_preprocessed')
    parser.add_argument('--right_dir', type=str, default='./datasets/cruxeval_iterated')
    parser.add_argument('--python_dir', type=str, default=f'./datasets/cruxeval')
    parser.add_argument('--python_new_test_dir', type=str, default=f'./datasets/cruxeval')
    parser.add_argument('--output_dir', type=str, default='./datasets/cruxeval_iterated_repaired')
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
        # read python data
        ds_python = []
        for i in range(800):
            with open(f"{args.python_dir}/sample_{i}_f.py","r",encoding="utf-8") as f:
                ds_python.append({"code":f.read()})
        # read test case
        ds_test = load_dataset("json",data_files=f"{args.tests_dir}/{lang}.jsonl")["train"]
        test_dic = {i["id"]:i for i in ds_test}
        # read data from last iteration
        with open(f"{args.right_dir}/{lang}.json","r",encoding="utf-8") as f:
            ds_right = json.load(f)
        # deduplicate
        prompts_iter = []
        right_id = []
        for index,data in enumerate(ds_right):
            if "error" in data:
                errors = data["error"]
                errors_dedup = []
                for i in range(len(errors)):
                    for j in range(i+1,len(errors)):
                        if is_similar(errors[i],errors[j],lambda x:x["error_message"]+x["code"],5):
                            break
                    else:
                        errors_dedup.append(errors[i])
                data["error"] = []
                for index_error,error in enumerate(errors_dedup):
                    if len(prompts_iter) <= index_error:
                        prompts_iter.append([{"task_id":data["id"],"error":error}])
                    else:
                        prompts_iter[index_error].append({"task_id":data["id"],"error":error})
            else:
                right_id.append(data["id"])
        # iterate
        for cur_iter,prompts in enumerate(prompts_iter):
            print(f"* {lang} {cur_iter} : {len(right_id)}")
            # gen prompt
            gen_prompts = []
            for prompt in prompts:
                cur_id = prompt["task_id"]
                if cur_id in right_id:
                    continue
                python_code = ds_python[cur_id]["code"]
                cur_test = test_dic[cur_id]
                errors = prompt["error"]
                prompt["prompt"] = gen_repair_prompt_openai(python_code,cur_test,errors,lang)
                gen_prompts.append(prompt)
            if len(gen_prompts) == 0:
                continue
            # gen result
            gen_res = gen_result(gen_prompts,tokenizer,llm,lang,args.tmp,"chat")
            for cur_res in gen_res:
                cur_res["generation"] = cur_res["generation"].split(f"```{lang}")[-1]
            # judge
            for index,cur_res in tqdm(enumerate(gen_res),total=len(gen_res)):
                code = cur_res["generation"]
                cur_id = cur_res["task_id"]
                code_status = eval_iterating_code(lang, code, test_dic[cur_id]["tests"])
                # if error
                # {"error": XX "error_message": XX}
                # if correct
                # {"inputs": XX "outputs": XX}
                if "error" in code_status:
                    code_status["code"] = code
                    ds_right[cur_id]["error"].append(code_status)
                else:
                    code_status["code"] = code + test_dic[cur_id]["tests"]
                    code_status["id"] = cur_id
                    ds_right[cur_id] = code_status
                    right_id.append(cur_id)
            # save the result
            with open(f"{args.output_dir}/{lang}.json", "w", encoding="utf-8") as f:
                json.dump(ds_right, f, ensure_ascii=False, indent=4)
        print(f"tot {lang} {cur_iter} : {len(right_id)}")