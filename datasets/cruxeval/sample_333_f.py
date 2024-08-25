from typing import List

def f(places: List[int], lazy: List[int]) -> int:
    """"""
    ### Canonical solution below ###
    places.sort()
    for lazy in lazy:
        places.remove(lazy)
    if len(places) == 1:
        return 1
    for i, place in enumerate(places):
        if places.count(place+1) == 0:
            return i+1
    return i+1

### Unit tests below ###
def check(candidate):
    assert candidate([375, 564, 857, 90, 728, 92], [728]) == 1

def test_check():
    check(f)