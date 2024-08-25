from typing import List

def f(nums: List[int], odd1: int, odd2: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    while odd1 in nums:
        nums.remove(odd1)
    while odd2 in nums:
        nums.remove(odd2)
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3, 7, 7, 6, 8, 4, 1, 2, 3, 5, 1, 3, 21, 1, 3], 3, 1) == [2, 7, 7, 6, 8, 4, 2, 5, 21]

def test_check():
    check(f)