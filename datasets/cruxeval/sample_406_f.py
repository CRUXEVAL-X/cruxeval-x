def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    ls = list(text)
    ls[0], ls[-1] = ls[-1].upper(), ls[0].upper()
    return ''.join(ls).istitle()

### Unit tests below ###
def check(candidate):
    assert candidate('Josh') == False

def test_check():
    check(f)