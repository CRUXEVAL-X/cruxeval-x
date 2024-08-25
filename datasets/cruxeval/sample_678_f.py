from typing import Dict

def f(text: str) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    freq = dict()
    for c in text.lower():
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

### Unit tests below ###
def check(candidate):
    assert candidate("HI") == {'h': 1, 'i': 1}

def test_check():
    check(f)