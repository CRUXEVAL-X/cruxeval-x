from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    asc, desc = nums.copy(), []
    asc.reverse()
    desc = asc[:len(asc)//2]
    return desc + asc + desc

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)