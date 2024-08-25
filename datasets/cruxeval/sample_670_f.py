from typing import List, Any

def f(a: List[str], b: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    d = dict(zip(a, b))
    a.sort(key=d.get, reverse=True)
    return [d.pop(x) for x in a]

### Unit tests below ###
def check(candidate):
    assert candidate(['12','ab'], [2,2]) == [2, 2]

def test_check():
    check(f)