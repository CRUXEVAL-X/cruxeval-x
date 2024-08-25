def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    return not any([c.isupper() for c in text])

### Unit tests below ###
def check(candidate):
    assert candidate('lunabotics') == True

def test_check():
    check(f)