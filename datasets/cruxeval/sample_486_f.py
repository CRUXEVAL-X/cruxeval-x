from typing import Dict

def f(dic: Dict[int, int]) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    dic_op = dic.copy()
    for key, val in dic.items():
        dic_op[key] = val * val
    return dic_op

### Unit tests below ###
def check(candidate):
    assert candidate({1:1, 2:2, 3:3}) == {1: 1, 2: 4, 3: 9}

def test_check():
    check(f)