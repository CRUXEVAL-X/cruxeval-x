def f(s: str) -> int:
    """"""
    ### Canonical solution below ###
    count = 0
    for c in s:
        if s.rindex(c) != s.index(c):
            count+=1
    return count

### Unit tests below ###
def check(candidate):
    assert candidate("abca dea ead") == 10

def test_check():
    check(f)