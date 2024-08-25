def f(text: str, prefix: str) -> str:
    """"""
    ### Canonical solution below ###
    return text[len(prefix):]

### Unit tests below ###
def check(candidate):
    assert candidate('123x John z', 'z') == '23x John z'

def test_check():
    check(f)