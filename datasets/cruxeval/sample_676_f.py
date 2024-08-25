def f(text: str, tab_size: int) -> str:
    """"""
    ### Canonical solution below ###
    return text.replace('\t', ' '*tab_size)

### Unit tests below ###
def check(candidate):
    assert candidate('a', 100) == 'a'

def test_check():
    check(f)