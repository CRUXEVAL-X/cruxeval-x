from typing import List, Tuple

def f(tuple_list: Tuple[int,int,int,int], joint: str) -> str:
    """"""
    ### Canonical solution below ###
    string = ''
    for num in tuple_list:
        string += dict.fromkeys(str(num), joint * len(str(num))).popitem()[0] + joint
    return string

### Unit tests below ###
def check(candidate):
    assert candidate((32332, 23543, 132323, 33300), ',') == '2,4,2,0,'

def test_check():
    check(f)