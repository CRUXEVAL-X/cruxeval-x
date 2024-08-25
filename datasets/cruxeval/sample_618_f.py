def f(match: str, fill: str, n: int) -> str:
    """"""
    ### Canonical solution below ###
    return fill[:n] + match

### Unit tests below ###
def check(candidate):
    assert candidate('9', '8', 2) == '89'

def test_check():
    check(f)