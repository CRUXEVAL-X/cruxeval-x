def f(text: str, suffix: str) -> bool:
    """"""
    ### Canonical solution below ###
    if suffix == '':
        suffix = None
    return text.endswith(suffix)

### Unit tests below ###
def check(candidate):
    assert candidate('uMeGndkGh', 'kG') == False

def test_check():
    check(f)