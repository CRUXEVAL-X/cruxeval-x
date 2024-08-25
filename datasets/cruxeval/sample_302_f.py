def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    return string.replace('needles', 'haystacks')

### Unit tests below ###
def check(candidate):
    assert candidate('wdeejjjzsjsjjsxjjneddaddddddefsfd') == 'wdeejjjzsjsjjsxjjneddaddddddefsfd'

def test_check():
    check(f)