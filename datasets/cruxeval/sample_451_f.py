def f(text: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    text = list(text)
    for count, item in enumerate(text):
        if item == char:
            text.remove(item)
            return ''.join(text)
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('pn', 'p') == 'n'

def test_check():
    check(f)