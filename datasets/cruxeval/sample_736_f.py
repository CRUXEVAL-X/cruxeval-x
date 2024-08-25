def f(text: str, insert: str) -> str:
    """"""
    ### Canonical solution below ###
    whitespaces = {'\t', '\r', '\v', ' ', '\f', '\n'}
    clean = ''
    for char in text:
        if char in whitespaces:
            clean += insert
        else:
            clean += char
    return clean

### Unit tests below ###
def check(candidate):
    assert candidate('pi wa', 'chi') == 'pichiwa'

def test_check():
    check(f)