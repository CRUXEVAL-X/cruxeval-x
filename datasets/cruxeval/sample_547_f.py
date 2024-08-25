def f(letters: str) -> str:
    """"""
    ### Canonical solution below ###
    letters_only = letters.strip("., !?*")
    return "....".join(letters_only.split(" "))

### Unit tests below ###
def check(candidate):
    assert candidate("h,e,l,l,o,wo,r,ld,") == 'h,e,l,l,o,wo,r,ld'

def test_check():
    check(f)