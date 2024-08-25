from typing import List

def f(lst: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    lst[1:4] = lst[1:4][::-1]
    return lst

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3]) == [1, 3, 2]

def test_check():
    check(f)