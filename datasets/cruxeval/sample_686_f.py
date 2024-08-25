from typing import Dict, List

def f(d: Dict[str, int], l: List[str]) -> Dict[str, int]:
    """"""
	### Canonical solution below ###
    new_d = {}

    for k in l:
        if d.get(k) is not None:
            new_d[k] = d[k]

    return new_d.copy()

### Unit tests below ###
def check(candidate):
    assert candidate({"lorem ipsum" : 12, "dolor" : 23}, ["lorem ipsum", "dolor"]) == {'lorem ipsum': 12, 'dolor': 23}

def test_check():
    check(f)