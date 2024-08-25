from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    count = len(nums)
    for i in range(count-1, 0, -2):
        nums.insert(i, nums.pop(0) + nums.pop(0))
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([-5, 3, -2, -3, -1, 3, 5]) == [5, -2, 2, -5]

def test_check():
    check(f)