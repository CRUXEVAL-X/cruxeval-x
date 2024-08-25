from typing import Dict

def f(d: Dict[int, int], n: int) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    for i in range(n):
        item = d.popitem()
        d[item[1]] = item[0]
    return d

### Unit tests below ###
def check(candidate):
    assert candidate({1: 2, 3: 4, 5: 6, 7: 8, 9: 10}, 1) == {1: 2, 3: 4, 5: 6, 7: 8, 10: 9}

def test_check():
    check(f)