def f(n: str) -> int:
    """"""
    ### Canonical solution below ###
    for i in str(n):
        if not i.isdigit():
            n = -1
            break
    return n

### Unit tests below ###
def check(candidate):
    assert candidate("6 ** 2") == -1

def test_check():
    check(f)