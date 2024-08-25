def f(string: str) -> bool:
    """"""
    ### Canonical solution below ###
    if string.isupper():
        return True
    else:
        return False

### Unit tests below ###
def check(candidate):
    assert candidate('Ohno') == False

def test_check():
    check(f)