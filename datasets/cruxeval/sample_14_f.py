def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    arr = list(s.strip())
    arr.reverse()
    return ''.join(arr)

### Unit tests below ###
def check(candidate):
    assert candidate('   OOP   ') == 'POO'

def test_check():
    check(f)