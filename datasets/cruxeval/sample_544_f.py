def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    a = text.split('\n')
    b = []
    for i in range(len(a)):
        c = a[i].replace('\t', '    ')
        b.append(c)
    return '\n'.join(b)

### Unit tests below ###
def check(candidate):
    assert candidate("\t\t\ttab tab tabulates") == '            tab tab tabulates'

def test_check():
    check(f)