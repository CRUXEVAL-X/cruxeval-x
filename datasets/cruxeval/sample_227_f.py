def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    text = text.lower()
    head, tail = text[0], text[1:]
    return head.upper() + tail

### Unit tests below ###
def check(candidate):
    assert candidate('Manolo') == 'Manolo'

def test_check():
    check(f)