from typing import List

def f(x: List[int]) -> int:
    """"""
    ### Canonical solution below ###
    if x == []:
        return -1
    else:
        cache = {}
        for item in x:
            if item in cache:
                cache[item] += 1
            else:
                cache[item] = 1
        return max(cache.values())

### Unit tests below ###
def check(candidate):
    assert candidate([1, 0, 2, 2, 0, 0, 0, 1]) == 4

def test_check():
    check(f)