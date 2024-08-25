def f(text: str, num_digits: int) -> str:
    """"""
    ### Canonical solution below ###
    width = max(1, num_digits)
    return text.zfill(width)

### Unit tests below ###
def check(candidate):
    assert candidate('19', 5) == '00019'

def test_check():
    check(f)