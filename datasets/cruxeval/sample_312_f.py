def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    if s.isalnum():
        return "True"
    return "False"

### Unit tests below ###
def check(candidate):
    assert candidate('777') == 'True'

def test_check():
    check(f)