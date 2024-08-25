def f(text: str, char: str) -> int:
    """"""
    ### Canonical solution below ###
    return text.rindex(char)

### Unit tests below ###
def check(candidate):
    assert candidate("breakfast", "e") == 2

def test_check():
    check(f)