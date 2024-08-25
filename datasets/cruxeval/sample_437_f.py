from typing import List, Dict

def f(tap_hierarchy: List[str]) -> Dict[str, None]:
    """"""
    ### Canonical solution below ###
    hierarchy = {}
    for gift in tap_hierarchy:
        hierarchy = hierarchy.fromkeys(gift, None)
    return hierarchy

### Unit tests below ###
def check(candidate):
    assert candidate(['john', 'doe', 'the', 'john', 'doe']) == {'d': None, 'o': None, 'e': None}

def test_check():
    check(f)