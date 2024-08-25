def f(n: int) -> str:
    """"""
    ### Canonical solution below ###
    t = 0
    b = ''
    digits = list(map(int, str(n)))
    for d in digits:
        if d == 0: t += 1
        else: break
    for _ in range(t):
        b += str(1) + '0' + str(4)
    b += str(n)
    return b

### Unit tests below ###
def check(candidate):
    assert candidate(372359) == '372359'

def test_check():
    check(f)