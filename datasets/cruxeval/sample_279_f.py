def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    ans = ''
    while text != '':
        x, sep, text = text.partition('(')
        ans = x + sep.replace('(', '|') + ans
        ans = ans + text[0] + ans
        text = text[1:]
    return ans

### Unit tests below ###
def check(candidate):
    assert candidate("") == ''

def test_check():
    check(f)