def f(t: str) -> str:
    """"""
    ### Canonical solution below ###
    a, sep, b = t.rpartition('-')
    if len(b) == len(a):
        return 'imbalanced'
    return a + b.replace(sep, '')

### Unit tests below ###
def check(candidate):
    assert candidate("fubarbaz") == 'fubarbaz'

def test_check():
    check(f)