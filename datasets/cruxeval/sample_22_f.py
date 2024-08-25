from typing import Union, List

def f(a: int) -> Union[List[int], int]:
    """"""
    ### Canonical solution below ###
    if a == 0:
        return [0]
    result = []
    while a > 0:
        result.append(a%10)
        a = a//10
    result.reverse()
    return int(''.join(str(i) for i in result))

### Unit tests below ###
def check(candidate):
    assert candidate(000) == [0]

def test_check():
    check(f)