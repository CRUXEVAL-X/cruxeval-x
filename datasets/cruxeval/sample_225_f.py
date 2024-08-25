def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    if text.islower():
        return True
    return False

### Unit tests below ###
def check(candidate):
    assert candidate("54882") == False

def test_check():
    check(f)