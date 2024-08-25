from typing import Dict, Tuple

def f(d: Dict[str, int]) -> Tuple[str, Dict[str, int]]:
    """"""
    ### Canonical solution below ###
    i = len(d) - 1
    key = list(d.keys())[i]
    d.pop(key, None)
    return key, d

### Unit tests below ###
def check(candidate):
    assert candidate({'e': 1, 'd': 2, 'c': 3}) == ('c', {'e': 1, 'd': 2})

def test_check():
    check(f)