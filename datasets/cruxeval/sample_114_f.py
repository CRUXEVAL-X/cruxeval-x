from typing import List

def f(text: str, sep: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    return text.rsplit(sep, maxsplit=2)

### Unit tests below ###
def check(candidate):
    assert candidate("a-.-.b", "-.") == ['a', '', 'b']

def test_check():
    check(f)