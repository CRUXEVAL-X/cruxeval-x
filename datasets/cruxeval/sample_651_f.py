def f(text: str, letter: str) -> str:
    """"""
    ### Canonical solution below ###
    if letter.islower(): letter = letter.upper()
    text = ''.join([letter if char == letter.lower() else char for char in text])
    return text.capitalize()

### Unit tests below ###
def check(candidate):
    assert candidate('E wrestled evil until upperfeat', 'e') == 'E wrestled evil until upperfeat'

def test_check():
    check(f)