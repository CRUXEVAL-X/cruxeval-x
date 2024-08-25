def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    s = text.lower()
    for i in range(len(s)):
        if s[i] == 'x':
            return 'no'
    return text.isupper()

### Unit tests below ###
def check(candidate):
    assert candidate('dEXE') == 'no'

def test_check():
    check(f)