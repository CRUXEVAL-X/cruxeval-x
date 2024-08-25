def f(text: str, pref: str) -> bool:
    """"""
    ### Canonical solution below ###
    if isinstance(pref, list):
        return ', '.join(text.startswith(x) for x in pref)
    else:
        return text.startswith(pref)

### Unit tests below ###
def check(candidate):
    assert candidate('Hello World', 'W') == False

def test_check():
    check(f)