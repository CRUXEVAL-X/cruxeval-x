from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    middle = len(nums)//2
    return nums[middle:] + nums[0:middle]

### Unit tests below ###
def check(candidate):
    assert candidate([1, 1, 1]) == [1, 1, 1]

def test_check():
    check(f)