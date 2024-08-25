def f(text: str, prefix: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.startswith(prefix):
        return text.removeprefix(prefix)
    if prefix in text:
        return text.replace(prefix, '').strip()
    return text.upper()

### Unit tests below ###
def check(candidate):
    assert candidate('abixaaaily', 'al') == 'ABIXAAAILY'

def test_check():
    check(f)