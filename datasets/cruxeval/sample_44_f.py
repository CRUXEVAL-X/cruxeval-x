def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    ls = list(text)
    for i in range(0, len(ls)):
        if ls[i]!='+':
            ls.insert(i, '+')
            ls.insert(i, '*')
            break
    return '+'.join(ls)

### Unit tests below ###
def check(candidate):
    assert candidate('nzoh') == '*+++n+z+o+h'

def test_check():
    check(f)