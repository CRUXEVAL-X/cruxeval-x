def f(text: str, n: int) -> str:
    """"""
    ### Canonical solution below ###
    length = len(text)
    return text[length*(n%4):length ]

### Unit tests below ###
def check(candidate):
    assert candidate('abc', 1) == ''

def test_check():
    check(f)