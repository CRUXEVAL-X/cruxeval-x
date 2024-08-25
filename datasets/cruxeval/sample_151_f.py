def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    for c in text:
        if c.isdigit():
            if c == '0':
                c = '.'
            else:
                c = '0' if c != '1' else '.'
    return ''.join(list(text)).replace('.', '0')

### Unit tests below ###
def check(candidate):
    assert candidate('697 this is the ultimate 7 address to attack') == '697 this is the ultimate 7 address to attack'

def test_check():
    check(f)