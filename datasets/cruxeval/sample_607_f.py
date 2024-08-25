def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    for i in ['.', '!', '?']:
        if text.endswith(i):
            return True
    return False

### Unit tests below ###
def check(candidate):
    assert candidate('. C.') == True

def test_check():
    check(f)