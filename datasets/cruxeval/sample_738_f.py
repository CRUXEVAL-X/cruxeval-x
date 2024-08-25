def f(text: str, characters: str) -> str:
    """"""
    ### Canonical solution below ###
    for i in range(len(characters)):
        text = text.rstrip(characters[i::len(characters)])
    return text

### Unit tests below ###
def check(candidate):
    assert candidate("r;r;r;r;r;r;r;r;r", "x.r") == 'r;r;r;r;r;r;r;r;'

def test_check():
    check(f)