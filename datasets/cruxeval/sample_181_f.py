from typing import List, Tuple

def f(s: str) -> Tuple[str, int]:
    """"""
    ### Canonical solution below ###
    count = 0
    digits = ""
    for c in s:
        if c.isdigit():
            count += 1
            digits += c
    return (digits, count)

### Unit tests below ###
def check(candidate):
    assert candidate("qwfasgahh329kn12a23") == ('3291223', 7)

def test_check():
    check(f)