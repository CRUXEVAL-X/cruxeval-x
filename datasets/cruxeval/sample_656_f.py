from typing import List

def f(letters: List[str]) -> str:
    """"""
    ### Canonical solution below ###
    a = [] 
    for i in range(len(letters)):
        if letters[i] in a:
            return 'no'
        a.append(letters[i]) 
    return 'yes'

### Unit tests below ###
def check(candidate):
    assert candidate(['b', 'i', 'r', 'o', 's', 'j', 'v', 'p']) == 'yes'

def test_check():
    check(f)