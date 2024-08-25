from typing import List

def f(nums: List[int], idx: int, added: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    nums[idx:idx] = (added,)
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([2, 2, 2, 3, 3], 2, 3) == [2, 2, 3, 2, 3, 3]

def test_check():
    check(f)