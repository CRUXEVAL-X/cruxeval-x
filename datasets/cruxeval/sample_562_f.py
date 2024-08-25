def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    return text.upper() == str(text)

### Unit tests below ###
def check(candidate):
    assert candidate('VTBAEPJSLGAHINS') == True

def test_check():
    check(f)