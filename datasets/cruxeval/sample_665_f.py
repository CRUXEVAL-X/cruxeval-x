def f(chars: str) -> str:
    """"""
    ### Canonical solution below ###
    s = ""
    for ch in chars:
        if chars.count(ch) % 2 == 0:
            s += ch.upper()
        else:
            s += ch
    return s

### Unit tests below ###
def check(candidate):
    assert candidate("acbced") == 'aCbCed'

def test_check():
    check(f)