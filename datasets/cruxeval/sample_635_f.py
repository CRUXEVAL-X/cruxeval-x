def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    valid_chars = ['-', '_', '+', '.', '/', ' ']
    text = text.upper()
    for char in text:
        if char.isalnum() == False and char not in valid_chars:
            return False
    return True

### Unit tests below ###
def check(candidate):
    assert candidate("9.twCpTf.H7 HPeaQ^ C7I6U,C:YtW") == False

def test_check():
    check(f)