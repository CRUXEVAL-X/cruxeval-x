from typing import List, Dict

def f(keys: List[int], value: int) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    d = dict.fromkeys(keys, value)
    for i, k in enumerate(d.copy(), 1):
        if d[k] == d[i]:
            del d[i]
    return d

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 1, 1], 3) == {}

def test_check():
    check(f)