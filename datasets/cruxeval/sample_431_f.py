from typing import List

def f(n: int, m: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    arr = list(range(1, n+1))
    for i in range(m):
        arr.clear()
    return arr

### Unit tests below ###
def check(candidate):
    assert candidate(1, 3) == []

def test_check():
    check(f)