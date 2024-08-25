def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    a = []
    for i in range(len(text)):
        if not text[i].isdecimal():
            a.append(text[i])
    return ''.join(a)

### Unit tests below ###
def check(candidate):
    assert candidate("seiq7229 d27") == 'seiq d'

def test_check():
    check(f)