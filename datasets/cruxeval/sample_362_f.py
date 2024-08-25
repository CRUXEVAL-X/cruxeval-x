def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    for i in range(len(text)-1):
        if text[i:].islower():
            return text[i + 1:]
    return ''

### Unit tests below ###
def check(candidate):
    assert candidate('wrazugizoernmgzu') == 'razugizoernmgzu'

def test_check():
    check(f)