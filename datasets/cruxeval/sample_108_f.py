from typing import Union, List, Dict

def f(var: int) -> int:
    """"""
    ### Canonical solution below ###
    amount = len(var) if type(var) == list else 0
    if type(var) == dict:
        amount = len(var.keys())
    nonzero = amount if amount > 0 else 0
    return nonzero

### Unit tests below ###
def check(candidate):
    assert candidate(1) == 0

def test_check():
    check(f)