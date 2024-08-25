def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    for i in range(len(text)-1, 0, -1):
        if not text[i].isupper():
            return text[0:i]
    return ''

### Unit tests below ###
def check(candidate):
    assert candidate('SzHjifnzog') == 'SzHjifnzo'

def test_check():
    check(f)