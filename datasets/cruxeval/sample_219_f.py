def f(s1: str, s2: str) -> bool:
    """"""
    ### Canonical solution below ###
    for k in range(0, len(s2)+len(s1)):
        s1 += s1[0]
        if s1.find(s2) >= 0:
            return True
    return False

### Unit tests below ###
def check(candidate):
    assert candidate("Hello", ")") == False

def test_check():
    check(f)