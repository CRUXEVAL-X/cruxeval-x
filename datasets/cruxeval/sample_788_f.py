def f(text: str, suffix: str) -> str:
    """"""
    ### Canonical solution below ###
    if suffix.startswith("/"):
        return text + suffix[1:]
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('hello.txt', '/') == 'hello.txt'

def test_check():
    check(f)