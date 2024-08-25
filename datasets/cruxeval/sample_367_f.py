from typing import List

def f(nums: List[int], rmvalue: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    res = nums[:]
    while rmvalue in res:
        popped = res.pop(res.index(rmvalue))
        if popped != rmvalue:
            res.append(popped)
    return res

### Unit tests below ###
def check(candidate):
    assert candidate([6, 2, 1, 1, 4, 1], 5) == [6, 2, 1, 1, 4, 1]

def test_check():
    check(f)