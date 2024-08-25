from typing import Tuple

def f(row: str) -> Tuple[int, int]:
    """"""
    ### Canonical solution below ###
    return (row.count('1'), row.count('0'))

### Unit tests below ###
def check(candidate):
    assert candidate("100010010") == (3, 6)

def test_check():
    check(f)