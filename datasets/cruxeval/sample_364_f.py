from typing import List, Callable, Union

def f(nums: List[int]) -> Union[List[List[int]], str]:
    """"""
    ### Canonical solution below ###
    verdict = lambda x: x < 2
    res = [x for x in nums if x != 0]
    result = [[x, verdict(x)] for x in res]
    if result:
        return result
    return 'error - no numbers or all zeros!'

### Unit tests below ###
def check(candidate):
    assert candidate([0, 3, 0, 1]) == [[3, False], [1, True]]

def test_check():
    check(f)