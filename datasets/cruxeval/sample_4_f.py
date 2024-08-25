from typing import List

def f(array: List[str]) -> str:
    """"""
    ### Canonical solution below ###
    s = ' '
    s += ''.join(array)
    return s

### Unit tests below ###
def check(candidate):
    assert candidate([' ', '  ', '    ', '   ']) == '           '

def test_check():
    check(f)