def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    return ''.join(list(text)).isspace()

### Unit tests below ###
def check(candidate):
    assert candidate(' \t  \u3000') == True

def test_check():
    check(f)