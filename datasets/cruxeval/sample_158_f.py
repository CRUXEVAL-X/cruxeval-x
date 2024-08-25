from typing import List

def f(arr: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    n = [item for item in arr if item%2 == 0]
    m = n+arr
    for i in m:
        if m.index(i) >= len(n):
            m.remove(i)
    return m

### Unit tests below ###
def check(candidate):
    assert candidate([3, 6, 4, -2, 5]) == [6, 4, -2, 6, 4, -2]

def test_check():
    check(f)