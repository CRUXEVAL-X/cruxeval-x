from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    count = len(nums)
    while len(nums) > (count//2):
        nums.clear()
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([2, 1, 2, 3, 1, 6, 3, 8]) == []

def test_check():
    check(f)