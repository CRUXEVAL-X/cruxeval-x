from typing import List

def f(my_list: List[str]) -> int:
    """"""
    ### Canonical solution below ###
    count = 0
    for i in my_list:
        if len(i) % 2 == 0:
            count += 1
    return count

### Unit tests below ###
def check(candidate):
    assert candidate(['mq', 'px', 'zy']) == 3
    
def test_check():
    check(f)