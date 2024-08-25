def f(s: str, amount: int) -> str:
    """"""
    ### Canonical solution below ###
    lines = s.splitlines()
    w = max(map(lambda l: l.rfind(' '), lines))
    ls = [[l, (w + 1) * amount - l.rfind(' ')] for l in lines]
    for i, line in enumerate(ls):
        ls[i][0] = line[0] + ' ' * line[1]
    return '\n'.join(map(lambda l: l[0], ls))

### Unit tests below ###
def check(candidate):
    assert candidate('\n', 2) == ' '

def test_check():
    check(f)