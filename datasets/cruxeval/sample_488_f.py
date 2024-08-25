def f(text: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    count = text.count(char)
    chars = list(text)
    if count > 0:
        index = chars.index(char) + 1
        chars[:index:index+1] = [c for c in chars[index:index+count:1]]
    return ''.join(chars)

### Unit tests below ###
def check(candidate):
    assert candidate('tezmgvn 651h', '6') == '5ezmgvn 651h'

def test_check():
    check(f)