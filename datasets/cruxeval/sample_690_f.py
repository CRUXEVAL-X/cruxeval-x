def f(n: str) -> str:
    """"""
    ### Canonical solution below ###
    if str(n).find('.') != -1:
        return str(int(n)+2.5)
    return str(n)

### Unit tests below ###
def check(candidate):
    assert candidate('800') == '800'

def test_check():
    check(f)