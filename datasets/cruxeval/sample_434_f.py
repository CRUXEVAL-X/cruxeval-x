def f(string: str) -> int:
    """"""
    ### Canonical solution below ###
    try:
       return string.rfind('e')
    except AttributeError:
        return "Nuk"

### Unit tests below ###
def check(candidate):
    assert candidate('eeuseeeoehasa') == 8

def test_check():
    check(f)