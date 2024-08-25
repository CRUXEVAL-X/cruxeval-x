def f(text: str, chars: str) -> str:
    """"""
    ### Canonical solution below ###
    chars = list(chars)
    text = list(text)
    new_text = text
    while len(new_text) > 0 and text:
        if new_text[0] in chars:
            new_text = new_text[1:]
        else:
            break 
    return ''.join(new_text)

### Unit tests below ###
def check(candidate):
    assert candidate('asfdellos', 'Ta') == 'sfdellos'

def test_check():
    check(f)