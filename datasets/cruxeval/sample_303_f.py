def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    i = (len(text) + 1) // 2
    result = list(text)
    while i < len(text):
        t = result[i].lower()
        if t == result[i]:
            i += 1
        else:
            result[i] = t
        i += 2
    return ''.join(result)

### Unit tests below ###
def check(candidate):
    assert candidate('mJkLbn') == 'mJklbn'

def test_check():
    check(f)