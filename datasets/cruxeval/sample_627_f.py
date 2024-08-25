from typing import List, Tuple

def f(parts: List[Tuple[str, int]]) -> List[int]:
    """"""
    ### Canonical solution below ###
    return list(dict(parts).values())

### Unit tests below ###
def check(candidate):
    assert candidate([('u', 1), ('s', 7), ('u', -5)]) == [-5, 7]

def test_check():
    check(f)