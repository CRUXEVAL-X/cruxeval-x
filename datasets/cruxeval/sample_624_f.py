def f(text: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    char_index = text.find(char)
    result = []
    if char_index > 0:
        result = list(text[:char_index])
    result.extend(list(char)+list(text[char_index+len(char):]))
    return ''.join(result)

### Unit tests below ###
def check(candidate):
    assert candidate('llomnrpc', 'x') == 'xllomnrpc'

def test_check():
    check(f)