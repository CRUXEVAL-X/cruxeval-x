from typing import List

def f(numbers: List[str], prefix: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    return sorted(n[len(prefix):] if (len(n) > len(prefix) and n.startswith(prefix)) else n
                  for n in numbers)

### Unit tests below ###
def check(candidate):
    assert candidate(['ix', 'dxh', 'snegi', 'wiubvu'], '') == ['dxh', 'ix', 'snegi', 'wiubvu']

def test_check():
    check(f)