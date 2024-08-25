def f(text: str, char: str, replace: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.replace(char, replace)

### Unit tests below ###
def check(candidate):
    assert candidate('a1a8', '1', 'n2') == 'an2a8'

def test_check():
    check(f)