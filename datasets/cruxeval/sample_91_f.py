from typing import List

def f(s: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    d = dict.fromkeys(s, 0)
    return list(d.keys())

### Unit tests below ###
def check(candidate):
    assert candidate("12ab23xy") == ['1', '2', 'a', 'b', '3', 'x', 'y']

def test_check():
    check(f)