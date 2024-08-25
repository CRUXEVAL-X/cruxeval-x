def f(text: str, suffix: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('zejrohaj', 'owc') == 'zejrohaj'

def test_check():
    check(f)