def f(n: int) -> bool:
    """"""
    ### Canonical solution below ###
    for n in str(n):
        if n not in "012" and n not in list(range(5, 10)):
            return False
    return True

### Unit tests below ###
def check(candidate):
    assert candidate(1341240312) == False

def test_check():
    check(f)