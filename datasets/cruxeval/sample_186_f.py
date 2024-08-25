def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    return ' '.join(map(str.lstrip, text.split()))

### Unit tests below ###
def check(candidate):
    assert candidate('pvtso') == 'pvtso'

def test_check():
    check(f)