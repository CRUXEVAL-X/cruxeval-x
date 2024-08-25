from typing import List

def f(array: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    result = []
    index = 0
    while index < len(array):
        result.append(array.pop())
        index += 2
    return result

### Unit tests below ###
def check(candidate):
    assert candidate([8, 8, -4, -9, 2, 8, -1, 8]) == [8, -1, 8]

def test_check():
    check(f)