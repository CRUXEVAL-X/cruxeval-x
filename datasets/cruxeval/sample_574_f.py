from typing import List

def f(simpons: List[str]) -> str:
    """"""
    ### Canonical solution below ###
    while simpons:
        pop = simpons.pop()
        if pop == pop.title():
            return pop
    return pop

### Unit tests below ###
def check(candidate):
    assert candidate(['George', 'Michael', 'George', 'Costanza']) == 'Costanza'

def test_check():
    check(f)