from typing import Dict

def f(cart: Dict[int,int]) -> Dict[int,int]:
    """"""
    ### Canonical solution below ###
    while len(cart) > 5:
        cart.popitem()
    return cart

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)