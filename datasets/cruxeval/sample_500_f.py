def f(text: str, delim: str) -> str:
    """"""
    ### Canonical solution below ###
    return text[:text[::-1].find(delim)][::-1]

### Unit tests below ###
def check(candidate):
    assert candidate('dsj osq wi w', ' ') == 'd'

def test_check():
    check(f)