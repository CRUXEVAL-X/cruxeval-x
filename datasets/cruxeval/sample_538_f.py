def f(text: str, width: int) -> str:
    """"""
    ### Canonical solution below ###
    return text[:width].center(width, 'z')

### Unit tests below ###
def check(candidate):
    assert candidate('0574', 9) == 'zzz0574zz'

def test_check():
    check(f)