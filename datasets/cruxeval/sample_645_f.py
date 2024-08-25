from typing import List

def f(nums: List[int], target: int) -> int:
    """"""
    ### Canonical solution below ###
    if nums.count(0):
        return 0
    elif nums.count(target) < 3:
        return 1
    else:
        return nums.index(target)

### Unit tests below ###
def check(candidate):
    assert candidate([1, 1, 1, 2], 3) == 1

def test_check():
    check(f)