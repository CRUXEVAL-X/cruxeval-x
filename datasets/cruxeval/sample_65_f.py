from typing import List

def f(nums: List[int], index: int) -> int:
    """"""
    ### Canonical solution below ###
    return nums[index] % 42 + nums.pop(index) * 2

### Unit tests below ###
def check(candidate):
    assert candidate([3, 2, 0, 3, 7], 3) == 9

def test_check():
    check(f)