from typing import Dict

def f(a: Dict[str, int], b: Dict[str, int]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    return {**a, **b}

### Unit tests below ###
def check(candidate):
    assert candidate({'w': 5, 'wi': 10}, {'w': 3}) == {'w': 3, 'wi': 10}

def test_check():
    check(f)