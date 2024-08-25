from typing import Dict, List

def f(d: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """"""
    ### Canonical solution below ###
    dCopy = d.copy()
    for key, value in dCopy.items():
        for i in range(len(value)):
            value[i] = value[i].upper()
    return dCopy

### Unit tests below ###
def check(candidate):
    assert candidate({'X': ['x', 'y']}) == {'X': ['X', 'Y']}

def test_check():
    check(f)