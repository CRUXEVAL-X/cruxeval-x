def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    return ''.join(x for x in text if x != ')')

### Unit tests below ###
def check(candidate):
    assert candidate(('(((((((((((d))))))))).))))(((((')) == '(((((((((((d.((((('

def test_check():
    check(f)