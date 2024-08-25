from typing import List, Any

def f(array: List[int], L: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    if L <= 0:
        return array
    if len(array) < L:
        array.extend(f(array, L - len(array)))
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3], 4) == [1, 2, 3, 1, 2, 3]

def test_check():
    check(f)