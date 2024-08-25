def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    count = text.count(text[0])
    ls = list(text)
    for _ in range(count):
        ls.remove(ls[0])
    return ''.join(ls)

### Unit tests below ###
def check(candidate):
    assert candidate(';,,,?') == ',,,?'

def test_check():
    check(f)