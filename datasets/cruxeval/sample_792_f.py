from typing import List, Dict, Any

def f(l1: List[str], l2: List[str]) -> Dict[str, List[str]]:
    """"""
    ### Canonical solution below ###
    if len(l1) != len(l2):
        return {}
    return dict.fromkeys(l1, l2)

### Unit tests below ###
def check(candidate):
    assert candidate(['a', 'b'], ['car', 'dog']) == {'a': ['car', 'dog'], 'b': ['car', 'dog']}

def test_check():
    check(f)