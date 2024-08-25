def f(text: str, pref: str) -> str:
    """"""
    ### Canonical solution below ###
    length = len(pref)
    if pref == text[:length]:
        return text[length:]
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('kumwwfv', 'k') == 'umwwfv'

def test_check():
    check(f)