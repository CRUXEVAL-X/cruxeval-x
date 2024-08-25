from typing import List

def f(nums: List[int], spot: int, idx: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    nums.insert(spot, idx)
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([1, 0, 1, 1], 0, 9) == [9, 1, 0, 1, 1]

def test_check():
    check(f)