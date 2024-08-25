from typing import Dict

def f(dic: Dict[int,int]) -> Dict[int,int]:
    """"""
    ### Canonical solution below ###
    d = {}
    for key in dic:
        d[key] = dic.popitem(last = False)[1]
    return d

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)