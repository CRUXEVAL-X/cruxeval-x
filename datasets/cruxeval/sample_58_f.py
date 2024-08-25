from typing import List

def f(nums: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    count = len(nums)
    for i in [i % 2 for i in range(count)]:
        nums.append(nums[i])
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([-1, 0, 0, 1, 1]) == [-1, 0, 0, 1, 1, -1, 0, -1, 0, -1]

def test_check():
    check(f)