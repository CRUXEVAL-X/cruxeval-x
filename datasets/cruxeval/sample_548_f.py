def f(text: str, suffix: str) -> str:
    """"""
    ### Canonical solution below ###
    if suffix and text and text.endswith(suffix):
        return text.removesuffix(suffix)
    else:
        return text

### Unit tests below ###
def check(candidate):
    assert candidate('spider', 'ed') == 'spider'

def test_check():
    check(f)