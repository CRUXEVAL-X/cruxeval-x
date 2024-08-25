from typing import List

def f(s: str, characters: List[int]) -> List[str]:
    """"""
    ### Canonical solution below ###
    return [s[i:i+1] for i in characters]

### Unit tests below ###
def check(candidate):
    assert candidate('s7 6s 1ss', [1, 3, 6, 1, 2]) == ['7', '6', '1', '7', ' ']

def test_check():
    check(f)