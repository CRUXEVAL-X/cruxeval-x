def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    result = []
    for i in range(len(text)):
        if not text[i].isascii():
            return False
        elif text[i].isalnum():
            result.append(text[i].upper())
        else:
            result.append(text[i])
    return ''.join(result)

### Unit tests below ###
def check(candidate):
    assert candidate("ua6hajq") == 'UA6HAJQ'

def test_check():
    check(f)