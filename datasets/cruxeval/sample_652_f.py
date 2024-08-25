def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    if not string or not string[0].isnumeric:
        return 'INVALID'
    cur = 0
    for i in range(len(string)):
        cur = cur * 10 + int(string[i])
    return str(cur)

### Unit tests below ###
def check(candidate):
    assert candidate('3') == '3'

def test_check():
    check(f)