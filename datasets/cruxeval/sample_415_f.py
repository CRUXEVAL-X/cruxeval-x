from typing import List, Tuple, Dict

def f(array: List[Tuple[int, int]]) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    d = dict(array)
    for key, value in d.items():
        if value < 0 or value > 9:
            return None
    return d

### Unit tests below ###
def check(candidate):
    assert candidate(((8, 5), (8, 2), (5, 3))) == {8: 2, 5: 3}

def test_check():
    check(f)