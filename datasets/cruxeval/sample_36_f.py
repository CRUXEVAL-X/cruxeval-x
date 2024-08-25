def f(text: str, chars: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.rstrip(chars) if text else text

### Unit tests below ###
def check(candidate):
    assert candidate('ha', '') == 'ha'

def test_check():
    check(f)