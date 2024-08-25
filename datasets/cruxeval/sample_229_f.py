from typing import Dict, Any, List

def f(dic: Dict[str, int], value: int) -> List[str]:
    """"""
    ### Canonical solution below ###
    result = []
    for e in dic:
        result.append(e[0])
        if e[1] == value:
            result.reverse()
        else:
            result.append(e[1])
    return result

### Unit tests below ###
def check(candidate):
    assert candidate({'9m':2, 'mA':1, '10K':2, 'Lk':2}, 1) == ['9', 'm', 'm', 'A', '1', '0', 'L', 'k']

def test_check():
    check(f)