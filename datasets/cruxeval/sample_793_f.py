from typing import List

def f(lst: List[int], start: int, end: int) -> int:
    """"""
    ### Canonical solution below ###
    count = 0
    for i in range(start, end):
        for j in range(i, end):
            if list[i] != list[j]:
                count += 1
    return count

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 4, 3, 2, 1], 0, 3) == 3

def test_check():
    check(f)