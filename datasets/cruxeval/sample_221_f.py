def f(text: str, delim: str) -> str:
    """"""
    ### Canonical solution below ###
    first, second = text.split(delim)
    return second + delim + first

### Unit tests below ###
def check(candidate):
    assert candidate('bpxa24fc5.', '.') == '.bpxa24fc5'

def test_check():
    check(f)