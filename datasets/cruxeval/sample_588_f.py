from typing import List

def f(items: List[str], target: str) -> int:
    """"""
    ### Canonical solution below ###
    if target in items:
        return items.index(target)
    return -1

### Unit tests below ###
def check(candidate):
    assert candidate(['''1''', '+', '-', '**', '//', '*', '+'], '**') == 3

def test_check():
    check(f)