def f(num: int) -> int:
    """"""
    ### Canonical solution below ###
    initial = [1]
    total = initial
    for _ in range(num):
        total = [1] + [x+y for x, y in zip(total, total[1:])]
        initial.append(total[-1])
    return sum(initial)

### Unit tests below ###
def check(candidate):
    assert candidate(3) == 4

def test_check():
    check(f)