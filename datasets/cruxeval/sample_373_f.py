from typing import List

def f(orig: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    copy = orig
    copy.append(100)
    orig.pop()
    return copy

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3]) == [1, 2, 3]

def test_check():
    check(f)