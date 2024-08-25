def f(txt: str) -> int:
    """"""
    ### Canonical solution below ###
    coincidences = {}
    for c in txt:
        if c in coincidences:
            coincidences[c] += 1
        else:
            coincidences[c] = 1
    return sum(coincidences.values())

### Unit tests below ###
def check(candidate):
    assert candidate("11 1 1") == 6

def test_check():
    check(f)