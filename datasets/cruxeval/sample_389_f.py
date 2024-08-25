from typing import List, Union

def f(total: List[str], arg: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    if type(arg) is list:
        for e in arg:
            total.extend(e)
    else:
        total.extend(arg)
    return total

### Unit tests below ###
def check(candidate):
    assert candidate(['1', '2', '3'], 'nammo') == ['1', '2', '3', 'n', 'a', 'm', 'm', 'o']

def test_check():
    check(f)