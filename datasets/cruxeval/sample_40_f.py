def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.ljust(len(text) + 1, "#")

### Unit tests below ###
def check(candidate):
    assert candidate("the cow goes moo") == 'the cow goes moo#'

def test_check():
    check(f)