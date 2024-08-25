def f(char: str) -> str:
    """"""
    ### Canonical solution below ###
    if char not in 'aeiouAEIOU':
        return None
    if char in 'AEIOU':
        return char.lower()
    return char.upper()

### Unit tests below ###
def check(candidate):
    assert candidate('o') == 'O'

def test_check():
    check(f)