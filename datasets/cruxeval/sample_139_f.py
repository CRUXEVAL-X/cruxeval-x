from typing import List, Union

def f(first: List[int], second: List[int]) -> Union[str, List[int]]:
    """"""
    ### Canonical solution below ###
    if len(first) < 10 or len(second) < 10:
        return 'no'
    for i in range(5):
        if first[i] != second[i]:
            return 'no'
    first.extend(second)
    return first

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 1], [1, 1, 2]) == 'no'

def test_check():
    check(f)