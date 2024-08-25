def f(s: str, x: str) -> str:
    """"""
    ### Canonical solution below ###
    count = 0
    while s[:len(x)] == x and count < len(s)-len(x):
        s = s[len(x):]
        count += len(x)
    return s

### Unit tests below ###
def check(candidate):
    assert candidate('If you want to live a happy life! Daniel', 'Daniel') == 'If you want to live a happy life! Daniel'

def test_check():
    check(f)