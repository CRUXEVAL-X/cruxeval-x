def f(integer: int, n: int) -> str:
    """"""
    ### Canonical solution below ###
    i = 1
    text = str(integer)
    while (i+len(text) < n):
        i += len(text)
    return text.zfill(i+len(text))

### Unit tests below ###
def check(candidate):
    assert candidate(8999,2) == '08999'

def test_check():
    check(f)