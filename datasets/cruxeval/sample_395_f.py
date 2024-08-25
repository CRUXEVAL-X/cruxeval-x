def f(s: str) -> int:
    """"""
    ### Canonical solution below ###
    for i in range(len(s)):
        if s[i].isdecimal():
            return i + (s[i] == '0')
        elif s[i] == '0':
            return -1
    return -1

### Unit tests below ###
def check(candidate):
    assert candidate("11") == 0

def test_check():
    check(f)