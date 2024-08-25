from typing import List

def f(k: int, j: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    arr = []
    for i in range(k):
        arr.append(j)
    return arr

### Unit tests below ###
def check(candidate):
    assert candidate(7, 5) == [5, 5, 5, 5, 5, 5, 5]

def test_check():
    check(f)