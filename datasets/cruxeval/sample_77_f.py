def f(text: str, character: str) -> str:
    """"""
    ### Canonical solution below ###
    subject = text[text.rfind(character):]
    return subject*text.count(character)

### Unit tests below ###
def check(candidate):
    assert candidate('h ,lpvvkohh,u', 'i') == ''

def test_check():
    check(f)