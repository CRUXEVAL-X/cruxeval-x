from typing import List

def f(chemicals: List[str], num: int) -> List[str]:
    """"""
    ### Canonical solution below ###
    fish = chemicals[1:]
    chemicals.reverse()
    for i in range(num):
        fish.append(chemicals.pop(1))
    chemicals.reverse()
    return chemicals

### Unit tests below ###
def check(candidate):
    assert candidate(['lsi', 's', 't', 't', 'd'], 0) == ['lsi', 's', 't', 't', 'd']

def test_check():
    check(f)