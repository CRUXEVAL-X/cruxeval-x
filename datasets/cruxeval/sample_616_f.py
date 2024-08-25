def f(body: str) -> str:
    """"""
    ### Canonical solution below ###
    ls = list(body)
    dist = 0
    for i in range(0, len(ls) - 1):
        if ls[i - 2 if i - 2 >= 0 else 0] == '\t':
            dist += (1 + ls[i - 1].count('\t')) * 3
        ls[i] = '[' + ls[i] + ']'
    return ''.join(ls).expandtabs(4 + dist)

### Unit tests below ###
def check(candidate):
    assert candidate('\n\ny\n') == '[\n][\n][y]\n'

def test_check():
    check(f)