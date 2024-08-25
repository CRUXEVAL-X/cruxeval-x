def f(s1: str, s2: str) -> str:
    """"""
    ### Canonical solution below ###
    if s2.endswith(s1):
        s2 = s2[:len(s1) * -1]
    return s2

### Unit tests below ###
def check(candidate):
    assert candidate("he", "hello") == 'hello'

def test_check():
    check(f)