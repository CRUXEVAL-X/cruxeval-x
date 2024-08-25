def f(name: str) -> str:
    """"""
    ### Canonical solution below ###
    return '*'.join(name.split(' '))

### Unit tests below ###
def check(candidate):
    assert candidate('Fred Smith') == 'Fred*Smith'

def test_check():
    check(f)