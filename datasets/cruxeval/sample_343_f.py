from typing import List, Any, Union

def f(array: List[Union[List[int], int]], elem: List[Union[List[int], int]]) -> List[Union[List[int], int]]:
    """"""
    ### Canonical solution below ###
    array.extend(elem)
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([[1, 2, 3], [1, 2], 1], [[1, 2, 3], 3, [2, 1]]) == [[1, 2, 3], [1, 2], 1, [1, 2, 3], 3, [2, 1]]

def test_check():
    check(f)