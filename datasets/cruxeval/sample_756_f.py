def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.isalnum() and all(i.isdigit() for i in text):
        return 'integer'
    return 'string'

### Unit tests below ###
def check(candidate):
    assert candidate('') == 'string'

def test_check():
    check(f)