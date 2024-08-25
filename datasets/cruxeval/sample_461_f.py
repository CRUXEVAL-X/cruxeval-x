def f(text: str, search: str) -> bool:
    """"""
    ### Canonical solution below ###
    return search.startswith(text) or False

### Unit tests below ###
def check(candidate):
    assert candidate('123', '123eenhas0') == True

def test_check():
    check(f)