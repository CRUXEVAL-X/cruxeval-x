def f(a: str, b: str, n: int) -> str:
    """"""
    ### Canonical solution below ###
    result = m = b
    for _ in range(n):
        if m:
            a, m = a.replace(m, '', 1), None
            result = m = b
    return result.join(a.split(b))

### Unit tests below ###
def check(candidate):
    assert candidate('unrndqafi', 'c', 2) == 'unrndqafi'

def test_check():
    check(f)