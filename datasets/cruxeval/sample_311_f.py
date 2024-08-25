def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    text = text.replace('#', '1').replace('$', '5')
    return 'yes' if text.isnumeric() else 'no'

### Unit tests below ###
def check(candidate):
    assert candidate('A') == 'no'

def test_check():
    check(f)