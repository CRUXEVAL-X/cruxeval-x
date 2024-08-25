def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    return text.split(':')[0].count('#')

### Unit tests below ###
def check(candidate):
    assert candidate("#! : #!") == 1

def test_check():
    check(f)