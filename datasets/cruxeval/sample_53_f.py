from typing import List

def f(text: str) -> List[int]:
    """"""
    ### Canonical solution below ###
    occ = {}
    for ch in text:
        name = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f'}
        name = name.get(ch, ch)
        occ[name] = occ.get(name, 0) + 1
    return [x for _, x in occ.items()]

### Unit tests below ###
def check(candidate):
    assert candidate("URW rNB") == [1, 1, 1, 1, 1, 1, 1]

def test_check():
    check(f)