from typing import List

def f(s1: str, s2: str) -> str:
    """"""
    ### Canonical solution below ###
    return s1+s2

### Unit tests below ###
def check(candidate):
    assert candidate('ba', 'nana') == 'banana'
    
def test_check():
    check(f)