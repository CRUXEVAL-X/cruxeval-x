from typing import Union

def f(length: int, text: str) -> Union[str, bool]:
    """"""
    ### Canonical solution below ###
    if len(text) == length:
        return text[::-1]
    return False

### Unit tests below ###
def check(candidate):
    assert candidate(-5, 'G5ogb6f,c7e.EMm') == False

def test_check():
    check(f)