def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    l = text.rpartition('0')
    if l[2] == '':
        return '-1:-1'
    return f'{len(l[0])}:{l[2].find("0") + 1}'

### Unit tests below ###
def check(candidate):
    assert candidate('qq0tt') == '2:0'

def test_check():
    check(f)