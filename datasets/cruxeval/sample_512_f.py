def f(s: str) -> bool:
    """"""
    ### Canonical solution below ###
    return len(s) == s.count('0') + s.count('1')

### Unit tests below ###
def check(candidate):
    assert candidate('102') == False

def test_check():
    check(f)