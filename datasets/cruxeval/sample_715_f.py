def f(text: str, char: str) -> bool:
    """"""
    ### Canonical solution below ###
    return text.count(char) % 2 != 0

### Unit tests below ###
def check(candidate):
    assert candidate('abababac', 'a') == False

def test_check():
    check(f)