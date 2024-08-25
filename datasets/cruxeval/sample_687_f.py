def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    t = list(text)
    t.pop(len(t) // 2)
    t.append(text.lower())
    return ':'.join([c for c in t])

### Unit tests below ###
def check(candidate):
    assert candidate('Rjug nzufE') == 'R:j:u:g: :z:u:f:E:rjug nzufe'

def test_check():
    check(f)