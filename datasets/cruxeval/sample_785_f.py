def f(n: int) -> str:
    """"""
    ### Canonical solution below ###
    streak = ''
    for c in str(n):
        streak += c.ljust(int(c) * 2)
    return streak

### Unit tests below ###
def check(candidate):
    assert candidate(1) == '1 '

def test_check():
    check(f)