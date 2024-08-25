from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    count = len(nums)
    if count == 0:
        nums = [0] * int(nums.pop())
    elif count % 2 == 0:
        nums.clear()
    else:
        del nums[:count//2:]
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([-6, -2, 1, -3, 0, 1]) == []

def test_check():
    check(f)