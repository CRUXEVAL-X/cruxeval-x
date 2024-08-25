from typing import List

def f(in_list: List[int], num: int) -> int:
    """"""
    ### Canonical solution below ###
    in_list.append(num)
    return in_list.index(max(in_list[:-1]))

### Unit tests below ###
def check(candidate):
    assert candidate([-1, 12, -6, -2], -1) == 1

def test_check():
    check(f)