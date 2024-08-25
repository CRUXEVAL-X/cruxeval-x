def f(text: str, char: str) -> bool:
    """"""
    ### Canonical solution below ###
    return char.islower() and text.islower()

### Unit tests below ###
def check(candidate):
    assert candidate('abc', 'e') == True

def test_check():
    check(f)