def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    for c in text:
        if not c.isnumeric():
            return False
    return bool(text)

### Unit tests below ###
def check(candidate):
    assert candidate('99') == True

def test_check():
    check(f)