def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    return s.replace('(', '[').replace(')', ']')

### Unit tests below ###
def check(candidate):
    assert candidate("(ac)") == '[ac]'

def test_check():
    check(f)