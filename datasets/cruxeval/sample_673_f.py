def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    if string.isupper():
        return string.lower()
    elif string.islower():
        return string.upper()
    return string

### Unit tests below ###
def check(candidate):
    assert candidate("cA") == 'cA'

def test_check():
    check(f)