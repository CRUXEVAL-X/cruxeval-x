def f(text: str, n: int) -> str:
    """"""
    ### Canonical solution below ###
    if n < 0 or len(text) <= n:
        return text
    result = text[0 : n]
    i = len(result) - 1
    while i >= 0:
        if result[i] != text[i]:
            break
        i -= 1
    return text[0 : i + 1]

### Unit tests below ###
def check(candidate):
    assert candidate('bR', -1) == 'bR'

def test_check():
    check(f)