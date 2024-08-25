from typing import List

def f(st: str, pattern: List[str]) -> bool:
    """"""
    ### Canonical solution below ###
    for p in pattern:
        if not st.startswith(p): return False
        st = st[len(p):]
    return True

### Unit tests below ###
def check(candidate):
    assert candidate('qwbnjrxs', ['jr', 'b', 'r', 'qw']) == False

def test_check():
    check(f)