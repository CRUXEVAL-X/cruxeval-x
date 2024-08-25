from typing import Dict,Tuple

def f(d: Dict[str, int]) -> Tuple[int,int]:
    """"""
    ### Canonical solution below ###
    if 'x' in d:
        x = d['x']
    if 'y' in d:
        y = d['y']
    return x,y

### Unit tests below ###
def check(candidate):
    assert candidate({'x': 5, 'y': 12}) == (5, 12)
    
def test_check():
    check(f)