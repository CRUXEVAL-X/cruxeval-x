from typing import Dict, Tuple

def f(d: Dict[str, int]) -> Tuple[Tuple[str, int], Tuple[str, int]]:
    """"""
    ### Canonical solution below ###
    i = iter(d.items())
    return next(i), next(i)

### Unit tests below ###
def check(candidate):
    assert candidate({'a': 123, 'b': 456, 'c': 789}) == (('a', 123), ('b', 456))

def test_check():
    check(f)