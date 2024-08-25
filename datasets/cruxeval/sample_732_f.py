from typing import Dict

def f(char_freq: Dict[str, int]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    result = {}
    for k, v in char_freq.copy().items():
        result[k] = v // 2
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({'u': 20, 'v': 5, 'b': 7, 'w': 3, 'x': 3}) == {'u': 10, 'v': 2, 'b': 3, 'w': 1, 'x': 1}

def test_check():
    check(f)