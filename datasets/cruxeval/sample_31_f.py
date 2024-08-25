def f(string: str) -> int:
    """"""
    ### Canonical solution below ###
    upper = 0
    for c in string:
        if c.isupper():
            upper += 1
    return upper * (2,1)[upper % 2]

### Unit tests below ###
def check(candidate):
    assert candidate('PoIOarTvpoead') == 8

def test_check():
    check(f)