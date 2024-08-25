from typing import List

def f(list: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    original = list[:]
    while len(list) > 1:
        list.pop(len(list) - 1)
        for i in range(len(list)):
            list.pop(i)
    list = original[:]
    if list:
        list.pop(0)
    return list

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)