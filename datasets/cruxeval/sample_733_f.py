def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    length = len(text) // 2
    left_half = text[:length]
    right_half = text[length:][::-1]
    return left_half + right_half

### Unit tests below ###
def check(candidate):
    assert candidate('n') == 'n'

def test_check():
    check(f)