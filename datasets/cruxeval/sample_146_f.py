from typing import List

def f(single_digit: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    result = []
    for c in range(1, 11):
        if c != single_digit:
            result.append(c)
    return result

### Unit tests below ###
def check(candidate):
    assert candidate(5) == [1, 2, 3, 4, 6, 7, 8, 9, 10]

def test_check():
    check(f)