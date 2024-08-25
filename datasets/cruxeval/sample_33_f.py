from typing import List, Dict

def f(lists: List[int]) -> str:
    """"""
    ### Canonical solution below ###
    dic = {}
    for n in lists:
        if n in dic:
            dic[n].append(lists.pop(lists.index(n)))
        else:
            dic[n] = lists[:lists.index(n) + 1]
    return str(dic).replace(' ', '')

### Unit tests below ###
def check(candidate):
    assert candidate([5, 2, 7, 2, 3, 5]) == '{5:[5,5],2:[5,2,2],7:[5,2,7]}'

def test_check():
    check(f)