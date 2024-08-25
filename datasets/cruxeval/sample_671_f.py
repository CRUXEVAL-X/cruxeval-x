def f(text: str, char1: str, char2: str) -> str:
    """"""
    ### Canonical solution below ###
    t1a = []
    t2a = []
    for i in range(len(char1)):
        t1a.append(char1[i])
        t2a.append(char2[i])
    t1 = text.maketrans(dict(zip(t1a, t2a)))
    return text.translate(t1)

### Unit tests below ###
def check(candidate):
    assert candidate("ewriyat emf rwto segya", "tey", "dgo") == 'gwrioad gmf rwdo sggoa'

def test_check():
    check(f)