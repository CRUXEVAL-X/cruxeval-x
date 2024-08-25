from typing import List

def f(array: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    output = array.copy()
    output[0::2] = output[-1::-2]
    output.reverse()
    return output

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)