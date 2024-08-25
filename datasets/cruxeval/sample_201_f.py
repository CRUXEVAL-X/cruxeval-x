def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    chars = []
    for c in text:
        if c.isdigit():
            chars.append(c)
    return ''.join(chars[::-1])

### Unit tests below ###
def check(candidate):
    assert candidate('--4yrw 251-//4 6p') == '641524'

def test_check():
    check(f)