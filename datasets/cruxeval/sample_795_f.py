def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.title().replace('Io', 'io')

### Unit tests below ###
def check(candidate):
    assert candidate('Fu,ux zfujijabji pfu.') == 'Fu,Ux Zfujijabji Pfu.'

def test_check():
    check(f)