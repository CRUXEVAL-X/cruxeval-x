def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    a = text.strip().split(' ')
    for i in range(len(a)):
        if a[i].isdigit() is False:
            return '-'
    return " ".join(a)

### Unit tests below ###
def check(candidate):
    assert candidate("d khqw whi fwi bbn 41") == '-'

def test_check():
    check(f)