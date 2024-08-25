from typing import List

def f(numbers: List[int], index: int) -> List[int]:
    """"""
    ### Canonical solution below ###
    for n in numbers[index:]:
        numbers.insert(index, n)
        index += 1
    return numbers[:index]

### Unit tests below ###
def check(candidate):
    assert candidate([-2, 4, -4], 0) == [-2, 4, -4]

def test_check():
    check(f)