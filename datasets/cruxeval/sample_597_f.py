def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    return s.upper()

### Unit tests below ###
def check(candidate):
    assert candidate("Jaafodsfa SOdofj AoaFjIs  JAFasIdfSa1") == 'JAAFODSFA SODOFJ AOAFJIS  JAFASIDFSA1'

def test_check():
    check(f)