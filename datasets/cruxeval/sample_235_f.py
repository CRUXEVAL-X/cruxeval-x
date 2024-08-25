from typing import List

def f(array: List[str], arr: List[str]) -> List[str]:
    """"""
    ### Canonical solution below ###
    result = []
    for s in arr:
        result += list(filter(lambda l: l != '', s.split(arr[array.index(s)])))
    return result

### Unit tests below ###
def check(candidate):
    assert candidate([], []) == []

def test_check():
    check(f)