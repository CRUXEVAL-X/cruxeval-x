from typing import Dict

def f(dic: Dict[int, str]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    dic2 = dict(zip(dic.values(), dic.keys()))
    return dic2

### Unit tests below ###
def check(candidate):
    assert candidate({-1: "a", 0: "b", 1: "c"}) == {'a': -1, 'b': 0, 'c': 1}

def test_check():
    check(f)