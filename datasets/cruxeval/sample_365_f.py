def f(n: str, s: str) -> str:
    """"""
    ### Canonical solution below ###
    if s.startswith(n):
        pre, _ = s.split(n, 1)
        return pre + n + s[len(n):]
    return s

### Unit tests below ###
def check(candidate):
    assert candidate('xqc', 'mRcwVqXsRDRb') == 'mRcwVqXsRDRb'

def test_check():
    check(f)