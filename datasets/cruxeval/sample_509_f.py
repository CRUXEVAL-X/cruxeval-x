def f(value: int, width: int) -> str:
    """"""
    ### Canonical solution below ###
    if value >= 0:
        return str(value).zfill(width)

    if value < 0:
        return '-' + str(-value).zfill(width)
    return ''

### Unit tests below ###
def check(candidate):
    assert candidate(5, 1) == '5'

def test_check():
    check(f)