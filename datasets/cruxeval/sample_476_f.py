def f(a: str, split_on: str) -> bool:
    """"""
    ### Canonical solution below ###
    t = a.split()
    a = []
    for i in t:
        for j in i:
            a.append(j)
    if split_on in a:
        return True
    else:
        return False

### Unit tests below ###
def check(candidate):
    assert candidate("booty boot-boot bootclass", 'k') == False

def test_check():
    check(f)