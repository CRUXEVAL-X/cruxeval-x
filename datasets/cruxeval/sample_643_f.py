def f(text: str, suffix: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.endswith(suffix):
        text = text[:-1] + text[-1:].swapcase()
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('damdrodm', 'm') == 'damdrodM'

def test_check():
    check(f)