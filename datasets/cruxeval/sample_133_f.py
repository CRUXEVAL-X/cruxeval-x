from typing import List

def f(nums: List[int], elements: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    result = []
    for i in range(len(elements)):
        result.append(nums.pop())
    return nums

### Unit tests below ###
def check(candidate):
    assert candidate([7, 1, 2, 6, 0, 2], [9, 0, 3]) == [7, 1, 2]

def test_check():
    check(f)