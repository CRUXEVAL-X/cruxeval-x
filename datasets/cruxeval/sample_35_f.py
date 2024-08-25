from typing import List

def f(pattern: str, items: List[str]) -> List[int]:
    """"""
    ### Canonical solution below ###
    result = []
    for text in items:
        pos = text.rfind(pattern)
        if pos >= 0:
            result.append(pos)

    return result

### Unit tests below ###
def check(candidate):
    assert candidate(" B ", [" bBb ", " BaB ", " bB", " bBbB ", " bbb"]) == []

def test_check():
    check(f)