def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    if s.isalpha():
        return "yes"
    if s == "":
        return "str is empty"
    return "no"

### Unit tests below ###
def check(candidate):
    assert candidate('Boolean') == 'yes'

def test_check():
    check(f)