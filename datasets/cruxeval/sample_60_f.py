def f(doc: str) -> str:
    """"""
    ### Canonical solution below ###
    for x in doc:
        if x.isalpha():
            return x.capitalize()
    return '-'

### Unit tests below ###
def check(candidate):
    assert candidate('raruwa') == 'R'

def test_check():
    check(f)