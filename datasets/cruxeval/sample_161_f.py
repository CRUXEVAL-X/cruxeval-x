def f(text: str, value: str) -> str:
    """"""
    ### Canonical solution below ###
    left, _, right = text.partition(value)
    return right + left

### Unit tests below ###
def check(candidate):
    assert candidate('difkj rinpx', 'k') == 'j rinpxdif'

def test_check():
    check(f)