from typing import List

def f(lst: List[int], mode: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    result = [el for el in lst]
    if mode:
        result.reverse()
    return result

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3, 4], 1) == [4, 3, 2, 1]

def test_check():
    check(f)