def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    i = 0
    while i < len(text) and text[i].isspace():
        i+=1
    if i == len(text):
        return 'space'
    return 'no'

### Unit tests below ###
def check(candidate):
    assert candidate("     ") == 'space'

def test_check():
    check(f)