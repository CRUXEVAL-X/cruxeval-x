def f(text: str, value: str) -> str:
    """"""
    ### Canonical solution below ###
    new_text = list(text)
    try:
        new_text.append(value)
        length = len(new_text)
    except IndexError:
        length = 0
    return '[' + str(length) + ']'

### Unit tests below ###
def check(candidate):
    assert candidate('abv', 'a') == '[4]'

def test_check():
    check(f)