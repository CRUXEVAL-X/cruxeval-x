from typing import List

def f(array: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    result = array.copy()
    result.reverse()
    result[:] = [item * 2 for item in result]
    return result

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3, 4, 5]) == [10, 8, 6, 4, 2]

def test_check():
    check(f)