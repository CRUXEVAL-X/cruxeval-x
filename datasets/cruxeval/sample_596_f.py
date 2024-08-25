from typing import List

def f(txt: List[str], alpha: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    txt = sorted(txt)
    if txt.index(alpha) % 2 == 0:
        return txt[::-1]
    return txt

### Unit tests below ###
def check(candidate):
    assert candidate(['8', '9', '7', '4', '3', '2'], '9') == ['2', '3', '4', '7', '8', '9']

def test_check():
    check(f)