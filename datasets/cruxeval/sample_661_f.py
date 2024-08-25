def f(letters: str, maxsplit: int) -> str:
    """"""
    ### Canonical solution below ###
    return ''.join(letters.split()[-maxsplit:])

### Unit tests below ###
def check(candidate):
    assert candidate('elrts,SS ee', 6) == 'elrts,SSee'

def test_check():
    check(f)