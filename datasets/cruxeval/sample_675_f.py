from typing import List

def f(nums: List[int], sort_count: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    nums.sort()
    return nums[:sort_count]

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 2, 3, 4, 5], 1) == [1]

def test_check():
    check(f)