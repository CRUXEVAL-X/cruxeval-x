from typing import List

def f(lst: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    lst.sort()
    return lst[0:3]

### Unit tests below ###
def check(candidate):
    assert candidate([5, 8, 1, 3, 0]) == [0, 1, 3]

def test_check():
    check(f)