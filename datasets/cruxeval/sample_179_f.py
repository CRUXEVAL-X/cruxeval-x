from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    # Pass in a copy to avoid modifying nums
    nums = nums[:]
    count = len(nums)
    for i in range(-count+1, 0):
        nums.insert(0, nums[i])
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([7, 1, 2, 6, 0, 2]) == [2, 0, 6, 2, 1, 7, 1, 2, 6, 0, 2]

def test_check():
    check(f)