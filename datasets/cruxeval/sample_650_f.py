def f(string: str, substring: str) -> str:
    """"""
    ### Canonical solution below ###
    while string.startswith(substring):
        string = string[len(substring):len(string)]
    return string

### Unit tests below ###
def check(candidate):
    assert candidate('', 'A') == ''

def test_check():
    check(f)