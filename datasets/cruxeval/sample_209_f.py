def f(prefix: str, s: str) -> str:
    """"""
    ### Canonical solution below ###
    return str.removeprefix(prefix, s)

### Unit tests below ###
def check(candidate):
    assert candidate('hymi', 'hymifulhxhzpnyihyf') == 'hymi'

def test_check():
    check(f)