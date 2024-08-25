def f(text: str, space_symbol: str, size: int) -> str:
    """"""
    ### Canonical solution below ###
    spaces = ''.join(space_symbol for i in range(size-len(text)))
    return text + spaces

### Unit tests below ###
def check(candidate):
    assert candidate('w', '))', 7) == 'w))))))))))))'

def test_check():
    check(f)