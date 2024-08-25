def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    rtext = list(text)
    for i in range(1, len(rtext) - 1):
        rtext.insert(i + 1, '|')
    return ''.join(rtext)

### Unit tests below ###
def check(candidate):
    assert candidate('pxcznyf') == 'px|||||cznyf'

def test_check():
    check(f)