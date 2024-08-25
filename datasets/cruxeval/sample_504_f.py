from typing import List

def f(values: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    values.sort()
    return values

### Unit tests below ###
def check(candidate):
    assert candidate([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_check():
    check(f)