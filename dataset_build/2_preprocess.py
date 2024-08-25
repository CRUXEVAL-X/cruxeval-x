import argparse
import os
from pathlib import Path
import json
import re
import sys
from untils import lang_comment
current_dir = os.path.dirname(os.path.abspath(__file__))
mutipl_dir = os.path.join(current_dir, "../MutiPL-E", "dataset_builder")
sys.path.append(mutipl_dir)

def remove_comments(code,comment):
    code = code.replace(comment,"")
    return code

def list_originals(root):
    directory = Path(Path(__file__).parent, "..").resolve()
    files_unsorted = directory.glob(f"{root}/*.py")
    def key_func(s): return int(str(s.name).split("_")[1])
    files_by_number = {key_func(file): file for file in files_unsorted}

    return files_by_number


if __name__ == "__main__":
    # read the parameter
    parser = argparse.ArgumentParser()
    parser.add_argument("--langs", type=str, default="['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']")
    parser.add_argument('--input_dir', type=str, default="./datasets/cruxeval")
    parser.add_argument("--output_dir", type=str, default="./datasets/cruxeval_preprocessed")

    args = parser.parse_args()

    langs = eval(args.langs)
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    output = []
    for cur_lang in langs:
        # Construct the language-specific translator module name
        lang = f"humaneval_to_{cur_lang}"
        translator = __import__(lang).Translator()
        from generic_translator import translate_prompt_and_tests
        # Define the output file path
        output_path = f"{args.output_dir}/{cur_lang}.jsonl"
        originals = list_originals(args.input_dir)

        cnt = 0
        with open(output_path, "w", encoding="utf-8") as f:
            for i in range(len(originals)):
                print(originals[i])
                try:
                    # Translate the prompt and test
                    result = translate_prompt_and_tests(
                                originals[i],
                                translator,
                                "transform",
                                "reworded",
                                add_canonical_to_prompt=False,
                                panic_on_test_fail=False,
                            )
                except:
                    result = None
                
                if result is None:
                    cnt += 1
                    continue
                prompt_res, tests, cruxeval_i,cruxeval_o = result

                # Remove comments from the prompt result
                prompt_res = remove_comments(prompt_res,lang_comment[cur_lang])
                if lang == "cs" and tests.find("Debug.Assert(Equals(") != -1:
                    # Add a specific method for C# if needed
                    prompt_res +="""    public static bool Equals<TKey, TValue>(Dictionary<TKey, TValue> dict1, Dictionary<TKey, TValue> dict2)
        {
            var dict3 = dict2.Where(x => !dict1.ContainsKey(x.Key) || !EqualityComparer<TValue>.Default.Equals(dict1[x.Key], x.Value))
                            .Union(dict1.Where(x => !dict2.ContainsKey(x.Key) || !EqualityComparer<TValue>.Default.Equals(dict2[x.Key], x.Value)))
                            .ToDictionary(x => x.Key, x => x.Value);
            return dict3.Count == 0;
        }
    """         
                if lang == "humaneval_to_jl" and tests.find("Dict()") != -1:
                    # Handle specific pattern for Julia language
                    pattern = r'Dict\{[^}]*\}'
                    input_part,output_part = prompt_res.split(")::")
                    input_dics = re.findall(pattern, input_part)
                    output_dics = re.findall(pattern, output_part)
                    for cur_dic in input_dics:
                        if "candidate(????)" not in tests:
                            tests = tests.replace("Dict()", f"{cur_dic}()",1)
                    for cur_dic in output_dics:
                        tests = tests.replace("Dict()", f"{cur_dic}()",1)
                # Construct the current data dictionary
                cur_data = {
                    "id": i, 
                    "prompt": prompt_res, 
                    "tests": tests,
                    "input_reasoning": cruxeval_i,
                    "output_reasoning": cruxeval_o}
                json.dump(cur_data, f,ensure_ascii=False)
                f.write("\n")
        # Append the language and count of failures to the output list
        output.append([lang.replace("humaneval_to_",""),cnt])
    print(output)