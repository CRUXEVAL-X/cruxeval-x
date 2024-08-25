from typing import List

def f(nums: List[int]) -> bool:
    """"""
    ### Canonical solution below ###
    if nums[::-1] == nums:
        return True
    return False

### Unit tests below ###
def check(candidate):
    assert candidate([0, 3, 6, 2]) == False

def test_check():
    check(f)