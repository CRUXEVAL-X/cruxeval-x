from typing import List

def f(xs: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    for idx in reversed(range(-len(xs)-1, -1)):
        xs.insert(idx, xs.pop(0))
    return xs

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3]) == [1, 2, 3]

def test_check():
    check(f)