from typing import Dict

def f(tags: Dict[str, str]) -> str:
    """"""
    ### Canonical solution below ###
    resp = ""
    for key in tags:
        resp += key + " "
    return resp

### Unit tests below ###
def check(candidate):
    assert candidate({"3":"3","4":"5"}) == '3 4 '

def test_check():
    check(f)