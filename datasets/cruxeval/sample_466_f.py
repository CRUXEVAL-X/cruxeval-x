def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    length = len(text)
    index = 0
    while index < length and text[index].isspace():
        index += 1
    return text[index:index+5]

### Unit tests below ###
def check(candidate):
    assert candidate('-----\t\n\tth\n-----') == '-----'

def test_check():
    check(f)