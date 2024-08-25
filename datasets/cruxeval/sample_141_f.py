from typing import List

def f(li: List[str]) -> List[int]:
    """"""
    ### Canonical solution below ###
    return [li.count(i) for i in li]

### Unit tests below ###
def check(candidate):
    assert candidate(['k', 'x', 'c', 'x', 'x', 'b', 'l', 'f', 'r', 'n', 'g']) == [1, 3, 1, 3, 3, 1, 1, 1, 1, 1, 1]

def test_check():
    check(f)