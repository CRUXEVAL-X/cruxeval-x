def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    return sum(1 for c in text if c.isdigit())

### Unit tests below ###
def check(candidate):
    assert candidate('so456') == 3

def test_check():
    check(f)