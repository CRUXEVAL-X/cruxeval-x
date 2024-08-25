def f(text: str, strip_chars: str) -> str:
    """"""
    ### Canonical solution below ###
    return text[::-1].strip(strip_chars)[::-1]

### Unit tests below ###
def check(candidate):
    assert candidate('tcmfsmj', 'cfj') == 'tcmfsm'

def test_check():
    check(f)