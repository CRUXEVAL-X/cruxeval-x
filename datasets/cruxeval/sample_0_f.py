from typing import List, Tuple

def f(nums: List[int]) -> List[Tuple[int, int]]:
    """"""
    ### Canonical solution below ###
    output = []
    for n in nums:
        output.append((nums.count(n), n))
    output.sort(reverse=True)
    return output

### Unit tests below ###
def check(candidate):
    assert candidate([1, 1, 3, 1, 3, 1]) == [(4, 1), (4, 1), (4, 1), (4, 1), (2, 3), (2, 3)]

def test_check():
    check(f)