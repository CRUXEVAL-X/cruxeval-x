from typing import List

def f(text: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    ls = text.split()
    lines = " ".join(ls[::3]).splitlines()
    res = []
    for i in range(2):
        ln = ls[1::3]
        if 3 * i + 1 < len(ln):
            res.append(" ".join(ln[3 * i:3 * (i + 1)]))
    return lines + res

### Unit tests below ###
def check(candidate):
    assert candidate("echo hello!!! nice!") == ['echo']

def test_check():
    check(f)