def f(letters: str) -> int:
    """"""
    ### Canonical solution below ###
    count = 0
    for l in letters:
        if l.isdigit():
            count += 1
    return count

### Unit tests below ###
def check(candidate):
    assert candidate("dp ef1 gh2") == 2

def test_check():
    check(f)