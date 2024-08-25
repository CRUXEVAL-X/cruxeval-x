def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    tmp = string.lower()
    for char in string.lower():
        if char in tmp:
            tmp = tmp.replace(char, '', 1)
    return tmp

### Unit tests below ###
def check(candidate):
    assert candidate('[ Hello ]+ Hello, World!!_ Hi') == ''

def test_check():
    check(f)