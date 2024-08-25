def f(txt: str) -> str:
    """"""
    ### Canonical solution below ###
    return txt.format(*('0'*20,))

### Unit tests below ###
def check(candidate):
    assert candidate("5123807309875480094949830") == '5123807309875480094949830'

def test_check():
    check(f)