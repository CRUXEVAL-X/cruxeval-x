def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    for i in range(len(text)):
        if text[i] == ' ':
            text = text.replace(' ', '\t', 1)
    return text.expandtabs(4)

### Unit tests below ###
def check(candidate):
    assert candidate('\n\n\t\tz\td\ng\n\t\t\te') == '\n\n        z   d\ng\n            e'

def test_check():
    check(f)