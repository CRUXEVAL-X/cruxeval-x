def f(a: str) -> str:
    """"""
    ### Canonical solution below ###
    return ' '.join(a.split())

### Unit tests below ###
def check(candidate):
    assert candidate(' h e l l o   w o r l d! ') == 'h e l l o w o r l d!'

def test_check():
    check(f)