def f(x: str) -> str:
    """"""
    ### Canonical solution below ###
    return " ".join(list(x)[::-1])

### Unit tests below ###
def check(candidate):
    assert candidate("lert dna ndqmxohi3") == '3 i h o x m q d n   a n d   t r e l'

def test_check():
    check(f)