def f(text: str, limit: int, char: str) -> str:
    """"""
    ### Canonical solution below ###
    if limit < len(text):
        return text[0:limit]
    return text.ljust(limit, char)

### Unit tests below ###
def check(candidate):
    assert candidate('tqzym', 5, 'c') == 'tqzym'

def test_check():
    check(f)