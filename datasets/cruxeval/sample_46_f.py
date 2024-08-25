from typing import List

def f(l: List[str], c: str) -> str:
    """"""
    ### Canonical solution below ###
    return c.join(l)

### Unit tests below ###
def check(candidate):
    assert candidate(['many', 'letters', 'asvsz', 'hello', 'man'], '') == 'manylettersasvszhelloman'

def test_check():
    check(f)