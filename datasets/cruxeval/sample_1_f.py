from typing import Tuple, Dict, Optional

def f(a: Tuple[int, int], b: Tuple[int, int], c: Tuple[int, int]) -> Dict[int,Optional[int]]:
    """"""
    ### Canonical solution below ###
    result = {}
    for d in a, b, c:
        result.update(dict.fromkeys(d))
    return result

### Unit tests below ###
def check(candidate):
    assert candidate((1, 3), (1, 4), (1, 2)) == {1: None, 2: None, 3: None, 4: None}

def test_check():
    check(f)