def f(code: str) -> str:
    """"""
    ### Canonical solution below ###
    return "{}: {}".format(code, code.encode())

### Unit tests below ###
def check(candidate):
    assert candidate('148') == "148: b'148'"

def test_check():
    check(f)