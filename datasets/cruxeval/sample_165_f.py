def f(text: str, lower: int, upper: int) -> bool:
    """"""
    ### Canonical solution below ###
    return text[lower:upper].isascii()

### Unit tests below ###
def check(candidate):
    assert candidate('=xtanp|sugv?z', 3, 6) == True

def test_check():
    check(f)