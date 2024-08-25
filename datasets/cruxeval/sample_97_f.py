from typing import List

def f(lst: List[int]) -> bool:
    """"""
    ### Canonical solution below ###
    lst.clear()
    for i in lst:
        if i == 3:
            return False
    else:
        return True

### Unit tests below ###
def check(candidate):
    assert candidate([2, 0]) == True

def test_check():
    check(f)