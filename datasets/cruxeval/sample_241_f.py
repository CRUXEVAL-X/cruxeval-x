def f(postcode: str) -> str:
    """"""
    ### Canonical solution below ###
    return postcode[postcode.index('C'):]

### Unit tests below ###
def check(candidate):
    assert candidate('ED20 CW') == 'CW'

def test_check():
    check(f)