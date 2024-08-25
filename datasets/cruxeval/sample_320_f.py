def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    index = 1
    while index < len(text):
        if text[index] != text[index - 1]:
            index += 1
        else:
            text1 = text[:index]
            text2 = text[index:].swapcase()
            return text1 + text2
    return text.swapcase()

### Unit tests below ###
def check(candidate):
    assert candidate('USaR') == 'usAr'

def test_check():
    check(f)