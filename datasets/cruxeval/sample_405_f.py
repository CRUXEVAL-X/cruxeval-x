from typing import List

def f(xs: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    new_x = xs[0] - 1
    xs.pop(0)
    while(new_x <= xs[0]):
        xs.pop(0)
        new_x -= 1
    xs.insert(0, new_x)
    return xs

### Unit tests below ###
def check(candidate):
    assert candidate([6, 3, 4, 1, 2, 3, 5]) == [5, 3, 4, 1, 2, 3, 5]

def test_check():
    check(f)