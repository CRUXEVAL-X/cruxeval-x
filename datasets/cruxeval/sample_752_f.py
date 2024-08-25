def f(s: str, amount: int) -> str:
    """"""
    ### Canonical solution below ###
    return (amount - len(s)) * 'z' + s

### Unit tests below ###
def check(candidate):
    assert candidate('abc', 8) == 'zzzzzabc'

def test_check():
    check(f)