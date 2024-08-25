from typing import List

def f(lst: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                lst.sort()
    return lst

### Unit tests below ###
def check(candidate):
    assert candidate([63, 0, 1, 5, 9, 87, 0, 7, 25, 4]) == [0, 0, 1, 4, 5, 7, 9, 25, 63, 87]

def test_check():
    check(f)