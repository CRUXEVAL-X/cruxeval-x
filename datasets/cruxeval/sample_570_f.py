from typing import List

def f(array: List[int], index: int, value: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    array.insert(0, index + 1)
    if value >= 1:
        array.insert(index, value)
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([2], 0, 2) == [2, 1, 2]

def test_check():
    check(f)