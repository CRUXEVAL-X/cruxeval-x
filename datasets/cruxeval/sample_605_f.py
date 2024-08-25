from typing import List

def f(nums: List[int]) -> str:
    """"""
    ### Canonical solution below ###
    nums.clear()
    return "quack"

### Unit tests below ###
def check(candidate):
    assert candidate([2, 5, 1, 7, 9, 3]) == 'quack'

def test_check():
    check(f)