from typing import List

def f(array: List[int], elem: int) -> int:
    """"""
    ### Canonical solution below ###
    return array.count(elem) + elem

### Unit tests below ###
def check(candidate):
    assert candidate([1, 1, 1], -2) == -2

def test_check():
    check(f)