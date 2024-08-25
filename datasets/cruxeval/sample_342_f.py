def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    return text.count('-') == len(text)

### Unit tests below ###
def check(candidate):
    assert candidate("---123-4") == False

def test_check():
    check(f)