from typing import Dict, List

def f(nums: Dict[str, str]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    copy = nums.copy()
    newDict = dict()
    for k in copy:
        newDict[k] = len(copy[k])
    return newDict

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)