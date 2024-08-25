from typing import Dict, List

def f(d: Dict[str, int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    size = len(d)
    v = [0] * size
    if size == 0:
        return v
    for i, e in enumerate(d.values()):
        v[i] = e
    return v

### Unit tests below ###
def check(candidate):
    assert candidate({'a': 1, 'b': 2, 'c': 3}) == [1, 2, 3]

def test_check():
    check(f)