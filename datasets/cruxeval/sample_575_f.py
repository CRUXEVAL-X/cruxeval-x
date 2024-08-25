from typing import List

def f(nums: List[int], val: int) -> int:
    """"""
    ### Canonical solution below ###
    new_list = []
    [new_list.extend([i] * val) for i in nums]
    return sum(new_list)

### Unit tests below ###
def check(candidate):
    assert candidate([10, 4], 3) == 42

def test_check():
    check(f)