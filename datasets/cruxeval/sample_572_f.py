from typing import Dict, Any, List, Tuple

def f(data: Dict[int, Any], num: int) -> List[Tuple[Tuple[int, Any], Any]]:
    """"""
    ### Canonical solution below ###
    new_dict = {}
    temp = list(data.items())
    for i in range(len(temp) - 1, num - 1, -1):
        new_dict[temp[i]] = None
    return temp[num:] + list(new_dict.items())

### Unit tests below ###
def check(candidate):
    assert candidate({1: 9, 2: 10, 3: 1}, 1) == [(2, 10), (3, 1), ((3, 1), None), ((2, 10), None)]

def test_check():
    check(f)