def f(text: str, letter: str) -> int:
    """"""
    ### Canonical solution below ###
    t = text
    for alph in text:
        t = t.replace(alph, "")
    return len(t.split(letter))

### Unit tests below ###
def check(candidate):
    assert candidate("c, c, c ,c, c", "c") == 1

def test_check():
    check(f)