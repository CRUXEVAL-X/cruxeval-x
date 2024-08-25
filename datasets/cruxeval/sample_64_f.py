def f(text: str, size: int) -> str:
    """"""
    ### Canonical solution below ###
    counter = len(text)
    for i in range(size-int(size%2)):
        text = ' '+text+' '
        counter += 2
        if counter >= size:
            return text

### Unit tests below ###
def check(candidate):
    assert candidate("7", 10) == '     7     '

def test_check():
    check(f)