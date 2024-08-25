def f(text: str, delimiter: str) -> str:
    """"""
    ### Canonical solution below ###
    text = text.rpartition(delimiter)
    return text[0] + text[-1]

### Unit tests below ###
def check(candidate):
    assert candidate('xxjarczx', 'x') == 'xxjarcz'

def test_check():
    check(f)