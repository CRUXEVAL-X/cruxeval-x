def f(text: str, n: int) -> str:
    """"""
    ### Canonical solution below ###
    if len(text) <= 2:
        return text
    leading_chars = text[0] * (n - len(text) + 1)
    return leading_chars + text[1:-1] + text[-1]

### Unit tests below ###
def check(candidate):
    assert candidate('g', 15) == 'g'

def test_check():
    check(f)