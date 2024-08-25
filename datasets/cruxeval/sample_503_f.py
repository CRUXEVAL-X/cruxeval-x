from typing import Dict, List, Tuple

def f(d: Dict[int, int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    result = [None] * len(d)
    a = b = 0
    while d:
        result[a] = d.popitem(a == b)
        a, b = b, (b+1) % len(result)
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({}) == []

def test_check():
    check(f)