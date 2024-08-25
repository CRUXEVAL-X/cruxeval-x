def f(needle: str, haystack: str) -> int:
    """"""
    ### Canonical solution below ###
    count = 0
    while needle in haystack:
        haystack = haystack.replace(needle, '', 1)
        count += 1
    return count

### Unit tests below ###
def check(candidate):
    assert candidate('a', 'xxxaaxaaxx') == 4

def test_check():
    check(f)