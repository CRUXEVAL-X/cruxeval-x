def f(text: str, suffix: str) -> str:
    """"""
    ### Canonical solution below ###
    text += suffix
    while text[-len(suffix):] == suffix:
        text = text[:-1]
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('faqo osax f', 'f') == 'faqo osax '

def test_check():
    check(f)