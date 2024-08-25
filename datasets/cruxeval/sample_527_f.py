def f(text: str, value: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.ljust(len(value), "?")

### Unit tests below ###
def check(candidate):
    assert candidate("!?", "") == '!?'

def test_check():
    check(f)