from typing import List, Union

def f(instagram: List[str], imgur: List[str], wins: int) -> Union[str, List[str]]:
    """"""
    ### Canonical solution below ###
    photos = [instagram, imgur]
    if instagram == imgur:
        return wins
    if wins == 1:
        return photos.pop()
    else:
        photos.reverse()
        return photos.pop()

### Unit tests below ###
def check(candidate):
    assert candidate(['sdfs', 'drcr', '2e'], ['sdfs', 'dr2c', 'QWERTY'], 0) == ['sdfs', 'drcr', '2e']

def test_check():
    check(f)