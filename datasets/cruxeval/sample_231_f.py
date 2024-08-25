from typing import List

def f(years: List[int]) -> int:
    """"""
    ### Canonical solution below ###
    a10 = sum(1 for x in years if x <= 1900)
    a90 = sum(1 for x in years if x > 1910)
    if a10 > 3:
        return 3
    elif a90 > 3:
        return 1
    else:
        return 2

### Unit tests below ###
def check(candidate):
    assert candidate([1872, 1995, 1945]) == 2

def test_check():
    check(f)