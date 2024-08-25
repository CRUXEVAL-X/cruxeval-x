def f(text: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    if text:
        text = text.removeprefix(char)
        text = text.removeprefix(text[-1])
        text = text[:-1] + text[-1].capitalize()
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('querist', 'u') == 'querisT'

def test_check():
    check(f)