def f(name: str) -> str:
    """"""
    ### Canonical solution below ###
    return '| ' + ' '.join(name.split(' ')) + ' |'

### Unit tests below ###
def check(candidate):
    assert candidate('i am your father') == '| i am your father |'

def test_check():
    check(f)