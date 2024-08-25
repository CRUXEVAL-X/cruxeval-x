def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    count = string.count(':')
    return string.replace(':', '', count - 1)

### Unit tests below ###
def check(candidate):
    assert candidate('1::1') == '1:1'

def test_check():
    check(f)