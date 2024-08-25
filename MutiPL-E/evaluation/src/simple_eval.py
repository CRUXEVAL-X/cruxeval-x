import argparse
import json
from containerized_eval import eval_string_script 

def cli():
    args = argparse.ArgumentParser()
    args.add_argument("--lang", required=True, type=str, help="The language of the file")
    return args

if __name__ == "__main__":
    args = cli().parse_args() 
    prog_str = "#include<assert.h>\n#include<bits/stdc++.h>\n\nstd::string f(std::tuple<long, long> a, std::tuple<long, long> b, std::tuple<long, long> c) {\n    std::map<long, long> result;\n    auto update_result = [&result](const std::tuple<long, long>& t) {\n        result[std::get<0>(t)] = 0;\n        result[std::get<1>(t)] = 0;\n    };\n\n    update_result(a);\n    update_result(b);\n    update_result(c);\n\n    std::string result_str = \"{\";\n    for (auto it = result.begin(); it != result.end(); ++it) {\n        if (it != result.begin()) {\n            result_str += \", \";\n        }\n        result_str += std::to_string(it->first) + \": \" + std::to_string(it->second);\n    }\n    result_str += \"}\";\n\n    return result_str;}\nint main() {\n    auto candidate = f;\n    assert(candidate((std::make_tuple(1, 3)), (std::make_tuple(1, 4)), (std::make_tuple(1, 2))) == (\"{1: None, 2: None, 3: None, 4: None}\"));\n}\n"
    # while True:
    #     try:
    #         line = input()
    #         prog_str += line + "\n"
    #     except EOFError:
    #         break
    print(json.dumps(eval_string_script(args.lang, prog_str)), end="")
