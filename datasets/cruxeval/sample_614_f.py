def f(text: str, substr: str, occ: int) -> int:
    """"""
    ### Canonical solution below ###
    n = 0
    while True:
        i = text.rfind(substr)
        if i == -1:
            break
        elif n == occ:
            return i
        else:
            n += 1
            text = text[:i]
    return -1

### Unit tests below ###
def check(candidate):
    assert candidate('zjegiymjc', 'j', 2) == -1

def test_check():
    check(f)