from typing import Dict

def f(s: str) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    count = {}
    for i in s:
        if i.islower():
            count[i.lower()] = s.count(i.lower()) + count.get(i.lower(), 0)
        else:
            count[i.lower()] = s.count(i.upper()) + count.get(i.lower(), 0)
    return count

### Unit tests below ###
def check(candidate):
    assert candidate("FSA") == {'f': 1, 's': 1, 'a': 1}

def test_check():
    check(f)