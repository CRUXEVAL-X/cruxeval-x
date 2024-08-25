def f(text: str, count: int) -> str:
    """"""
    ### Canonical solution below ###
    for i in range(count):
        text = ''.join(reversed(text))
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('aBc, ,SzY', 2) == 'aBc, ,SzY'

def test_check():
    check(f)