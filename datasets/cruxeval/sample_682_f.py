def f(text: str, length: int, index: int) -> str:
    """"""
    ### Canonical solution below ###
    ls = text.rsplit(None, index)
    return '_'.join([l[:length] for l in ls])

### Unit tests below ###
def check(candidate):
    assert candidate('hypernimovichyp', 2, 2) == 'hy'

def test_check():
    check(f)