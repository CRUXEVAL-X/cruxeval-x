def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    for char in text:
        if not char.isspace():
            return False
    return True

### Unit tests below ###
def check(candidate):
    assert candidate('     i') == False

def test_check():
    check(f)