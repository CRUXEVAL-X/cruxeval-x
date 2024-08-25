def f(num: int) -> str:
    """"""
    ### Canonical solution below ###
    if 0 < num < 1000 and num != 6174:
        return 'Half Life'
    return 'Not found'

### Unit tests below ###
def check(candidate):
    assert candidate(6173) == 'Not found'

def test_check():
    check(f)