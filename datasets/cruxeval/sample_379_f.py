from typing import List, Union

def f(nums: List[int]) -> Union[bool, List[int]]:
    """"""
    ### Canonical solution below ###
    for i in range(len(nums) - 1, -1, -3):
        if nums[i] == 0:
            nums.clear()
            return False
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([0, 0, 1, 2, 1]) == False

def test_check():
    check(f)