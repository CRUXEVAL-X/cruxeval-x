from typing import Dict

def f(zoo: Dict[str, str]) -> Dict[str, str]:
    """"""
    ### Canonical solution below ###
    return dict((v, k) for k, v in zoo.items())

### Unit tests below ###
def check(candidate):
    assert candidate({'AAA': 'fr'}) == {'fr': 'AAA'}

def test_check():
    check(f)