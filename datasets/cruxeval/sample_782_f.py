def f(input: str) -> bool:
    """"""
    ### Canonical solution below ###
    for char in input:
        if char.isupper():
            return False
    return True

### Unit tests below ###
def check(candidate):
    assert candidate("a j c n x X k") == False

def test_check():
    check(f)