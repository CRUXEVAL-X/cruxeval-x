def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    trans = str.maketrans('"\'><', '9833')
    return text.translate(trans)

### Unit tests below ###
def check(candidate):
    assert candidate("Transform quotations\"\nnot into numbers.") == 'Transform quotations9\nnot into numbers.'

def test_check():
    check(f)