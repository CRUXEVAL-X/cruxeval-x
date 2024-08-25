from typing import Dict

def f(d: Dict[int, int], k: int) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    new_d = {}
    for key, val in d.items():
        if key < k:
            new_d[key] = val
    return new_d

### Unit tests below ###
def check(candidate):
    assert candidate({1: 2, 2: 4, 3: 3}, 3) == {1: 2, 2: 4}

def test_check():
    check(f)