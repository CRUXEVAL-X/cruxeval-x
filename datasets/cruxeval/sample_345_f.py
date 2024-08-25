from typing import Tuple

def f(a: str, b: str) -> Tuple[str, str]:
    """"""
    ### Canonical solution below ###
    if a < b:
        return (b, a)
    return (a, b)

### Unit tests below ###
def check(candidate):
    assert candidate('ml', 'mv') == ('mv', 'ml')

def test_check():
    check(f)