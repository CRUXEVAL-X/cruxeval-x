def f(number: str) -> bool:
    """"""
    ### Canonical solution below ###
    return True if number.isdecimal() else False

### Unit tests below ###
def check(candidate):
    assert candidate('dummy33;d') == False

def test_check():
    check(f)