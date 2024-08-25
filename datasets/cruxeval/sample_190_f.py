def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    short = ''
    for c in text:
        if(c.islower()):
            short += c
    return short

### Unit tests below ###
def check(candidate):
    assert candidate('980jio80jic kld094398IIl ') == 'jiojickldl'

def test_check():
    check(f)