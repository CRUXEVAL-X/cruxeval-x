from typing import Dict

def f(bag: Dict[int, int]) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    values = list(bag.values())
    tbl = {}
    for v in range(100):
        if v in values:
            tbl[v] = values.count(v)
    return tbl

### Unit tests below ###
def check(candidate):
    assert candidate({0: 0, 1: 0, 2: 0, 3: 0, 4: 0}) == {0: 5}

def test_check():
    check(f)