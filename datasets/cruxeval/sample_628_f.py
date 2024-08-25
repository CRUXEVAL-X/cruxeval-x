from typing import List

def f(nums: List[int], delete: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    nums.remove(delete)
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([4, 5, 3, 6, 1], 5) == [4, 3, 6, 1]

def test_check():
    check(f)