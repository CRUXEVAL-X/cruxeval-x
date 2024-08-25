def f(s: str, o: str) -> str:
    """"""
    ### Canonical solution below ###
    if s.startswith(o):
        return s
    return o + f(s, o[-2::-1])

### Unit tests below ###
def check(candidate):
    assert candidate('abba', 'bab') == 'bababba'

def test_check():
    check(f)