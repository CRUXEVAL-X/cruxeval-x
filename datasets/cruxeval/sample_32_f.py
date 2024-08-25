def f(s: str, sep: str) -> str:
    """"""
    ### Canonical solution below ###
    reverse = ['*' + e for e in s.split(sep)]
    return ';'.join(reversed(reverse))

### Unit tests below ###
def check(candidate):
    assert candidate('volume', 'l') == '*ume;*vo'

def test_check():
    check(f)