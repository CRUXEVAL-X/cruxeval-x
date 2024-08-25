def f(s: str, l: int) -> str:
    """"""
    ### Canonical solution below ###
    return s.ljust(l, '=').rpartition('=')[0]

### Unit tests below ###
def check(candidate):
    assert candidate('urecord', 8) == 'urecord'

def test_check():
    check(f)