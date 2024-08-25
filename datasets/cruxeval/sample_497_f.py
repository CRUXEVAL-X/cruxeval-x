from typing import List

def f(n: int) -> List[str]:
    """"""
    ### Canonical solution below ###
    b = list(str(n))
    for i in range(2,len(b)): b[i] += '+'
    return b

### Unit tests below ###
def check(candidate):
    assert candidate(44) == ['4', '4']

def test_check():
    check(f)