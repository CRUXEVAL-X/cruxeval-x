from typing import List

def f(array: List[str]) -> List[str]:
    """"""
    ### Canonical solution below ###
    c = array
    array_copy = array

    while True:
        c.append('_')
        if c == array_copy:
            array_copy[c.index('_')] = ''
            break
        
    return array_copy

### Unit tests below ###
def check(candidate):
    assert candidate([]) == ['']

def test_check():
    check(f)