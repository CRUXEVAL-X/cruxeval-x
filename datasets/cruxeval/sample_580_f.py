from typing import List

def f(text: str, char: str) -> List[int]:
    """"""
    ### Canonical solution below ###
    new_text = text
    a = []
    while char in new_text:
        a.append(new_text.index(char))
        new_text = new_text.replace(char,"",1)
    return a

### Unit tests below ###
def check(candidate):
    assert candidate('rvr', 'r') == [0, 1]

def test_check():
    check(f)