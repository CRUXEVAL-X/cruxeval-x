from typing import List

def f(list_: List[str], num: int) -> List[str]:
    """"""
    ### Canonical solution below ###
    temp = []
    for i in list_:
        i = num // 2 * ('%s,' % i)
        temp.append(i)
    return temp

### Unit tests below ###
def check(candidate):
    assert candidate(['v'], 1) == ['']

def test_check():
    check(f)