def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    return ''.join((c.casefold() for c in s))

### Unit tests below ###
def check(candidate):
    assert candidate('abcDEFGhIJ') == 'abcdefghij'

def test_check():
    check(f)