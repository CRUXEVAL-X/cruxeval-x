from typing import List

def f(name: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    return [name[0], name[1][::-1][0]]

### Unit tests below ###
def check(candidate):
    assert candidate("master. ") == ['m', 'a']

def test_check():
    check(f)