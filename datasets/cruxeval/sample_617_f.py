def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.isascii():
        return 'ascii'
    else:
        return 'non ascii'

### Unit tests below ###
def check(candidate):
    assert candidate("<<<<") == 'ascii'

def test_check():
    check(f)