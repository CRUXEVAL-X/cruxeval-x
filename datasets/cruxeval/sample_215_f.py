def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    new_text = text
    while len(text) > 1 and text[0] == text[-1]:
        new_text = text = text[1:-1]
    return new_text

### Unit tests below ###
def check(candidate):
    assert candidate(')') == ')'

def test_check():
    check(f)