from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    count = len(nums)
    for i in range(0, count):
        nums.insert(i, nums[i]*2)
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([2, 8, -2, 9, 3, 3]) == [4, 4, 4, 4, 4, 4, 2, 8, -2, 9, 3, 3]

def test_check():
    check(f)