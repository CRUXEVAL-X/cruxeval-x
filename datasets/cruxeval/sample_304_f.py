from typing import Dict

def f(d: Dict[int, int]) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    key1 = sorted(d.items(), key=lambda x: x[0], reverse=True)[0][0]
    val1 = d.pop(key1)
    key2 = sorted(d.items(), key=lambda x: x[0], reverse=True)[0][0]
    val2 = d.pop(key2)
    return dict({key1: val1, key2: val2})

### Unit tests below ###
def check(candidate):
    assert candidate({2: 3, 17: 3, 16: 6, 18: 6, 87: 7}) == {87: 7, 18: 6}

def test_check():
    check(f)