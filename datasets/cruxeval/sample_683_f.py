from typing import Dict

def f(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    result = dict1.copy()
    result.update([(__, dict2[__]) for __ in dict2])
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({'disface': 9, 'cam': 7}, {'mforce': 5}) == {'disface': 9, 'cam': 7, 'mforce': 5}

def test_check():
    check(f)