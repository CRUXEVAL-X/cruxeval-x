from typing import List

def f(lst: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    lst.reverse()
    lst.pop()
    lst.reverse()
    return lst

### Unit tests below ###
def check(candidate):
    assert candidate([7, 8, 2, 8]) == [8, 2, 8]

def test_check():
    check(f)