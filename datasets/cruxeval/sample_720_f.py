from typing import List

def f(items: List[str], item: str) -> int:
    """"""
    ### Canonical solution below ###
    while items[-1] == item:
        items.pop()
    items.append(item)
    return len(items)

### Unit tests below ###
def check(candidate):
    assert candidate(['bfreratrrbdbzagbretaredtroefcoiqrrneaosf'], 'n') == 2

def test_check():
    check(f)