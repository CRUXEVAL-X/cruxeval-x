def f(text: str, res: int) -> str:
    """"""
    ### Canonical solution below ###
    for c in '*\n"':
        text = text.replace(c, '!' + str(res))
    if text.startswith('!'):
        text = text[len(str(res)):]
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('"Leap and the net will appear', 123) == '3Leap and the net will appear'

def test_check():
    check(f)