from typing import List

def f(digits: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    digits.reverse()
    if len(digits) < 2:
        return digits
    for i in range(0, len(digits), 2):
        digits[i], digits[i+1] = digits[i+1], digits[i]
    return digits

### Unit tests below ###
def check(candidate):
    assert candidate([1,2]) == [1, 2]

def test_check():
    check(f)