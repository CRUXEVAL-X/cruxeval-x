from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    for i in range(len(nums)):
        if nums[i] % 3 == 0:
            nums.append(nums[i])
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([1, 3]) == [1, 3, 3]

def test_check():
    check(f)