from typing import List, Dict

def f(array1: List[int], array2: List[int]) -> Dict[int, List[int]]:
    """"""
    ### Canonical solution below ###
    result = dict.fromkeys(array1)
    for key in result:
        result[key] = [el for el in array2 if key * 2 > el]
    return result

### Unit tests below ###
def check(candidate):
    assert candidate([0, 132], [5, 991, 32, 997]) == {0: [], 132: [5, 32]}

def test_check():
    check(f)