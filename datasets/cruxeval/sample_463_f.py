from typing import Dict

def f(dict: Dict[int, int]) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    result = dict.copy()
    remove_keys = []
    for k, v in dict.items():
        if v in dict:
            del result[k]
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({-1: -1, 5: 5, 3: 6, -4: -4}) == {3: 6}

def test_check():
    check(f)