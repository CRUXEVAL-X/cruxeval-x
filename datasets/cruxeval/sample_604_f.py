def f(text: str, start: str) -> bool:
    """"""
    ### Canonical solution below ###
    return text.startswith(start)

### Unit tests below ###
def check(candidate):
    assert candidate("Hello world", "Hello") == True

def test_check():
    check(f)