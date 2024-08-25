def f(name: str) -> str:
    """"""
    ### Canonical solution below ###
    if name.islower():
        name = name.upper()
    else:
        name = name.lower()
    return name

### Unit tests below ###
def check(candidate):
    assert candidate('Pinneaple') == 'pinneaple'

def test_check():
    check(f)