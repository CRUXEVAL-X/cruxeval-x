def f(text: str, value: str) -> str:
    """"""
    ### Canonical solution below ###
    if not value in text:
        return ''
    return text.rpartition(value)[0]

### Unit tests below ###
def check(candidate):
    assert candidate('mmfbifen', 'i') == 'mmfb'

def test_check():
    check(f)