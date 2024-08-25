def f(string: str, prefix: str) -> str:
    """"""
    ### Canonical solution below ###
    if string.startswith(prefix):
        return string.removeprefix(prefix)
    return string

### Unit tests below ###
def check(candidate):
    assert candidate("Vipra", "via") == 'Vipra'

def test_check():
    check(f)