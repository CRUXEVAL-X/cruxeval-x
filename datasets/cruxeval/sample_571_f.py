def f(input_string: str, spaces: int) -> str:
    """"""
    ### Canonical solution below ###
    return input_string.expandtabs(spaces)

### Unit tests below ###
def check(candidate):
    assert candidate(r'a\tb', 4) == 'a\\tb'

def test_check():
    check(f)