from typing import List

def f(nums: List[int]) -> str:
    """"""
    ### Canonical solution below ###
    count = len(nums)
    score = {0: "F", 1: "E", 2: "D", 3: "C", 4: "B", 5: "A", 6: ""}
    result = []
    for i in range(count):
        result.append(score.get(nums[i]))
    return ''.join(result)

### Unit tests below ###
def check(candidate):
    assert candidate([4, 5]) == 'BA'

def test_check():
    check(f)