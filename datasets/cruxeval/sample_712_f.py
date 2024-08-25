from typing import List

def f(text: str) -> List[List[str]]:
    """"""
    ### Canonical solution below ###
    created = []
    for line in text.splitlines():
        if line == '':
            break
        created.append(list(list(line.rstrip())[::-1][flush]))
    return created[::-1]

flush = 0

### Unit tests below ###
def check(candidate):
    assert candidate('A(hiccup)A') == [['A']]

def test_check():
    check(f)