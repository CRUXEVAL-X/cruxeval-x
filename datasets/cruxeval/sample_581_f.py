def f(text: str, sign: str) -> str:
    """"""
    ### Canonical solution below ###
    length = len(text)
    new_text = list(text)
    sign = list(sign)
    for i in range(len(sign)):
        new_text.insert((i * length - 1) // 2 + (i + 1) // 2, sign[i])
    return ''.join(new_text)

### Unit tests below ###
def check(candidate):
    assert candidate('akoon', 'sXo') == 'akoXoosn'

def test_check():
    check(f)