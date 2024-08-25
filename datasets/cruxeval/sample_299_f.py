def f(text: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    if not text.endswith(char):
        return f(char + text, char)
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('staovk', 'k') == 'staovk'

def test_check():
    check(f)