def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    try:
        return text.isalpha()
    except:
        return False

### Unit tests below ###
def check(candidate):
    assert candidate("x") == True

def test_check():
    check(f)