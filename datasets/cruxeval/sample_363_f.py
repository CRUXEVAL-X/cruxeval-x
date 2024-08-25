from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    nums.sort()
    n = len(nums)
    new_nums = [nums[n//2]]
    
    if n % 2 == 0:
        new_nums = [nums[n//2 - 1], nums[n//2]]
    
    for i in range(0, n//2):
        new_nums.insert(0, nums[n-i-1])
        new_nums.append(nums[i])
    return new_nums

### Unit tests below ###
def check(candidate):
    assert candidate([1]) == [1]

def test_check():
    check(f)