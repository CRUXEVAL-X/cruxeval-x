import json
from transformers import AutoTokenizer
import argparse
from datasets import load_dataset
from prompt import crux_input_prompt_chat,crux_output_prompt_chat
from untils import eval_code,lang_map,input_map,iterating_stops,gpt_response
import json
from tqdm import tqdm
import os


def read_data(file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data

def gen_result(examples, model: str):
    stop = ["[/ANSWER]"]
    prompts = [ex["prompt"] for ex in examples]
    for i in tqdm(range(len(examples)),total= len(examples)):
        examples[i]['generation'] = gpt_response(prompts[i], tmp = 0, stop=stop,model_name=args.model_name,base_url=args.base_url,api_key=args.api_key)
    return examples

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--langs', type=str, default="['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']")
    parser.add_argument('--model_name', type=str, default='')
    parser.add_argument("--api_key", type=str, default="")
    parser.add_argument("--base_url", type=str, default="")
    parser.add_argument('--tmp', type=int, default=0)
    parser.add_argument('--tot_data_num', type=int, default=800)

    parser.add_argument('--data_root', type=str, default=f'./datasets/cruxeval-x')
    parser.add_argument('--data_input_output', type=str, default=f'./datasets/cruxeval_preprocessed')
    parser.add_argument('--example_root', type=str, default=f'./datasets/examples')
    parser.add_argument('--example_input_output', type=str, default=f'./datasets/examples_preprocessed')
    parser.add_argument('--output_dir', type=str, default=f'./infer_results')



    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    output_dir = f"{args.output_dir}/{args.model_name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    langs = eval(args.langs)
    for lang in langs:
        ds_data = read_data(f"{args.data_root}/{lang}.json")
        ds_data_input_output = load_dataset("json",data_files=f"{args.data_input_output}/{lang}.jsonl")["train"]
        example_data = read_data(f"{args.example_root}/{lang}.json")
        example_data_input_output = load_dataset("json",data_files=f"{args.example_input_output}/{lang}.jsonl")["train"]
        ds_data_input_output = {"input":{i["id"]:i["input_reasoning"] for i in ds_data_input_output},
                                "output":{i["id"]:i["output_reasoning"] for i in ds_data_input_output}}
        example_data_input_output = {"input":{i["id"]:i["input_reasoning"] for i in example_data_input_output},
                                    "output":{i["id"]:i["output_reasoning"] for i in example_data_input_output}}
        prompt_func = {
            "input":crux_input_prompt_chat,
            "output":crux_output_prompt_chat
        }
        prompts = {}
        # construct prompt
        for task_type in ["input","output"]:
            examples = []
            for example in example_data:
                code = example["code"]
                flag = False
                for stop in iterating_stops[lang]:
                    if stop in code:
                        code = code.split(stop)[0]
                        flag = True
                        break
                if not flag: assert Exception
                code_right_part = example_data_input_output[task_type][example["id"]]
                examples.append({"code":code+code_right_part,"answer":example[f"{task_type}s"]})

            cur_prompt = [] # {"prompt":prompt,"task_id":task_id}
            for sample in ds_data:
                if "code" not in sample: continue
                code = sample["code"]
                flag = False
                for stop in iterating_stops[lang]:
                    if stop in code:
                        code = code.split(stop)[0]
                        flag = True
                        break
                if not flag: assert Exception
                code_right_part = ds_data_input_output[task_type][sample["id"]]
                code += code_right_part
                cur_prompt.append({"prompt":prompt_func[task_type](lang,examples,code,args.model_name),
                                   "task_id":sample["id"]})
            prompts[task_type] = cur_prompt
        # generate answer
        for task_type in ["input","output"]:
            print(task_type)
            cur_prompt = prompts[task_type]
            gen_res = gen_result(cur_prompt,args.model_name)
            for cur_res in gen_res:
                cur_res["generation"] = cur_res["generation"].split("[ANSWER]")[-1]
                cur_res["generation"] = cur_res["generation"].replace("[/ANSWER","")
            # judege whether the answer is right
            outputs = [{"id":i,"res":0} for i in range(800)]
            for index,cur_res in tqdm(enumerate(gen_res),total=len(gen_res)):
                answer = cur_res["generation"].strip()
                cur_id = cur_res["task_id"]
                code = cur_prompt[index]["prompt"][-1]["content"].split(f"```{lang}")[-1]
                code = code.replace(f"```","")
                if task_type == "output":
                    code = code.replace("????",answer)
                else:
                    code = code.replace(input_map[lang], answer)
                exec_output = eval_code(lang_map[lang], code)
                if exec_output["status"] != "OK":
                    outputs[cur_id]["res"] = False
                    outputs[cur_id]["error"] = exec_output["status"]
                    outputs[cur_id]["error_message"] = exec_output["stderr"]
                    outputs[cur_id]["code"] = code
                    outputs[cur_id]["answer"] = answer
                else:
                    outputs[cur_id]["res"] = True
                    outputs[cur_id]["code"] = code
                    outputs[cur_id]["answer"] = answer
                    
            with open(f"{output_dir}/{lang}_{task_type}.json","w",encoding="utf-8") as f:
                json.dump(outputs,f,indent=4,ensure_ascii=False)