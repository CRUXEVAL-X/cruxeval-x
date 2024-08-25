from typing import List

def f(array: List[int], target: int) -> int:
    """"""
    ### Canonical solution below ###
    count, i = 0, 1
    for j in range(1, len(array)):
        if ((array[j] > array[j-1]) and (array[j] <= target)): count += i
        elif array[j] <= array[j-1]: i = 1
        else: i += 1
    return count

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, -1, 4], 2) == 1

def test_check():
    check(f)