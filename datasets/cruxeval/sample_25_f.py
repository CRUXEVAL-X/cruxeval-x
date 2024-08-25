from typing import Dict

def f(d: Dict[str, int]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    d = d.copy()
    d.popitem()
    return d

### Unit tests below ###
def check(candidate):
    assert candidate({"l": 1, "t": 2, "x:": 3}) == {'l': 1, 't': 2}

def test_check():
    check(f)