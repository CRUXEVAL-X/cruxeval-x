from typing import Union

def f(num: int) -> Union[str, int]:
    """"""
    ### Canonical solution below ###
    if num % 2 == 0:
        return s
    else:
        return num - 1

### Unit tests below ###
def check(candidate):
    assert candidate(21) == 20

def test_check():
    check(f)