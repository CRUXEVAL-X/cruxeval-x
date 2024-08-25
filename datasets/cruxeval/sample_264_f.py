def f(test_str: str) -> str:
    """"""
    ### Canonical solution below ###
    s = test_str.replace('a', 'A')
    return s.replace('e', 'A')

### Unit tests below ###
def check(candidate):
    assert candidate("papera") == 'pApArA'

def test_check():
    check(f)