def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    if text == '42.42':
        return True
    for i in range(3, len(text) - 3):
        if text[i] == '.' and text[i - 3:].isdigit() and text[:i].isdigit():
            return True
    return False

### Unit tests below ###
def check(candidate):
    assert candidate("123E-10") == False

def test_check():
    check(f)