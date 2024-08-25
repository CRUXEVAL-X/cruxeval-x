def f(text: str, prefix: str) -> str:
    """"""
    ### Canonical solution below ###
    while text.startswith(prefix):
        text = text[len(prefix):] or text
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('ndbtdabdahesyehu', 'n') == 'dbtdabdahesyehu'

def test_check():
    check(f)