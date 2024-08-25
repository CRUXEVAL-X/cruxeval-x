def f(strand: str, zmnc: str) -> int:
    """"""
    ### Canonical solution below ###
    poz = strand.find(zmnc)
    while poz != -1:
        strand = strand[poz + 1:]
        poz = strand.find(zmnc)
    return strand.rfind(zmnc)

### Unit tests below ###
def check(candidate):
    assert candidate('', 'abc') == -1

def test_check():
    check(f)