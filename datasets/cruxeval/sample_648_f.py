from typing import List, Union

def f(list1: List[int], list2: List[int]) -> Union[int, str]:
    """"""
    ### Canonical solution below ###
    l = list1[:]
    while len(l) > 0:
        if l[-1] in list2:
            l.pop()
        else:
            return l[-1]
    return 'missing'

### Unit tests below ###
def check(candidate):
    assert candidate([0, 4, 5, 6], [13, 23, -5, 0]) == 6

def test_check():
    check(f)