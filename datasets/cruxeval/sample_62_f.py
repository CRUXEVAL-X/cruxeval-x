from typing import Dict, Tuple

def f(user: Dict[str, str]) -> Tuple[str, str, str, str]:
    """"""
    ### Canonical solution below ###
    if len(list(user.keys())) > len(list(user.values())):
        return tuple(user.keys())
    return tuple(user.values())

### Unit tests below ###
def check(candidate):
    assert candidate({"eating" : "ja", "books" : "nee", "piano" : "coke", "excitement" : "zoo"}) == ('ja', 'nee', 'coke', 'zoo')

def test_check():
    check(f)