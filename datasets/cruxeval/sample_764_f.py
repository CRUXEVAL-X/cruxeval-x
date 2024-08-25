def f(text: str, old: str, new: str) -> str:
    """"""
    ### Canonical solution below ###
    text2 = text.replace(old, new)
    old2 = old[::-1]
    while old2 in text2:
        text2 = text2.replace(old2, new)
    return text2

### Unit tests below ###
def check(candidate):
    assert candidate("some test string", "some", "any") == 'any test string'

def test_check():
    check(f)