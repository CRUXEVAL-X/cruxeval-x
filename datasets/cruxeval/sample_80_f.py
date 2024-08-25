def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    return ''.join(reversed(s.rstrip()))

### Unit tests below ###
def check(candidate):
    assert candidate('ab        ') == 'ba'

def test_check():
    check(f)