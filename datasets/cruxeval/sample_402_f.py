from typing import List, Dict

def f(n: int, l: List[str]) -> Dict[int, int]:
    """"""
    ### Canonical solution below ###
    archive = {}
    for _ in range(n):
        archive.clear()
        archive.update({x + 10: x * 10 for x in l})
    return archive

### Unit tests below ###
def check(candidate):
    assert candidate(0, ['aaa', 'bbb']) == {}

def test_check():
    check(f)