from typing import List

def f(array: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    array_2 = []
    for i in array:
        if i>0:
            array_2 += [i]
    array_2.sort(reverse=True)
    return array_2

### Unit tests below ###
def check(candidate):
    assert candidate([4, 8, 17, 89, 43, 14]) == [89, 43, 17, 14, 8, 4]

def test_check():
    check(f)