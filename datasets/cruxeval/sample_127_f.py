def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    s = text.splitlines()
    return len(s)

### Unit tests below ###
def check(candidate):
    assert candidate("145\n\n12fjkjg") == 3

def test_check():
    check(f)