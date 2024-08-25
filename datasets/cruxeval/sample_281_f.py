from typing import Dict, Any

def f(c: Dict[Any, Any], index: int, value: int) -> Dict[Any, Any]:
    """"""
    ### Canonical solution below ###
    c[index] = value
    if value >= 3:
        c.update({'message' : 'xcrWt'})
    else: 
        del c['message']
    return c

### Unit tests below ###
def check(candidate):
    assert candidate({1: 2, 3: 4, 5: 6, 'message': 'qrTHo'}, 8, 2) == {1: 2, 3: 4, 5: 6, 8: 2}

def test_check():
    check(f)