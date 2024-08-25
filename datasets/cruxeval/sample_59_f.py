def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    a = [char for char in s if char != ' ']
    b = a
    for c in reversed(a):
        if c == ' ':
            b.pop()
        else:
            break
    return ''.join(b)

### Unit tests below ###
def check(candidate):
    assert candidate('hi ') == 'hi'

def test_check():
    check(f)