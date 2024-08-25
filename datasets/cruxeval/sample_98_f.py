def f(s: str) -> int:
    """"""
    ### Canonical solution below ###
    return sum([s.istitle() for s in s.split()])

### Unit tests below ###
def check(candidate):
    assert candidate('SOME OF THIS Is uknowN!') == 1

def test_check():
    check(f)