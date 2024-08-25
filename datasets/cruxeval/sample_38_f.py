def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    return string.title().replace(' ', '')

### Unit tests below ###
def check(candidate):
    assert candidate('1oE-err bzz-bmm') == '1Oe-ErrBzz-Bmm'

def test_check():
    check(f)