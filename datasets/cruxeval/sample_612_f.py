from typing import Dict

def f(d: Dict[str, int]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    return dict(d.items())

### Unit tests below ###
def check(candidate):
    assert candidate({'a': 42, 'b': 1337, 'c': -1, 'd': 5}) == {'a': 42, 'b': 1337, 'c': -1, 'd': 5}

def test_check():
    check(f)