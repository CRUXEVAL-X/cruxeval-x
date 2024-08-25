from typing import Dict

def f(sb: str) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    d = {}
    for s in sb:
        d[s] = d.get(s, 0) + 1
    return d

### Unit tests below ###
def check(candidate):
    assert candidate('meow meow') == {'m': 2, 'e': 2, 'o': 2, 'w': 2, ' ': 1}

def test_check():
    check(f)