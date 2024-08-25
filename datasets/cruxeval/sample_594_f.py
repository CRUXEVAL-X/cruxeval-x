def f(file: str) -> int:
    """"""
    ### Canonical solution below ###
    return file.index('\n')

### Unit tests below ###
def check(candidate):
    assert candidate("n wez szize lnson tilebi it 504n.\n") == 33

def test_check():
    check(f)