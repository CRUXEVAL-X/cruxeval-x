def f(a: str, b: str, c: str, d: str) -> str:
    """"""
    ### Canonical solution below ###
    return a and b or c and d

### Unit tests below ###
def check(candidate):
    assert candidate('CJU', 'BFS', 'WBYDZPVES', 'Y') == 'BFS'

def test_check():
    check(f)