def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    return max(text.find(ch) for ch in 'aeiou')

### Unit tests below ###
def check(candidate):
    assert candidate("qsqgijwmmhbchoj") == 13

def test_check():
    check(f)