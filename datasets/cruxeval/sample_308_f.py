from typing import List, Dict

def f(strings: List[str]) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    occurances = {}
    for string in strings:
        if string not in occurances:
            occurances[string] = strings.count(string)
    return occurances

### Unit tests below ###
def check(candidate):
    assert candidate(["La", "Q", "9", "La", "La"]) == {'La': 3, 'Q': 1, '9': 1}

def test_check():
    check(f)