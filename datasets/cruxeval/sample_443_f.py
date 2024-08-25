def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    for space in text:
        if space == ' ':
            text = text.lstrip()
        else:
            text = text.replace('cd', space)
    return text

### Unit tests below ###
def check(candidate):
    assert candidate("lorem ipsum") == 'lorem ipsum'

def test_check():
    check(f)