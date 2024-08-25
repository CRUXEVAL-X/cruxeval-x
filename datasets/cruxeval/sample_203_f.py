from typing import Dict, Any

def f(d: Dict[str, str]) -> Dict[str, str]:
    """"""
    ### Canonical solution below ###
    d.clear()
    return d

### Unit tests below ###
def check(candidate):
    assert candidate({'a': '3', 'b': '-1', 'c': 'Dum'}) == {}

def test_check():
    check(f)