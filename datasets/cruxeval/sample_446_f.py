from typing import List

def f(array: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    l = len(array)
    if l % 2 == 0:
        array.clear()
    else:
        array.reverse()
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)