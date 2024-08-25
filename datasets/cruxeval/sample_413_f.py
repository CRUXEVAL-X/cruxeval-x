def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    return '{}{}{}'.format(s[3:], s[2], s[5:8])

### Unit tests below ###
def check(candidate):
    assert candidate('jbucwc') == 'cwcuc'

def test_check():
    check(f)