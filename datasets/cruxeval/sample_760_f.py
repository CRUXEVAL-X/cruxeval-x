from typing import Dict, List

def f(d: Dict[str, int]) -> List[str]:
    """"""
    ### Canonical solution below ###
    l = []
    while len(d) > 0:
        key = d.popitem()[0]
        l.append(key)
    return l

### Unit tests below ###
def check(candidate):
    assert candidate({'f': 1, 'h': 2, 'j': 3, 'k': 4}) == ['k', 'j', 'h', 'f']

def test_check():
    check(f)