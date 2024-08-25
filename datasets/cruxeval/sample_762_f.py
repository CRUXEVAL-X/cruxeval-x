def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    text = text.lower()
    capitalize = text.capitalize()
    return text[:1] + capitalize[1:]

### Unit tests below ###
def check(candidate):
    assert candidate('this And cPanel') == 'this and cpanel'

def test_check():
    check(f)