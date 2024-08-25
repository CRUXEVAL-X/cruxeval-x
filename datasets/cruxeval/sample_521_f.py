from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    m = max(nums)
    for i in range(m):
        nums.reverse()
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([43, 0, 4, 77, 5, 2, 0, 9, 77]) == [77, 9, 0, 2, 5, 77, 4, 0, 43]

def test_check():
    check(f)