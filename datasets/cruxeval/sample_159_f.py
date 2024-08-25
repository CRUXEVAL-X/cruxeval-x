def f(st: str) -> str:
    """"""
    ### Canonical solution below ###
    swapped = ''
    for ch in reversed(st):
        swapped += ch.swapcase()
    return swapped

### Unit tests below ###
def check(candidate):
    assert candidate('RTiGM') == 'mgItr'

def test_check():
    check(f)