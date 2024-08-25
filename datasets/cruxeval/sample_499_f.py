def f(text: str, length: int, fillchar: str) -> str:
    """"""
    ### Canonical solution below ###
    size = len(text)
    return text.center(length, fillchar)

### Unit tests below ###
def check(candidate):
    assert candidate('magazine', 25, '.') == '.........magazine........'

def test_check():
    check(f)