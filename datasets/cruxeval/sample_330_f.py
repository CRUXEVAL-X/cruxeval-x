def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    ans = []
    for char in text:
        if char.isdigit():
            ans.append(char)
        else:
            ans.append(' ')
    return ''.join(ans)

### Unit tests below ###
def check(candidate):
    assert candidate('m4n2o') == ' 4 2 '

def test_check():
    check(f)