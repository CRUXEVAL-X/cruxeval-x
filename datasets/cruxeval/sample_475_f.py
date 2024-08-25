from typing import List, Any

def f(array: List[int], index: int) -> int:
    """"""
    ### Canonical solution below ###
    if index < 0:
        index = len(array) + index
    return array[index]

### Unit tests below ###
def check(candidate):
    assert candidate([1], 0) == 1

def test_check():
    check(f)