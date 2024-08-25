def f(text: str, value: str) -> str:
    """"""
    ### Canonical solution below ###
    length = len(text)
    index = 0
    while length > 0:
        value = text[index] + value
        length -= 1
        index += 1
    return value

### Unit tests below ###
def check(candidate):
    assert candidate('jao mt', 'house') == 'tm oajhouse'

def test_check():
    check(f)