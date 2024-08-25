from typing import List

def f(s1: str, s2: str) -> List[int]:
    """"""
    ### Canonical solution below ###
    res = []
    i = s1.rfind(s2)
    while i != -1:
        res.append(i+len(s2)-1)
        i = s1.rfind(s2, 0, i)
    return res

### Unit tests below ###
def check(candidate):
    assert candidate('abcdefghabc', 'abc') == [10, 2]

def test_check():
    check(f)