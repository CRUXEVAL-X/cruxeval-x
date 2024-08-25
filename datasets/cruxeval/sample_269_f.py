from typing import List, Union

def f(array: List[int]) -> List[Union[int, str]]:
    """"""
    ### Canonical solution below ###
    zero_len = (len(array) - 1) % 3
    for i in range(zero_len):
        array[i] = '0'
    for i in range(zero_len + 1, len(array), 3):
        array[i - 1:i + 2] = ['0', '0', '0']
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([9, 2]) == ['0', 2]

def test_check():
    check(f)