def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    return ', '.join(text.splitlines())

### Unit tests below ###
def check(candidate):
    assert candidate("BYE\nNO\nWAY") == 'BYE, NO, WAY'

def test_check():
    check(f)