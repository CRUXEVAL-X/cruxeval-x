from typing import List

def f(seq: List[str], v: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    a = []
    for i in seq:
        if i.endswith(v):
            a.append(i*2)
    return a

### Unit tests below ###
def check(candidate):
    assert candidate([ 'oH', 'ee', 'mb', 'deft', 'n', 'zz', 'f', 'abA' ], 'zz') == ['zzzz']

def test_check():
    check(f)