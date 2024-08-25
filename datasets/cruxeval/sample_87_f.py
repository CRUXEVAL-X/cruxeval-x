from typing import List

def f(nums: List[int]) -> str:
    """"""
    ### Canonical solution below ###
    nums.reverse()
    return ''.join(map(str, nums))

### Unit tests below ###
def check(candidate):
    assert candidate([-1, 9, 3, 1, -2]) == '-2139-1'

def test_check():
    check(f)