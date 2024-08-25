def f(s: str) -> int:
    """"""
    ### Canonical solution below ###
    b = ''
    c = ''
    for i in s:
        c = c + i
        if s.rfind(c) > -1:
            return s.rfind(c)
    return 0

### Unit tests below ###
def check(candidate):
    assert candidate('papeluchis') == 2

def test_check():
    check(f)