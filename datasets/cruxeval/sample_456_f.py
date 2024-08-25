def f(s: str, tab: int) -> str:
    """"""
    ### Canonical solution below ###
    return s.expandtabs(tab)

### Unit tests below ###
def check(candidate):
    assert candidate("Join us in Hungary", 4) == 'Join us in Hungary'

def test_check():
    check(f)