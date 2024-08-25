def f(text: str, chars: str) -> str:
    """"""
    ### Canonical solution below ###
    result = list(text)
    while chars in result[-3::-2]:
        result.remove(result[-3])
        result.remove(result[-3])
    return ''.join(result).strip('.')

### Unit tests below ###
def check(candidate):
    assert candidate('ellod!p.nkyp.exa.bi.y.hain', '.n.in.ha.y') == 'ellod!p.nkyp.exa.bi.y.hain'

def test_check():
    check(f)