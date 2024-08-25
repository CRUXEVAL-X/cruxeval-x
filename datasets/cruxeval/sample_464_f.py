from typing import Union

def f(ans: str) -> Union[int, str]:
    """"""
    ### Canonical solution below ###
    if ans.isdecimal():
        total = int(ans) * 4 - 50
        total -= len([c for c in list(ans) if c not in '02468']) * 100
        return total
    return 'NAN'

### Unit tests below ###
def check(candidate):
    assert candidate('0') == -50

def test_check():
    check(f)