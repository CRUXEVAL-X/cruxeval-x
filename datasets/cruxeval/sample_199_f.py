def f(s: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    base = char * (s.count(char) + 1)
    return s.removesuffix(base)

### Unit tests below ###
def check(candidate):
    assert candidate('mnmnj krupa...##!@#!@#$$@##', '@') == 'mnmnj krupa...##!@#!@#$$@##'

def test_check():
    check(f)