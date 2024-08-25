def f(text: str, position: int, value: str) -> str:
    """"""
    ### Canonical solution below ###
    length = len(text)
    index = position % (length)
    if position < 0:
        index = length // 2
    new_text = list(text)
    new_text.insert(index, value)
    new_text.pop(length-1)
    return ''.join(new_text)

### Unit tests below ###
def check(candidate):
    assert candidate('sduyai', 1, 'y') == 'syduyi'

def test_check():
    check(f)