from typing import Tuple

def f(text: str) -> Tuple[int, int]:
    """"""
    ### Canonical solution below ###
    ws = 0
    for s in text:
        if s.isspace():
            ws += 1
    return ws, len(text)

### Unit tests below ###
def check(candidate):
    assert candidate("jcle oq wsnibktxpiozyxmopqkfnrfjds") == (2, 34)

def test_check():
    check(f)