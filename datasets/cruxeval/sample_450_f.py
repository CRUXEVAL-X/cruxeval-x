def f(strs: str) -> str:
    """"""
    ### Canonical solution below ###
    strs = strs.split()
    for i in range(1, len(strs), 2):
        strs[i] = ''.join(reversed(strs[i]))
    return ' '.join(strs)

### Unit tests below ###
def check(candidate):
    assert candidate('K zBK') == 'K KBz'

def test_check():
    check(f)