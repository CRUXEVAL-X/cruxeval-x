from typing import List, Union

def f(nums: List[Union[str, int]]) -> List[int]:
    """"""
    ### Canonical solution below ###
    digits = []
    for num in nums:
        if (isinstance(num, str) and num.isnumeric()) or isinstance(num, int):
            digits.append(num)
    digits = list(map(int, digits))
    return digits

### Unit tests below ###
def check(candidate):
    assert candidate([0, 6, '1', '2', 0]) == [0, 6, 1, 2, 0]

def test_check():
    check(f)