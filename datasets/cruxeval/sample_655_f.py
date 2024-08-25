def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    return s.replace('a', '').replace('r', '')

### Unit tests below ###
def check(candidate):
    assert candidate('rpaar') == 'p'

def test_check():
    check(f)