from typing import List

def f(array: List[int], n: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    return array[n:]

### Unit tests below ###
def check(candidate):
    assert candidate([0, 0, 1, 2, 2, 2, 2], 4) == [2, 2, 2]

def test_check():
    check(f)