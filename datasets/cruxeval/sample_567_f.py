from typing import List

def f(s: str, n: int) -> List[str]:
    """"""
    ### Canonical solution below ###
    ls = s.rsplit()
    out = []
    while len(ls) >= n:
        out += ls[-n:]
        ls = ls[:-n]
    return ls + ['_'.join(out)]

### Unit tests below ###
def check(candidate):
    assert candidate('one two three four five', 3) == ['one', 'two', 'three_four_five']

def test_check():
    check(f)