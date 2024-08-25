def f(text: str, comparison: str) -> int:
    """"""
    ### Canonical solution below ###
    length = len(comparison)
    if length <= len(text):
        for i in range(length):
            if comparison[length - i - 1] != text[len(text) - i - 1]:
                return i
    return length

### Unit tests below ###
def check(candidate):
    assert candidate("managed", "") == 0

def test_check():
    check(f)