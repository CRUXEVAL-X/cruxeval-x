def f(x: str) -> str:
    """"""
    ### Canonical solution below ###
    if x.islower():
        return x
    else:
        return x[::-1]

### Unit tests below ###
def check(candidate):
    assert candidate('ykdfhp') == 'ykdfhp'

def test_check():
    check(f)