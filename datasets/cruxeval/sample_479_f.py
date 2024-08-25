from typing import List

def f(nums: List[int], pop1: int, pop2: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    nums.pop(pop1 - 1)
    nums.pop(pop2 - 1)
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([1, 5, 2, 3, 6], 2, 4) == [1, 2, 3]

def test_check():
    check(f)