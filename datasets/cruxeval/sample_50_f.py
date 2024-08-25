from typing import List

def f(lst: List[str]) -> List[int]:
    """"""
    ### Canonical solution below ###
    lst.clear()
    lst += [1] * (len(lst) + 1)
    return lst

### Unit tests below ###
def check(candidate):
    assert candidate(['a', 'c', 'v']) == [1]

def test_check():
    check(f)