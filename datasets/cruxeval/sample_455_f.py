def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    uppers = 0
    for c in text:
        if c.isupper():
            uppers += 1
    return text.upper() if uppers >= 10 else text

### Unit tests below ###
def check(candidate):
    assert candidate('?XyZ') == '?XyZ'

def test_check():
    check(f)