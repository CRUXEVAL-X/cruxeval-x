def f(n: str, m: str, text: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.strip() == '':
        return text
    head, mid, tail = text[0], text[1:-1], text[-1]
    joined = head.replace(n, m) + mid.replace(n, m) + tail.replace(n, m)
    return joined

### Unit tests below ###
def check(candidate):
    assert candidate("x", "$", "2xz&5H3*1a@#a*1hris") == '2$z&5H3*1a@#a*1hris'

def test_check():
    check(f)