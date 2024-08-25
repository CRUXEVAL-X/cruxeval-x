from typing import Dict, Union

def f(dictionary: Dict[str, int]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    dictionary['1049'] = 55
    key, value = dictionary.popitem()
    dictionary[key] = value
    return dictionary

### Unit tests below ###
def check(candidate):
    assert candidate({'noeohqhk': 623}) == {'noeohqhk': 623, '1049': 55}

def test_check():
    check(f)