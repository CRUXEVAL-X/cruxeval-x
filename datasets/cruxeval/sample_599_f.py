from typing import List

def f(a: List[str], b: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    a = b.join(a)
    lst = []
    for i in range(1, len(a)+1, 2):
        lst.append(a[i-1:][:i])
        lst.append(a[i-1:][i:])
    return lst

### Unit tests below ###
def check(candidate):
    assert candidate(["a", "b", "c"], " ") == ['a', ' b c', 'b c', '', 'c', '']

def test_check():
    check(f)