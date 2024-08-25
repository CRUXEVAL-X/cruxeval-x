from typing import List

def f(list_x: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    item_count = len(list_x)
    new_list = []
    for i in range(item_count):
        new_list.append(list_x.pop())
    return new_list

### Unit tests below ###
def check(candidate):
    assert candidate([5, 8, 6, 8, 4]) == [4, 8, 6, 8, 5]

def test_check():
    check(f)