def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    a = ['']
    b = ''
    for i in text:
        if not i.isspace():
            a.append(b)
            b = ''
        else:
            b += i
    return len(a)

### Unit tests below ###
def check(candidate):
    assert candidate("       ") == 1

def test_check():
    check(f)