from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    count = len(nums)
    for i in range(0, count // 2):
        nums[i], nums[count-i-1] = nums[count-i-1], nums[i]
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([2, 6, 1, 3, 1]) == [1, 3, 1, 6, 2]

def test_check():
    check(f)