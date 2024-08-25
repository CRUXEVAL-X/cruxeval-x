from typing import List

def f(array: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    for i in range(len(array)):
        if array[i] < 0:
            array.pop(i)
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)