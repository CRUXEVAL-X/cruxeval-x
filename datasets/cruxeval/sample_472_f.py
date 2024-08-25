from typing import List

def f(text: str) -> List[int]:
    """"""
    ### Canonical solution below ###
    d = {}
    for char in text.replace('-', '').lower():
        d[char] = d[char] + 1 if char in d else 1
    d = sorted(d.items(), key=lambda x: x[1])
    return [val for i, val in d]

### Unit tests below ###
def check(candidate):
    assert candidate("x--y-z-5-C") == [1, 1, 1, 1, 1]

def test_check():
    check(f)