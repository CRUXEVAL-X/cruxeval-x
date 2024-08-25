from typing import List

def f(nums: List[int]) -> int:
    """"""
    ### Canonical solution below ###
    counts = 0
    for i in nums:
        if str(i).isdecimal():
            if counts == 0:
                counts += 1
    return counts

### Unit tests below ###
def check(candidate):
    assert candidate([0, 6, 2, -1, -2]) == 1

def test_check():
    check(f)