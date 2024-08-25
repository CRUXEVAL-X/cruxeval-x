from typing import List

def f(array: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    new_array = array.copy()
    new_array = reversed(new_array)
    return [x*x for x in new_array]

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 1]) == [1, 4, 1]

def test_check():
    check(f)