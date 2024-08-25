from typing import List, Dict

def f(commands: List[Dict[str, int]]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    d = {}
    for c in commands:
        d.update(c)
    return d

### Unit tests below ###
def check(candidate):
    assert candidate([{"brown": 2}, {"blue": 5}, {"bright": 4}]) == {'brown': 2, 'blue': 5, 'bright': 4}

def test_check():
    check(f)