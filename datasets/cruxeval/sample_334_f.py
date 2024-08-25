from typing import List

def f(a: str, b: List[str]) -> str:
    """"""
    ### Canonical solution below ###
    return a.join(b)

### Unit tests below ###
def check(candidate):
    assert candidate('00', ['nU', ' 9 rCSAz', 'w', ' lpA5BO', 'sizL', 'i7rlVr']) == 'nU00 9 rCSAz00w00 lpA5BO00sizL00i7rlVr'

def test_check():
    check(f)