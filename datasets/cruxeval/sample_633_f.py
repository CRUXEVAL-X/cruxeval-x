from typing import List

def f(array: List[int], elem: int) -> int:
    """"""
    ### Canonical solution below ###
    array.reverse()
    try:
        found = array.index(elem)
    finally:
        array.reverse()
    return found

### Unit tests below ###
def check(candidate):
    assert candidate([5, -3, 3, 2], 2) == 0

def test_check():
    check(f)