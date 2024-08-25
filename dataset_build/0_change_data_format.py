import os
import argparse
from datasets import load_dataset
if __name__ == '__main__':
    # read the parameter
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='./datasets/cruxeval.jsonl')
    parser.add_argument('--output_dir', type=str, default='./datasets/cruxeval_untyped')
    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    input_data = load_dataset('json', data_files=args.input_path)["train"]
    # Iterate over each sample in the input data
    for index,sample in enumerate(input_data):
        with open(os.path.join(args.output_dir, f'sample_{index}_f.py'), 'w') as f:
            code = sample['code'].split('\n')
            code_left = code[0]
            code_right = '\n'.join(code[1:])
            code = code_left + """
    \"\"\"\"\"\"
    ### Canonical solution below ###
""" + code_right 
            # Create the final code with the check and test_check functions
            cur_code = f"""{code}

def check(candidate):
    assert candidate({sample['input']}) == {sample['output']}

def test_check():
	check(f)"""
            # Write the final code to the file
            f.write(cur_code)
