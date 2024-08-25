def f(text: str, count: int) -> str:
    """"""
    ### Canonical solution below ###
    for i in range(count):
        text = text[::-1]
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('439m2670hlsw', 3) == 'wslh0762m934'

def test_check():
    check(f)