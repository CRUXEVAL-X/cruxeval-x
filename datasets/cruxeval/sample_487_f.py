from typing import Dict, List

def f(dict: Dict[int, str]) -> List[int]:
    """"""
    ### Canonical solution below ###
    even_keys = []
    for key in dict.keys():
        if key % 2 == 0:
            even_keys.append(key)
    return even_keys

### Unit tests below ###
def check(candidate):
    assert candidate({ 4: 'a' }) == [4]

def test_check():
    check(f)