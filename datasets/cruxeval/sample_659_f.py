from typing import List

def f(bots: List[str]) -> int:
    """"""
    ### Canonical solution below ###
    clean = []
    for username in bots:
        if not username.isupper():
            clean.append(username[:2] + username[-3:])
    return len(clean)

### Unit tests below ###
def check(candidate):
    assert candidate(['yR?TAJhIW?n', 'o11BgEFDfoe', 'KnHdn2vdEd', 'wvwruuqfhXbGis']) == 4

def test_check():
    check(f)