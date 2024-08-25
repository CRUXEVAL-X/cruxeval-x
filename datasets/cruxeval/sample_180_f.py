from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    a = -1
    b = nums[1:]
    while a <= b[0]:
        nums.remove(b[0])
        a = 0
        b = b[1:]
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([-1, 5, 3, -2, -6, 8, 8]) == [-1, -2, -6, 8, 8]

def test_check():
    check(f)