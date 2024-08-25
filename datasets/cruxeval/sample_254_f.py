def f(text: str, repl: str) -> str:
    """"""
    ### Canonical solution below ###
    trans = str.maketrans(text.lower(), repl.lower())
    return text.translate(trans)

### Unit tests below ###
def check(candidate):
    assert candidate('upper case', 'lower case') == 'lwwer case'

def test_check():
    check(f)