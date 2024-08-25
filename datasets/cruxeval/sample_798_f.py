def f(text: str, pre: str) -> str:
    """"""
    ### Canonical solution below ###
    if not text.startswith(pre):
        return text
    return text.removeprefix(pre)

### Unit tests below ###
def check(candidate):
    assert candidate('@hihu@!', '@hihu') == '@!'

def test_check():
    check(f)