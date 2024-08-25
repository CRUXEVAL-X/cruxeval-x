def f(s: str, c: str) -> str:
    """"""
    ### Canonical solution below ###
    s = s.split(' ')
    return ((c + "  ") + ("  ".join(s[::-1])))

### Unit tests below ###
def check(candidate):
    assert candidate('Hello There', '*') == '*  There  Hello'

def test_check():
    check(f)