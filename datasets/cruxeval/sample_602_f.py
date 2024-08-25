from typing import List

def f(nums: List[int], target: int) -> int:
    """"""
    ### Canonical solution below ###
    cnt = nums.count(target)
    return cnt * 2

### Unit tests below ###
def check(candidate):
    assert candidate([1, 1], 1) == 4

def test_check():
    check(f)