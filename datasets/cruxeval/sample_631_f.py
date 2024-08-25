def f(text: str, num: int) -> str:
    """"""
    ### Canonical solution below ###
    req = num - len(text)
    text = text.center(num, '*')
    return text[:req // 2: -req // 2]

### Unit tests below ###
def check(candidate):
    assert candidate('a', 19) == '*'

def test_check():
    check(f)