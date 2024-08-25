def f(text: str, speaker: str) -> str:
    """"""
    ### Canonical solution below ###
    while text.startswith(speaker):
        text = text[len(speaker):]
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('[CHARRUNNERS]Do you know who the other was? [NEGMENDS]', '[CHARRUNNERS]') == 'Do you know who the other was? [NEGMENDS]'

def test_check():
    check(f)