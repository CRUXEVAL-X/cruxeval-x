from typing import List

def f(numbers: List[str], num: int, val: int) -> str:
    """"""
    ### Canonical solution below ###
    while len(numbers) < num:
        numbers.insert(len(numbers) // 2, val)
    for _ in range(len(numbers) // (num - 1) - 4):
        numbers.insert(len(numbers) // 2, val)
    return ' '.join(numbers)

### Unit tests below ###
def check(candidate):
    assert candidate([], 0, 1) == ''

def test_check():
    check(f)