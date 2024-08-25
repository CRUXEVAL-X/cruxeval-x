def f(text: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    if char in text:
        if not text.startswith(char):
            text = text.replace(char,'')
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('\\foo', '\\') == '\\foo'

def test_check():
    check(f)