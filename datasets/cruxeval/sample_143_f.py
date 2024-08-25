def f(s: str, n: str) -> bool:
    """"""
    ### Canonical solution below ###
    return s.casefold() == n.casefold()

### Unit tests below ###
def check(candidate):
    assert candidate("daaX", "daaX") == True

def test_check():
    check(f)