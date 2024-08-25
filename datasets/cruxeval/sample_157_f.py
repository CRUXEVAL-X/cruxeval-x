def f(phrase: str) -> int:
    """"""
    ### Canonical solution below ###
    ans = 0
    for w in phrase.split():
        for ch in w:
            if ch == "0":
                ans += 1
    return ans

### Unit tests below ###
def check(candidate):
    assert candidate("aboba 212 has 0 digits") == 1

def test_check():
    check(f)