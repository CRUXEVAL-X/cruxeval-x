def f(text: str, symbols: str) -> str:
    """"""
    ### Canonical solution below ###
    count = 0
    if symbols:
        for i in symbols:
            count += 1
        text = text * count
    return text.rjust(len(text) + count*2)[:-2]

### Unit tests below ###
def check(candidate):
    assert candidate('', 'BC1ty') == '        '

def test_check():
    check(f)