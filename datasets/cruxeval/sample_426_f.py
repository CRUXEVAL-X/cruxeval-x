from typing import List, Any

def f(numbers: List[int], elem: int, idx: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    numbers.insert(idx, elem)
    return numbers

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3], 8, 5) == [1, 2, 3, 8]

def test_check():
    check(f)