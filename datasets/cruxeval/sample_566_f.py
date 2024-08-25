def f(string: str, code: str) -> str:
    """"""
    ### Canonical solution below ###
    t = ''
    try:
        t = string.encode(code)
        if t.endswith(b'\n'):
            t = t[:-1]
        t = t.decode('UTF-8')
        return t
    except:
        return t

### Unit tests below ###
def check(candidate):
    assert candidate("towaru", "UTF-8") == 'towaru'

def test_check():
    check(f)