def f(string: str, sep: str) -> str:
    """"""
    ### Canonical solution below ###
    cnt = string.count(sep)
    return((string+sep) * cnt)[::-1]

### Unit tests below ###
def check(candidate):
    assert candidate('caabcfcabfc', 'ab') == 'bacfbacfcbaacbacfbacfcbaac'

def test_check():
    check(f)