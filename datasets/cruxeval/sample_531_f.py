def f(text: str, x: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.removeprefix(x) == text:
        return f(text[1:], x)
    else:
        return text

### Unit tests below ###
def check(candidate):
    assert candidate("Ibaskdjgblw asdl ", "djgblw") == 'djgblw asdl '

def test_check():
    check(f)