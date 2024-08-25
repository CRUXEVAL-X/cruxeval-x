def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    text = list(text)
    for i in range(len(text)-1, -1, -1):
        if text[i].isspace():
            text[i] = '&nbsp;'
    return ''.join(text)

### Unit tests below ###
def check(candidate):
    assert candidate('   ') == '&nbsp;&nbsp;&nbsp;'

def test_check():
    check(f)