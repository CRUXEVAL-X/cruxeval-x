from typing import List, Any

def f(array: List[int], i_num: int, elem: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    array.insert(i_num, elem)
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([ -4,   1,  0], 1, 4) == [-4, 4, 1, 0]

def test_check():
    check(f)