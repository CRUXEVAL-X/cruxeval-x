def f(x: str) -> int:
    """"""
    ### Canonical solution below ###
    a = 0
    for i in x.split(' '):
        a += len(i.zfill(len(i)*2))
    return a

### Unit tests below ###
def check(candidate):
    assert candidate('999893767522480') == 30

def test_check():
    check(f)