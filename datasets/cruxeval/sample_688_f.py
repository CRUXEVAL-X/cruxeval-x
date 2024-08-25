from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    l = []
    for i in nums:
        if i not in l:
            l.append(i)
    return l

### Unit tests below ###
def check(candidate):
    assert candidate([3, 1, 9, 0, 2, 0, 8]) == [3, 1, 9, 0, 2, 8]

def test_check():
    check(f)