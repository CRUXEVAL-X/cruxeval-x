def f(txt: str, marker: int) -> str:
    """"""
    ### Canonical solution below ###
    a = []
    lines = txt.split('\n')
    for line in lines:
        a.append(line.center(marker))
    return '\n'.join(a)

### Unit tests below ###
def check(candidate):
    assert candidate('#[)[]>[^e>\n 8', -5) == '#[)[]>[^e>\n 8'

def test_check():
    check(f)