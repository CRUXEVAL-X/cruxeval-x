def f(start: int, end: int, interval: int) -> int:
    """"""
    ### Canonical solution below ###
    steps = list(range(start, end + 1, interval))
    if 1 in steps:
        steps[-1] = end + 1
    return len(steps)

### Unit tests below ###
def check(candidate):
    assert candidate(3, 10, 1) == 8

def test_check():
    check(f)