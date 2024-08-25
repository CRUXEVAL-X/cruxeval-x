from typing import List, Union

def f(arr1: List[int], arr2: List[Union[int, str, List[int]]]) -> List[Union[int, str, List[int]]]:
    """"""
    ### Canonical solution below ###
    new_arr = arr1.copy()
    new_arr.extend(arr2)
    return new_arr

### Unit tests below ###
def check(candidate):
    assert candidate([5, 1, 3, 7, 8], ['', 0, -1, []]) == [5, 1, 3, 7, 8, '', 0, -1, []]

def test_check():
    check(f)