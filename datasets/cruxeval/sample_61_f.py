def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    texts = text.split()
    if texts:
        xtexts = [t for t in texts if t.isascii() and t not in ('nada', '0')]
        return max(xtexts, key=len) if xtexts else 'nada'
    return 'nada'

### Unit tests below ###
def check(candidate):
    assert candidate("") == 'nada'

def test_check():
    check(f)