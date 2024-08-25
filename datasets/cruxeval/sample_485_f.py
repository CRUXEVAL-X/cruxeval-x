def f(tokens: str) -> str:
    """"""
    ### Canonical solution below ###
    tokens = tokens.split()
    if len(tokens) == 2:
        tokens = list(reversed(tokens))
    result = ' '.join([tokens[0].ljust(5), tokens[1].ljust(5)])
    return result

### Unit tests below ###
def check(candidate):
    assert candidate('gsd avdropj') == 'avdropj gsd  '

def test_check():
    check(f)