def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    return len(text.splitlines())

### Unit tests below ###
def check(candidate):
    assert candidate('ncdsdfdaaa0a1cdscsk*XFd') == 1

def test_check():
    check(f)