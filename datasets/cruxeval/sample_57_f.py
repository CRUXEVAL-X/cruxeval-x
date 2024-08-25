def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    text = text.upper()
    count_upper = 0
    for char in text:
        if char.isupper():
            count_upper += 1
        else:
            return 'no'
    return count_upper // 2

### Unit tests below ###
def check(candidate):
    assert candidate('ax') == 1

def test_check():
    check(f)