def f(s1: str, s2: str) -> int:
    """"""
    ### Canonical solution below ###
    position = 1
    count = 0
    while position > 0:
        position = s1.find(s2, position)
        count += 1
        position += 1
    return count

### Unit tests below ###
def check(candidate):
    assert candidate('xinyyexyxx', 'xx') == 2

def test_check():
    check(f)