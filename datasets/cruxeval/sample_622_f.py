def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    left, sep, right = s.rpartition('.')
    new = sep.join([right, left])
    _, sep, _ = new.rpartition('.')
    return new.replace(sep, ', ')

### Unit tests below ###
def check(candidate):
    assert candidate('galgu') == ', g, a, l, g, u, '

def test_check():
    check(f)