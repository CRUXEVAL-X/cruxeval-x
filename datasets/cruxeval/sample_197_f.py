def f(temp: int, timeLimit: int) -> str:
    """"""
    ### Canonical solution below ###
    s = timeLimit // temp
    e = timeLimit % temp
    return [f'{e} oC', f'{s} {e}'][s > 1]

### Unit tests below ###
def check(candidate):
    assert candidate(1, 1234567890) == '1234567890 0'

def test_check():
    check(f)