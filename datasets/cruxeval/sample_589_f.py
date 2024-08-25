from typing import List

def f(num: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    num.append(num[-1])
    return num

### Unit tests below ###
def check(candidate):
    assert candidate([-70, 20, 9, 1]) == [-70, 20, 9, 1, 1]

def test_check():
    check(f)