from typing import List, Union

def f(array: List[int], x: int, i: int) -> Union[str, List[int]]:
    """"""
    ### Canonical solution below ###
    if i < -len(array) or i > len(array) - 1:
        return 'no'
    temp = array[i]
    array[i] = x
    return array

### Unit tests below ###
def check(candidate):
    assert candidate([1,2,3,4,5,6,7,8,9,10], 11, 4) == [1, 2, 3, 4, 11, 6, 7, 8, 9, 10]

def test_check():
    check(f)