def f(ip: str, n: int) -> str:
    """"""
    ### Canonical solution below ###
    i = 0
    out = ''
    for c in ip:
        if i == n:
            out += '\n'
            i = 0
        i += 1
        out += c
    return out

### Unit tests below ###
def check(candidate):
    assert candidate("dskjs hjcdjnxhjicnn", 4) == 'dskj\ns hj\ncdjn\nxhji\ncnn'

def test_check():
    check(f)