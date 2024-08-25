def f(challenge: str) -> str:
    """"""
    ### Canonical solution below ###
    return challenge.casefold().replace('l', ',')

### Unit tests below ###
def check(candidate):
    assert candidate('czywZ') == 'czywz'

def test_check():
    check(f)