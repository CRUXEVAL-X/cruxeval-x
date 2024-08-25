from typing import List, Tuple

def f(nums: List[int], target: int) -> Tuple[List[int], List[int]]:
    """"""
    ### Canonical solution below ###
    lows, higgs = [], []
    for i in nums:
        if i < target:
            lows.append(i)
        else:
            higgs.append(i)
    lows.clear()
    return lows, higgs

### Unit tests below ###
def check(candidate):
    assert candidate([12, 516, 5, 2, 3, 214, 51], 5) == ([], [12, 516, 5, 214, 51])

def test_check():
    check(f)