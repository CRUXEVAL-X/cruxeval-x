def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    return text.find(",")

### Unit tests below ###
def check(candidate):
    assert candidate("There are, no, commas, in this text") == 9

def test_check():
    check(f)