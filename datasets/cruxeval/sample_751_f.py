def f(text: str, char: str, min_count: int) -> str:
    """"""
    ### Canonical solution below ###
    count = text.count(char)
    if count < min_count:
        return text.swapcase()
    return text

### Unit tests below ###
def check(candidate):
    assert candidate("wwwwhhhtttpp", 'w', 3) == 'wwwwhhhtttpp'

def test_check():
    check(f)