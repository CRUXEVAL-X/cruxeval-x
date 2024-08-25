def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.istitle():
        if len(text) > 1 and text.lower() != text:
            return text[0].lower() + text[1:]
    elif text.isalpha():
        return text.capitalize()
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('') == ''

def test_check():
    check(f)