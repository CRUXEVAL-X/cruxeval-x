def f(n: int, m: int, num: int) -> int:
    """"""
    ### Canonical solution below ###
    x_list = list(range(n, m+1))
    j = 0
    while True:
        j = (j + num) % len(x_list)
        if x_list[j] % 2 == 0:
            return x_list[j]

### Unit tests below ###
def check(candidate):
    assert candidate(46, 48, 21) == 46

def test_check():
    check(f)