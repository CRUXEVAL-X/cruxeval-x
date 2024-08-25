def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    text = text.split(' ')
    for t in text:
        if not t.isnumeric():
            return 'no'
    return 'yes'

### Unit tests below ###
def check(candidate):
    assert candidate('03625163633 d') == 'no'

def test_check():
    check(f)