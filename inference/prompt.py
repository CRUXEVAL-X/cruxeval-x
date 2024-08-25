def crux_input_prompt(lang,examples,input_text):
    example_str = ""
    for example in examples:
        example_str += f"""```{lang}
{example["code"].strip()}
```
[ANSWER]
{example["answer"]}
[/ANSWER]
"""

    return f"""You will be given a {lang} function f and a check function, where you only know the output of the test case. Find any input such that executing f on the input leads to the given output. There may be multiple answers, but you should only output one. Think step by step before arriving at an answer. Finally, surround the answer, with no additional words, with [ANSWER] and [/ANSWER] tags. Express your answer as a function call that when executed will give the output.

{example_str.rstrip()}
```{lang}
{input_text}
```
"""

def crux_output_prompt(lang,examples,input_text):
    example_str = ""
    for example in examples:
        example_str += f"""```{lang}
{example["code"].strip()}
```
[ANSWER]
{example["answer"]}
[/ANSWER]
"""

    return f"""Based on the given code, which may contain errors, complete the "????" in assert statement with the output when executing the {lang} code on the given test case. Do NOT output any extra information, even if the function is incorrect or incomplete. Do NOT output a description for the assert.

{example_str.rstrip()}
```{lang}
{input_text}
```
"""

def crux_input_prompt_chat(lang,examples,input_text,model:str):
    message = [{"role": "system", "content": "You are a helpful programming assistant designed to execute code."},]

    problem_str = f"You will be given a {lang} function f and a check function, where you only know the output of the test case. Find any input such that executing f on the input leads to the given output. There may be multiple answers, but you should only output one. Think step by step before arriving at an answer. Finally, surround the answer, with no additional words, with [ANSWER] and [/ANSWER] tags. Express your answer as a function call that when executed will give the output."
    
    if "gpt" in model:
        problem_str = f"""You will be given a {lang} function f and a check function, where you only know the output of the test case. Output the completion of the 
check function so that the code will run without errors by finding any input such that executing f 
on the input leads to the given output. There may be multiple answers, and you can output any one.
Do NOT output any additional information."""

    for example in examples:
        message.append({"role": "user", "content":f"""{problem_str}

```{lang}
{example["code"].strip()}
```""" })
        message.append({"role": "assistant", "content":f"""[ANSWER]
{example["answer"]}
[/ANSWER]"""})

    message.append({"role": "user", "content":f"""{problem_str}

```{lang}
{input_text}
```"""})

    return message

def crux_output_prompt_chat(lang,examples,input_text,model:str):
    message = [{"role": "system", "content": "You are a helpful programming assistant designed to execute code."},]

    problem_str = f"Based on the given code, which may contain errors, complete the \"????\" in assert statement with the output when executing the {lang} code on the given test case. Do NOT output any extra information, even if the function is incorrect or incomplete. Do NOT output a description for the assert."
    
    if "gpt" in model:
        problem_str = f"""Based on the given code, which may contain errors, complete the \"????\" in assert statement with the 
output when executing the {lang} code on the given test case. Do not output any extra information,
even if the function is incorrect or incomplete."""

    for example in examples:
        message.append({"role": "user", "content":f"""{problem_str}

```{lang}
{example["code"].strip()}
```""" })
        message.append({"role": "assistant", "content":f"""[ANSWER]
{example["answer"]}
[/ANSWER]"""})

    message.append({"role": "user", "content":f"""{problem_str}

```{lang}
{input_text}
```"""})
    return message