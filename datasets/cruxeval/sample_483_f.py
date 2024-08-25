def f(text: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    return ' '.join(text.split(char, len(text)))

### Unit tests below ###
def check(candidate):
    assert candidate('a', 'a') == ' '

def test_check():
    check(f)