from typing import Dict, List

def f(d1: Dict[int, List[int]], d2: Dict[int, List[int]]) -> int:
    """"""
    ### Canonical solution below ###
    mmax = 0
    for k1 in d1:
        if p := len(d1[k1])+len(d2.get(k1, [])):
            if p > mmax:
                mmax = p
    return mmax

### Unit tests below ###
def check(candidate):
    assert candidate({ 0: [], 1: [] }, { 0: [0, 0, 0, 0], 2: [2, 2, 2] }) == 4

def test_check():
    check(f)