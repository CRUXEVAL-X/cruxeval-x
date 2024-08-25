def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    while string:
        if string[-1].isalpha():
            return string
        string = string[:-1]
    return string

### Unit tests below ###
def check(candidate):
    assert candidate('--4/0-209') == ''

def test_check():
    check(f)