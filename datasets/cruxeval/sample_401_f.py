def f(text: str, suffix: str) -> str:
    """"""
    ### Canonical solution below ###
    if suffix and text.endswith(suffix):
        return text[:- len(suffix)]
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('mathematics', 'example') == 'mathematics'

def test_check():
    check(f)