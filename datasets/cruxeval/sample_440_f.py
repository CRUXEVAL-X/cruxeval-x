def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.isdecimal():
        return 'yes'
    else:
        return 'no'

### Unit tests below ###
def check(candidate):
    assert candidate("abc") == 'no'

def test_check():
    check(f)