from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    count = len(nums)
    for i in range(-count+1, 0):
        nums.extend([nums[i], nums[i]])
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([0, 6, 2, -1, -2]) == [0, 6, 2, -1, -2, 6, 6, -2, -2, -2, -2, -2, -2]

def test_check():
    check(f)