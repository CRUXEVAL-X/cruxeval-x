def f(value: str) -> str:
    """"""
    ### Canonical solution below ###
    ls = list(value)
    ls.append('NHIB')
    return ''.join(ls)

### Unit tests below ###
def check(candidate):
    assert candidate('ruam') == 'ruamNHIB'

def test_check():
    check(f)