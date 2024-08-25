def f(cat: str) -> int:
    """"""
    ### Canonical solution below ###
    digits = 0
    for char in cat:
        if char.isdigit():
            digits += 1
    return digits

### Unit tests below ###
def check(candidate):
    assert candidate('C24Bxxx982ab') == 5

def test_check():
    check(f)