from typing import List

def f(nums: List[int], mos: List[int]) -> bool:
    """"""
    ### Canonical solution below ###
    for num in mos:
        nums.pop(nums.index(num))
    nums.sort()
    for num in mos:
        nums += [num]
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

### Unit tests below ###
def check(candidate):
    assert candidate([3, 1, 2, 1, 4, 1], [1]) == False

def test_check():
    check(f)