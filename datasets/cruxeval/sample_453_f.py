def f(string: str, c: str) -> bool:
    """"""
    ### Canonical solution below ###
    return string.endswith(c)

### Unit tests below ###
def check(candidate):
    assert candidate('wrsch)xjmb8', 'c') == False

def test_check():
    check(f)