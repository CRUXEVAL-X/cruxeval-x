def f(s: str, n: int) -> str:
    """"""
    ### Canonical solution below ###
    if len(s) < n:
        return s
    else:
        return s.removeprefix(s[:n])

### Unit tests below ###
def check(candidate):
    assert candidate("try.", 5) == 'try.'

def test_check():
    check(f)