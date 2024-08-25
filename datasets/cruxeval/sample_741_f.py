from typing import List

def f(nums: List[int], p: int) -> int:
    """"""
    ### Canonical solution below ###
    prev_p = p - 1
    if prev_p < 0: prev_p = len(nums) - 1
    return nums[prev_p]

### Unit tests below ###
def check(candidate):
    assert candidate([6, 8, 2, 5, 3, 1, 9, 7], 6) == 1

def test_check():
    check(f)