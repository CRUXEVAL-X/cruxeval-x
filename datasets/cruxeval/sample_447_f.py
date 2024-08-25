def f(text: str, tab_size: int) -> str:
    """"""
    ### Canonical solution below ###
    res = ''
    text = text.replace('\t', ' '*(tab_size-1))
    for i in range(len(text)):
        if text[i] == ' ':
            res += '|'
        else:
            res += text[i]
    return res

### Unit tests below ###
def check(candidate):
    assert candidate("\ta", 3) == '||a'

def test_check():
    check(f)