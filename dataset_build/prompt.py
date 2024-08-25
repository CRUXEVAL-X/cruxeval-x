def generating_input_prompt(lang,inputs_python,inputs):
    prompt = f"""Please translate the python function to {lang} function:

```python
{inputs_python.rstrip()}
```"""
    if lang not in ["lua","rb","rkt"]:
        prompt += f"""

The function starts as follows, and your task is to complete it so that its semantics are the same as the python code above.
Note that the number of packages called at the beginning of the given function cannot be reduced, but can only be increased.

```{lang}
{inputs.rstrip()}
```"""
    return prompt

def generating_output_prompt(lang,inputs,outputs):
    return f"""```{lang}
{inputs.rstrip()}
{outputs.rstrip()}
```"""

def repair_generating_prompt(res,lang):
    return f"""The code you translated has the following {res['error']} error:

{res["error_message"]}

Please analyze the cause of the error and then return the repaired code in {lang}.
"""

generating_python_example = """def add(a, b):
    return a + b"""

def input_prompt(lang,inputs_python,inputs):
    return f"""Please translate the python function to {lang} function and translate the test case for check:

```python
{inputs_python.rstrip()}
```

Here is the start of the translated function, you can add more packages if needed:

```{lang}
{inputs.rstrip()}
```
"""

def input_prompt_with_check(lang,inputs_python,inputs,check_func):
    return f"""Please translate the python function to {lang} function and translate the test case for check:

```python
{inputs_python.rstrip()}
```

Here is the start of the translated function, and the translated check function, you can add more packages if needed:

```{lang}
{inputs.rstrip()}
```

```{lang}
{check_func.rstrip()}
```
"""

def output_prompt(lang,outputs):
    return f"""```{lang}
{outputs.rstrip()}
```"""

def gen_prompt_openai(examples,examples_python,examples_input,python_code,inputs_code,lang):
    message = [
        {"role": "system", "content": "You are a helpful programming assistant designed to translate code."},
    ]
    for index, example in enumerate(examples):
        message.append(
            {"role": "user", "content": input_prompt(lang, examples_python[index], examples_input[index])}
        )
        message.append(
            {"role": "assistant", "content": output_prompt(lang, examples[index])}
        )
    message.append(
        {"role": "user", "content": input_prompt(lang, python_code, inputs_code)}
    )
    return message

def err_prompt(lang,errors):
    if errors["error_message"] != "":
        errors["error_message"] = f":\n\n{errors['error_message']}\n"
    else:
        errors["error_message"] = "\n"
    return f"""The code you generated has the following errors:

{errors["error"]}{errors["error_message"]}
Please first analyse why the original code led to the error and how your modifications address it
Then, please modify the code to fix the error and make sure the code is accurately translated from the python code and can pass the test case
The modified code should be in code block ```{lang} ```"""


def new_err_prompt(lang,errors,check_func):
    return f"""The code you generated has the following errors:

{errors["stderr"]}
{errors["stdout"]}

Please first analyse why the original code led to the error and how your modifications address it
Then, please modify the code to fix the error and make sure the code is accurately translated from the python code and can pass the test case
The modified code should be in code block ```{lang} ```

The check function is as follows:
```{lang}
{check_func.rstrip()}
```
"""

def gen_repair_prompt_openai(python_code,cur_test,errors,lang):
    message = [
        {"role": "system", "content": "You are a helpful programming assistant designed to translate code."},
        {"role": "user", "content": input_prompt(lang, python_code, cur_test["prompt"])},
        {"role": "assistant", "content": output_prompt(lang, errors["code"]+cur_test["tests"])},
        {"role": "user", "content": err_prompt(lang, errors)}
    ]
    return message

d_19 = """import std.math;
import std.typecons;
import std.conv;
import std.algorithm;
import std.array;
import std.string;

string f(string x, string y) {
    char[] yMutable = y.dup;
    yMutable.reverse();
    string tmp = yMutable.map!(c => c == '9' ? '0' : '9').array.map!(c => c.to!string).array.join("");
    if (x.isNumeric && tmp.isNumeric) {
        return x ~ tmp;
    } else {
        return x;
    }
}
"""

swift_331 = """import Foundation

func f(strand: String, zmnc: String) -> Int {    
    var strand = strand
    var poz = strand.range(of: zmnc)
    while poz != nil {
        strand.removeSubrange(poz!)
        poz = strand.range(of: zmnc)
    }
    let lastIndex = strand.range(of: zmnc, options: [], range: nil, locale: nil)?.lowerBound.utf16Offset(in: strand)
    return lastIndex ?? -1
"""

python_2 = """from typing import Dict,Tuple

def f(d: Dict[str, int]) -> Tuple[int,int]:
    """"""
    ### Canonical solution below ###
    if 'x' in d:
        x = d['x']
    if 'y' in d:
        y = d['y']
    return x,y

### Unit tests below ###
def check(candidate):
    assert candidate({'x': 5, 'y': 12}) == (5, 12)
    
def test_check():
    check(f)
"""