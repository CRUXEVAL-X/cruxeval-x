from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    nums = [y for y in nums if y > 0]
    if len(nums) <= 3:
        return nums
    nums.reverse()
    half = len(nums)//2
    return nums[:half] + [0]*5 + nums[half:]

### Unit tests below ###
def check(candidate):
    assert candidate([10, 3, 2, 2, 6, 0]) == [6, 2, 0, 0, 0, 0, 0, 2, 3, 10]

def test_check():
    check(f)