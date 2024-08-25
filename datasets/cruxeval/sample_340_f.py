def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    uppercase_index = text.find('A')
    if uppercase_index >= 0:
        return text[:uppercase_index] + text[text.find('a') + 1 :]
    else:
        return ''.join(sorted(text))

### Unit tests below ###
def check(candidate):
    assert candidate('E jIkx HtDpV G') == '   DEGHIVjkptx'

def test_check():
    check(f)