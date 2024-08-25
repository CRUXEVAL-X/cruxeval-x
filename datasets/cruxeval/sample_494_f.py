def f(num: str, l: int) -> str:
    """"""
    ### Canonical solution below ###
    t = ""
    while l > len(num):
        t += '0'
        l -= 1
    return t + num

### Unit tests below ###
def check(candidate):
    assert candidate("1", 3) == '001'

def test_check():
    check(f)