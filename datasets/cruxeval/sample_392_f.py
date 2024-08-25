def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.upper() == text:
        return 'ALL UPPERCASE'
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('Hello Is It MyClass') == 'Hello Is It MyClass'

def test_check():
    check(f)